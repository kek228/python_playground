# Coroutines and Tasks

## Coroutines
WHAT is coroutine? Something which can be entered, exited, and resumed at many different points.
For this async-await syntax is used. 
Just calling coro() returns coroutine object.
There are 3 ways to start coroutines:
1. asyncio.run(main()) -> main is a coroutine.
2. await coro() in the body of OTHER CORO
3. asyncio.create_task()

## Awaitables
What can be "awaited". Coroutine object, obviously. asyncio.Task.
And Futures. Futures is an "eventual result" of async operation.

## Running an asyncio Program
asyncio.run(coro, *, debug=False)
Execute the coroutine coro and return the result of coro.
!!! This function cannot be called when another asyncio event loop is running in the same thread
ALWAYS creates a new loop and closes it in the end.

## Creating Tasks
asyncio.create_task(coro()) executed in the loop returned by get_running_loop().
asyncio.gather(*aws, loop=None, return_exceptions=False) -> runs tasks and returns a list of returned results

## Task Object
A Future-like object that runs a Python coroutine. So task manages coro, it might be canceled. Event loop runs Tasks



# STREAMS
Streams are high-level async/await-ready primitives to work with network connections.
Streams allow sending and receiving data without using callbacks or low-level protocols and transports.
