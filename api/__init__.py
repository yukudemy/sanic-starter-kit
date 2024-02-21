from sanic import Blueprint

from .learner import(
	bp_group_learner
	)

bp_group_api = Blueprint.group(
	bp_group_learner,
	url_prefix="/api"
	)

__all__=(
	bp_group_api
	)