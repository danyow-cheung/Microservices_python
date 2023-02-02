from quart import url_for 
import asyncio
from c2_quart_convert import app 

async def run_url_for():
    async with app.test_request_context('/',method='GET'):
        print(url_for('person',name='Alice'))

loop = asyncio.get_event_loop()
loop.run_until_complete(run_url_for())
