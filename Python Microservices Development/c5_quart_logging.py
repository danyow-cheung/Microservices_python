import logging
from quart import Quart,request 

app = Quart(__name__)
app.logger.setLevel(logging.INFO)

@app.route("/hello")
def hello_handler():
    app.logger.info("hello_handler called")
    app.logger.debug(f"The request was {request}")
    return {"hello":"World!"}

if __name__=="__main__":
    app.run(debug=True)