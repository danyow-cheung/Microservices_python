class Config:
    DEBUG = False 
    SQLURI  = 'postgres://username:xxx@localhost/db'

'''
可以添加到代碼中
from quart import Quart
>>> import pprint
>>> pp = pprint.PrettyPrinter(indent=4)
>>> app = Quart(__name__)
>>> app.config.from_object('prod_settings.Config') >>> pp.pprint(app.config)
'''


'''
很容易添加json，yaml等配置
>>> from quart import Quart
>>> import yaml
>>> from pathlib import Path
>>> app = Quart(__name__)
>>> print(Path("prod_settings.json").read_text()) {
    "DEBUG": false,
    "SQLURI":"postgres://username:xxx@localhost/db"
}
>>> app.config.from_json("prod_settings.json") >>> app.config["SQLURI"] 'postgres://username:xxx@localhost/db'
>>> print(Path("prod_settings.yml").read_text()) ---
DEBUG: False
SQLURI: "postgres://username:xxx@localhost/db"
>>> app.config.from_file("prod_settings.yml", yaml.safe_load)
'''