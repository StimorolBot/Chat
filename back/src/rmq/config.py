from aio_pika import connect


HOST = "localhost"
PORT = 5672
LOGIN = "guest"
PASSWORD = "guest"

EXCHANGE = ""
ROUTING_KEY = "error"


async def get_connection() -> connect:
    return await connect(host=HOST, port=PORT, login=LOGIN, password=PASSWORD)

