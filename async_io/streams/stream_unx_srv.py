import asyncio
import uvloop


async def handle_echo(reader, writer):
    while True:
        data = await reader.read(100)
        message = data.decode()
        addr = writer.get_extra_info('peername')

        print(f"Received {message!r} from {addr!r}")

        print(f"Send: {message!r}")
        writer.write(data)
        await writer.drain()


async def main():
    server = await asyncio.start_unix_server(handle_echo, path='\0test_socket')

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

# asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)

loop = uvloop.new_event_loop()
asyncio.set_event_loop(loop)
loop = asyncio.get_event_loop()
assert isinstance(loop, uvloop.Loop)

asyncio.run(main())
