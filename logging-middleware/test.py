import asyncio
from logger import log_event

async def main():
    result = await log_event(
        level="info",
        package="service",
        message="Logger test successful"
    )

    print(result)

asyncio.run(main())