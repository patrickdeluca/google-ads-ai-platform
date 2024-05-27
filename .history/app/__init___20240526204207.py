from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import Config
from dotenv import load_dotenv
import os

db = SQLAlchemy()
ma = Marshmallow()

def create_app(config_class=Config):
    app = Flask(__name__)
    load_dotenv()
    app.config.from_object(config_class)

    db.init_app(app)
    ma.init_app(app)

    from app.routes import account, campaign, ad_group, ad, ai, negative_keyword
    app.register_blueprint(account.bp)
    app.register_blueprint(campaign.bp)
    app.register_blueprint(ad_group.bp)
    app.register_blueprint(ad.bp)
    app.register_blueprint(ai.bp)
    app.register_blueprint(negative_keyword.bp)

    return app