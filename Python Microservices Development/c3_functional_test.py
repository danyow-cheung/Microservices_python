import unittest
import json
from quart_basic import app as tested_app # not this repo


class TestApp(unittest.IsolatedAsyncioTestCase):
    async def test_help(self):
        app = tested_app.test_client()

        hello = await app.get('/api')

        body = json.load(str(await hello.get_data(),'utf-8'))

        self.assertEqual(body['Hello'],"WORLD!")

if __name__=='__main__':
    unittest.main()