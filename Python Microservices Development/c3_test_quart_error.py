'''
寫一個測試c2_quart_error.py的文件
'''
import unittest
import json 
from c2_quart_error_handler import app as tested_app,text_404 

class TestApp(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        # create  a client to interact with the app 
        self.app  = tested_app.test_client()
    
    async def test_raise(self):
        hello = await self.app.get("/api")
        self.assertEqual(hello.status_code,500)
    
    async def test_proper_404(self):
        # call a non-existing endpoint
        hello = await self.app.get('/drrgow')
        self.assertEqual(hello.status_code,404)
        # we get a nice JSON body
        body = json.loads(str(await hello.get_data(),'utf-8'))
        self.assertEqual(hello.status_code,404)
        self.assertEqual(body['Error'],'404 NOT FOUND: The requested URL was not found on the server.If you entered the URL maually please check your spelling and try again.')
        self.assertEqual(body['Description'],text_404)
if __name__=='__main__':
    unittest.main()
