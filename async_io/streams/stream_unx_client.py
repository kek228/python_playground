import asyncio
import uvloop

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_unix_connection(path='\0test_socket')
    while True:
        writer.write(message.encode())
        await writer.drain()
        data = await reader.read(100)
        print(f'Received: {data.decode()!r}')
        await asyncio.sleep(1)

    writer.close()
    await writer.wait_closed()


# asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)

loop = uvloop.new_event_loop()
asyncio.set_event_loop(loop)

loop = asyncio.get_event_loop()
assert isinstance(loop, uvloop.Loop)


asyncio.run(tcp_echo_client('Hello World!'))
