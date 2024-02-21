
# api/learner/home/__init__.py
from sanic import Blueprint
from .home import(
	bp_home_home
	)


bp_group_home = Blueprint.group(
	bp_home_home,
	url_prefix="/home"
	)

__all__=(
	bp_group_home
	)