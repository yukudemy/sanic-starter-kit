# api_v1/content/__init__.py
from sanic import Blueprint
from .practice import(
	bp_practice_practice
	)
from .stream_video import(
	bp_handler_file_stream_practice
	)
from.get_practice import(
	bp_get_practice_practice
	)


bp_group_practice = Blueprint.group(
	bp_practice_practice,
	bp_handler_file_stream_practice,
	bp_get_practice_practice,
	url_prefix="/practice"
	)

__all__=(
	bp_group_practice
	)


