from sanic.views import HTTPMethodView
from sanic.response import text
from sanic.response import json
from sanic import Blueprint
from sanic import response

bp_handler_file_stream_practice= Blueprint("stream_video")

class StreamVideo(HTTPMethodView):

  async def get(self, request):
      return await response.file_stream(
        "path/to/some file.mp4",
        chunk_size=1024,
        mime_type="application/metalink4+xml",
        headers={
            "Content-Disposition": 'Attachment; filename="nicer_name.meta4"',
            "Content-Type": "application/metalink4+xml",
        },
    )

  # You can also use async syntax
  async def post(self, request):
      return text("I am post method")

  def put(self, request):
      return text("I am put method")

  def patch(self, request):
      return text("I am patch method")

  def delete(self, request):
      return text("I am delete method")


bp_handler_file_stream_practice.add_route(
  StreamVideo.as_view(),
  "stream_video"
  )
