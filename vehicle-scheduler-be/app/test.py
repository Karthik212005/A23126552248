import asyncio
from service import get_depots, get_vehicles, knapsack
from config import ACCESS_TOKEN

async def main():
    depots = await get_depots(ACCESS_TOKEN)
    vehicles = await get_vehicles(ACCESS_TOKEN)

    depots_list = depots["depots"]
    vehicles_list = vehicles["vehicles"]

    first_depot = depots_list[0]

    result = knapsack(
        first_depot["MechanicHours"],
        vehicles_list
    )

    print(result)

asyncio.run(main())