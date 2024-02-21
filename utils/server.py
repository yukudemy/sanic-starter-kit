from sanic import Sanic
from sanic import Sanic
from sanic.response import text
from api import(
	bp_group_api
	)

app = Sanic("SanicStarterTemplate")

@app.get("/")
async def hello_kit(request):
    return text("Hello, from Sanic Starter Kit.")



app.blueprint(
	bp_group_api
	)

