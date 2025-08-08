from os import name, environ
from flask  import Flask, redirect, url_for, request, render_template, session, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv


def create_app():
    app = Flask(__name__)
    app.secret_key = "firstkeyletsgo"
    return app