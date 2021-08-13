
import aiohttp
import json
import time
import asyncio

async def time_getter(session, location='Bucharest'):
    response = await session.request(method='GET', url=f'http://worldtimeapi.org/api/timezone/Europe/{location}')
    my_time = await response.text()
    return json.loads(my_time)

async def timezone_getter(session):
    response = await session.request(method='GET', url='http://worldtimeapi.org/api/timezone')
    time_zones = await response.text()
    time_zones = json.loads(time_zones)
    result = filter(lambda x:x ,map(lambda zone : zone.rsplit("/", maxsplit=1)[-1] if "Europe" in zone else None, time_zones))
    return result

async def get_world_time():
    async with aiohttp.ClientSession() as session:
        start_time = time.time()
        task0 = await asyncio.gather(timezone_getter(session))
        task = await asyncio.gather(*(time_getter(session, i) for i in task0))
        end_time = time.time()
        print(f'total time: {end_time - start_time}')
        print(task)

if __name__ == "__main__":
    asyncio.run(get_world_time())
