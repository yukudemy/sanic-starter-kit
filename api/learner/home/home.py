from sanic.views import HTTPMethodView
from sanic.response import text
from sanic.response import json
from sanic import Blueprint
from sanic import response

bp_home_home= Blueprint("home_home")

class Home(HTTPMethodView):

  def get(self, request):
      return text("Hello, home.")

  # You can also use async syntax
  async def post(self, request):
      return text("I am post method")

  def put(self, request):
      return text("I am put method")

  def patch(self, request):
      return text("I am patch method")

  def delete(self, request):
      return text("I am delete method")


bp_home_home.add_route(
  Home.as_view(),
  "/"
  )

