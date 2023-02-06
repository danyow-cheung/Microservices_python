# run command:
# c3_molotov_example.py --processes 10 --workers 200 --duration 60 
import json 
from molotov import scenario

@scenario(weight=40)
async def scenario_one(session):
    async with session.get('http://localhost:5000/api') as resp:
        res =await resp.json()
        assert res['Hello'] = 'World!'
        assert resp.status == 200


@scenario(weight=60)
async def scenario_two(session):
    async with session.get('http://localhost:5000/api') as resp:
        assert resp.status == 200

