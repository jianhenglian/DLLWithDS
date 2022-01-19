from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from config import config
from flask_wtf import CSRFProtect

bootstrap = Bootstrap()
moment = Moment()


UPLOAD_FOLDER = 'D:\\self_learning\\flask\\dataH\\app\\main\\learnText2\\alldocuments'


def create_app():
    app = Flask(__name__)
    app.config.from_object(config['default'])
    config['default'].init__app(app)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    bootstrap.init_app(app)
    moment.init_app(app)
    # CSRFProtect(app)

    from .main import main as main_blueprint
    app.add_url_rule(
        "/uploads/<name>", endpoint="download_file", build_only=True
    )
    # app.add_url_rule("/divideResult")
    app.register_blueprint(main_blueprint)

    return app
