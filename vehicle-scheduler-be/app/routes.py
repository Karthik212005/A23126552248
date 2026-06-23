from fastapi import APIRouter
from service import get_depots, get_vehicles, knapsack
from config import ACCESS_TOKEN

router = APIRouter()


@router.get("/depots")
async def depots():
    try:
        data = await get_depots(ACCESS_TOKEN)
        return data
    except Exception as e:
        return {"error": str(e)}


@router.get("/vehicles")
async def vehicles():
    try:
        data = await get_vehicles(ACCESS_TOKEN)
        return data
    except Exception as e:
        return {"error": str(e)}


@router.get("/schedule")
async def schedule():
    try:
        depots_response = await get_depots(ACCESS_TOKEN)
        vehicles_response = await get_vehicles(ACCESS_TOKEN)

        depots = depots_response["depots"]
        vehicles = vehicles_response["vehicles"]

        results = []

        for depot in depots:
            optimized = knapsack(
                depot["MechanicHours"],
                vehicles
            )

            results.append({
                "DepotID": depot["ID"],
                "MechanicHours": depot["MechanicHours"],
                "TotalImpact": optimized["totalImpact"],
                "SelectedTasks": optimized["selectedTasks"]
            })

        return results

    except Exception as e:
        return {"error": str(e)}