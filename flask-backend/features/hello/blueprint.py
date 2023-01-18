from flask import current_app, Blueprint

admin = Blueprint("admin", __name__, url_prefix="/admin")


@admin.route("/hello", strict_slashes=False)
def index():
    return "Hello G_G"
