from flask.blueprints import Blueprint
from . import routes



auth_bp = Blueprint("auth", __name__)


auth_bp.add_url_rule("/signup", view_func=routes.sign_up, methods=["POST"])
auth_bp.add_url_rule("/signin", view_func=routes.sign_in, methods=["POST"])
