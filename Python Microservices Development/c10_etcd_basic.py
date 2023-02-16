from quart import Quart,current_app 
import etcd3 

# can read this map from a tranditional config file
setting_map ={
    'dataset_url':'/services/dataservice/url'
}

setting_reverse_map = {v:k for k,v in setting_map.items()}

etcd_client = etcd3.client()
def load_settings():
    config = dict()
    for setting,etcd_key in setting_map.items():
        config[setting] = etcd_client.get(etcd_key)[0].decode('utf-8')
    return config

def create_app(name=__name__):
    app = Quart(__name__)
    app.config.update(load_settings())
    return app 

def watch_callback(event):
    global app 
    for update in event.events:
        # determine which settings to update,and convert from bytes to str 
        config_option = setting_reverse_map[update.key.decode('utf-8')]
        app.config[config_option] = update.value.decode('utf-8')

# start to watch for dataservice url changes 
# you can also watch entire areas with add_watch_prefix_callback
watch_id = etcd_client.add_watch_callback('/services/dataservice/url')
watch_callback()

@app.route('/api')
def what_is_url():
    return {"url":app.config['dataservice_url']}
app.run()
