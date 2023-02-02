
from quart import Quart,request,jsonify 


app = Quart(__name__)

@app.route("/api",provide_automatic_options = False)
async def my_microservice():
    print(dir(request))
    response = jsonify({"hello":'world'})
    print(response)
    print(await response.get_data())
    return response

@app.route('/person/<person_id>')
def person(person_id):
    return {'hello':person_id}

@app.route('/')
def index():
    return 'hello quart'

@app.route('/price/<float:money>')
def price(money):
    return 'money is'+str(money)+"$"


if __name__ =='__main__':
    print(app.url_map)
    app.run(debug=True)

