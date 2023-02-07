import os 
import aiohttp 
from quart import Quart,request,render_template ,login_required,redirct,url_for


app = Quart(__name__)

@app.route("/")
# @login_required
async def welcome_page():
    client_id = os.environ['SLACK_CLIENT_ID']
    return await render_template('welcome.html',client_id=client_id)
    # return await render_template('welcome.html')


@app.route("/slack/callback")
async def oauth2_slack_callback():
    code = request.args['code']

    client_id = os.environ['SLACK_CLIENT_ID']
    client_secret = os.environ['SLACK_CLIENT_SECRET']
    access_url = f"https://slack.com/api/oauth.v2.access?client_id={client_id}&client_secret={client_secret}&code={code}"
    async with aiohttp.ClientSession() as session:
        async with session.get(access_url) as resp:
            access_data = await resp.json()
            print(access_data)
    
    
    return await render_template('logged_in.html')
if __name__=="__main__":
    app.run(debug=True)
