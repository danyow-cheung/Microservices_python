from quart import Quart 
from quart_cors import cors 

app = Quart(__name__)
app = cors(app,allow_origin='https://quart.com')

@app.route('/api')
async def my_microservice():
    return {"Hello":"World"}
