from datetime import datetime
from jinja2 import Template
from email.utils import format_datetime
import time 
def render_email(**data):
    with open("email_template.j2") as f:
        template = Template(f.read())
    return template.render(**data)


data = {
    # 'data':time.time(),# 不顯示why
    'to':"danyow@danyow.com",
    'from':'danyowChan',
    'subject':'shopping',
    'name':'ac', 
    'items':[
        {"name":'a','price':1},
        {"name":'a','price':1},
        {"name":'a','price':1},
    ],
}
print(render_email(**data))
