
import time
import asyncio
from datetime import  datetime

async def get_time():
    await asyncio.sleep(2)
    print(f'finished time: {datetime.now()}')

async def main():
    start_time = time.time()
    await asyncio.gather(get_time(), get_time())
    end_time = time.time()
    print(f'Execution time: {end_time - start_time}')

if __name__ == "__main__":
    asyncio.run(main())
