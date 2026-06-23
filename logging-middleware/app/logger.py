import httpx
from config import TOKEN

LOG_URL = "http://4.224.186.213/evaluation-service/logs"

async def log_event(level, package, message):

    payload = {
        "stack": "backend",
        "level": level,
        "package": package,
        "message": message
    }

    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                LOG_URL,
                json=payload,
                headers=headers
            )

            print(response.status_code)
            return response.json()

    except Exception as e:
        print("Logging Error:", e)