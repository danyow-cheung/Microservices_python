from quart import Quart,request 
from werkzeug.routing import BaseConverter,ValidationError


_USERS = {"1":"Alice","2":"danniel"}
_IDS = {val:user_id for user_id ,val in _USERS.items()}

class RegisteredUser(BaseConverter):
    def to_python(self, value):
        if value in _USERS:
            return _USERS[value]
        raise ValidationError()
    

        # return super().to_python(value)

    def to_url(self,value):
        return _IDS[value]
    
app = Quart(__name__)
app.url_map.converters['registered'] = RegisteredUser
@app.route('/api/person/<registered:name>')
def person(name):
    return {"hello":name}
if __name__ =='__main__':
    app.run(debug=True)

