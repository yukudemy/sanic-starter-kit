
from sanic.views import HTTPMethodView
from sanic.response import text
from sanic.response import json
from sanic import Blueprint

bp_get_practice_practice = Blueprint("get_practice")

class GetPratice(HTTPMethodView):

  def get(self, request):
      return json({"my": "blueprint"})

  # You can also use async syntax
  async def post(self, request):
      return text("I am post method")

  def put(self, request):
      return text("I am put method")

  def patch(self, request):
      return text("I am patch method")

  def delete(self, request):
      return text("I am delete method")



bp_get_practice_practice.add_route(
  GetPratice.as_view(),
  "get_practice"
  )
