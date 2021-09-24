import asyncio
import time
import selectors

# STARTING COROS:

#  way1
async def main1():
    print('hello')
    await asyncio.sleep(1)
    print('world')


# way2
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main2():
    print(f"started at {time.strftime('%X')}")
    await say_after(1, 'hello')
    await say_after(2, 'world')
    print(f"finished at {time.strftime('%X')}")


# way3
async def main3():
    # create_task returns asyncio.Task object
    # When a coroutine is wrapped into a Task with functions like asyncio.create_task()
    # the coroutine is automatically scheduled to run soon:
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))
    print(f"started at {time.strftime('%X')}")
    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")


# might be a coro, but might not
async def fill_fut(fut):
    await asyncio.sleep(1)
    fut.set_result('FUT RES')
    return 0

# awaiting on futures
async def futures_example():
    loop = asyncio.get_running_loop()
    my_fut = loop.create_future()
    await fill_fut(my_fut)
    res = await my_fut
    print(f'res = {res}')
    return 100500

res = asyncio.run(futures_example())
print(f'asyncio.run res: {res}')


