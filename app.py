from flask import Flask
from flask import render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, logout_user

from werkzeug.security import generate_password_hash, check_password_hash
import os

from datetime import datetime
import pytz

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///chatapp_teamc.db"
app.config["SECRET_KEY"] = os.urandom(24)
db = SQLAlchemy(app)

Login_manager = LoginManager()
Login_manager.init_app(app)

# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(30), nullable=False, unique=True)
#     email = db.Column(db.String(50),nullable=False)
#     password = db.Column(db.String(12))
#     mymessageid = db.Column(db.Integer, db.ForeignKey("MyMessage.id"))
#     relasionid = db.Column(db.Integer, db.ForeignKey("Relation.id"))

# class Message(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     senduser = db.Column(db.ForeignKey("User.id"), nullable=False, unique=True)
#     created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone("Asia/Tokyo")))
#     content = db.Column(db.String(300), nullable=False)

# class MyMessage(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     messageid = db.Column(db.Integer, db.ForeignKey("Message.id"))

# class Relation(db.Model):
#     id = db.Column(db.Integer, primary_key=True)        







# -------------------------------- 以下にロジックを記述する ---------------------------------

#【2-1】 : 作業中☆ ユーザログイン画面 担当：奥村
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()
        if check_password_hash(user.password, password):
            login_user(user)
            return redirect("/usertop")
    else:
        return render_template("test_oku.html")






#【2-2】 : ユーザ登録画面
#【2-3】 : パスワード再設定
# ☆優先！【3-1】: ユーザTOP画面 担当：ibu









#【3-3】: ユーザ情報変更
#【3-4】: 新規つながり検索
# ☆優先！【4-1】: チャットルーム








# ---------------------------- 以下は教材youtubeで記述された模範コード（転用時は注意）----------------------------

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
