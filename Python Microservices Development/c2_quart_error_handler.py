from quart import Quart
app = Quart(__name__)

@app.errorhandler(500)
def error_handling(error):
    return {"Error":str(error)},500 

@app.route("/api")
def my_microservice():
    raise TypeError('SomeException')
if __name__ =='__main__':
    app.run(debug=True)
