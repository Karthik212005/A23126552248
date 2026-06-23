import httpx

BASE_URL = "http://4.224.186.213/evaluation-service"


async def get_depots(token):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{BASE_URL}/depots",
            headers=headers
        )

        print("DEPOTS STATUS:", response.status_code)
        print("DEPOTS RESPONSE:", response.text)

        return response.json()


async def get_vehicles(token):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{BASE_URL}/vehicles",
            headers=headers
        )

        print("VEHICLES STATUS:", response.status_code)
        print("VEHICLES RESPONSE:", response.text)

        return response.json()
    
def knapsack(capacity, vehicles):
    n = len(vehicles)

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        duration = vehicles[i - 1]["Duration"]
        impact = vehicles[i - 1]["Impact"]

        for w in range(capacity + 1):
            if duration <= w:
                dp[i][w] = max(
                    impact + dp[i - 1][w - duration],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    selected = []
    w = capacity

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(vehicles[i - 1])
            w -= vehicles[i - 1]["Duration"]

    selected.reverse()

    return {
        "totalImpact": dp[n][capacity],
        "selectedTasks": [task["TaskID"] for task in selected]
    }