from flask import Blueprint
from . import routes



org_bp = Blueprint("organization", __name__)



org_bp.add_url_rule("/organization", view_func=routes.create_organization, methods=["POST"])
org_bp.add_url_rule("/organization/<organization_id>", view_func=routes.get_organization, methods=["GET"])
