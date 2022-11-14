from flask import Flask
from flask import render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, logout_user

from werkzeug.security import generate_password_hash, check_pasword_hash
import os

from datetime import datetime
import pytz

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///chat.db"
app.config["SECRET_KEY"] = os.urandom(24)
db = SQLAlchemy(app)

# ☆優先！【2-1】: ログイン画面　担当：oku









#【2-2】 : ユーザ登録画面
#【2-3】 : パスワード再設定
# ☆優先！【3-1】: ユーザTOP画面 担当：ibu









#【3-3】: ユーザ情報変更
#【3-4】: 新規つながり検索
# ☆優先！【4-1】: チャットルーム








# ---------------------------- 以下は教材youtubeで記述された模範コード（転用時は注意）----------------------------
# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///chat.db"
# app.config["SECRET_KEY"] = os.urandom(24)
# db = SQLAlchemy(app)

# login_manager = LoginManager()
# login_manager.init_app()

# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(30), unique=True, nullable=False)
#     email = db.Column(db.String(50))
#     password = db.Column(db.String(30))

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String, unique=True, nullable=False)
#     email = db.Column(db.String)

# @app.route("/")
# def index():
#     return render_template("test.html")
