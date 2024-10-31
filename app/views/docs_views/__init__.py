from flask import Blueprint
from . import views


docs_bp = Blueprint("docs", __name__, url_prefix='/docs')



docs_bp.add_url_rule("/", view_func=views.index, methods=['GET'])
