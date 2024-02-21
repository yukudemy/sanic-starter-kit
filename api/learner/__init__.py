from sanic import Blueprint

from .home import(
	bp_group_home
	)
from .practice import(
	bp_group_practice
	)

bp_group_learner = Blueprint.group(
	bp_group_home,
	bp_group_practice,
	url_prefix="/learner"
	)

__all__=(
	bp_group_practice
	)