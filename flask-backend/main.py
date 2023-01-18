from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__, static_folder="./dist", static_url_path="/")
    app.url_map.strict_slashes = False
    from features.hello.blueprint import admin

    app.register_blueprint(admin)

    @app.route("/")
    def index():
        return app.send_static_file("index.html")

    CORS(app, resources={r"/*": {"origins": "*"}})
    return app
