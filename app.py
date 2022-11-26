from flask import Flask
from flask import render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user
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

# 1.Userテーブルを定義
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(50),nullable=False, unique=True)
    password = db.Column(db.String(12))
    # mymessageid = db.Column(db.Integer, db.ForeignKey("MyMessage.id"))
    # relasionid = db.Column(db.Integer, db.ForeignKey("Relation.id"))

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fromuser = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, unique=False)
    touser = db.Column(db.Integer, unique=False, nullable=False)
    content = db.Column(db.String(300), nullable=False)
    # created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone("Asia/Tokyo")))

class ChatRoom(db.Model):
    name = db.Column(db.String, primary_key=True)
    # messages = db.relationship("Relation",cascade="delete")
    # username = db.Column(db.String, db.ForeignKey("user.username"), primary_key=True)

class Relation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String)
    # user_name = db.Column(db.String, db.ForeignKey("user.username"))
    # chatroom = db.Column(db.String, db.ForeignKey("ChatRoom.name"))

class MyMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # messageid = db.Column(db.Integer, db.ForeignKey("Message.id"))


@Login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# -------------------------------- コード記述 -------------------------------- #

#【2-1】: ユーザログイン機能 (パスワード変更後の再ログインでエラー発生中)
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if check_password_hash(user.password, password):
            login_user(user)
            return redirect("/home")
    else:
        # flash("「メールアドレス」または「パスワード」に誤りがあります。")
        return render_template("login.html")

#【2-2】: 新規ユーザ登録画面(済)
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        email= request.form.get("email")
        password = request.form.get("password")

        user = User(username=username, email=email, password=generate_password_hash(password, method="sha256"))

        db.session.add(user)
        db.session.commit()
        return redirect("/")

    else:
        return render_template("signup.html")

#【2-3】: パスワード再設定(済)
@app.route("/forget", methods=["GET", "POST"])
def forget():
    if request.method == "POST":
        email= request.form.get("email")
        newpass = request.form.get("newpass")
        newword = request.form.get("newword")

        user = User.query.filter_by(email=email).first()
        if newpass == newword:
            user.password = newpass = generate_password_hash(newpass, method="sha256")
            db.session.add(user)
            db.session.commit()
            return redirect("/")
        else:
            return redirect("/forget")

    else:
        return render_template("forget.html")


#【3-1】: home画面 
@app.route("/home")
@login_required
def home():
    # user = User.query.all()
    # return render_template('home/list.html', user=user)
    return render_template("home.html")
# -------------------- 挙動項目 -------------------- -------------------- 挙動項目 -----------------------
# ⑦ データベース(Relationテーブル)からつながりユーザー(id / ユーザ名)を全件取得する。
# ⑦ 取得したデータを/usertop.html(仮)に表示させる
# ⑦ ↓
# ⑦ リストからユーザを選択できる様にする
# ⑦ ボタン押下によってチャットルームに画面遷移する(遷移先で選択したユーザ情報が自動的抽出される)

# ⑧ ボタン押下によってつながりユーザ検索ページに画面遷移する

# ⑨ ボタン押下によってユーザ情報変更/削除ページに画面遷移する

# 17. ボタン押下によってログアウト処理が実行される
# 17. ↓
# 17. ログアウト処理が実行された後【2-1】に画面遷移する
# -------------------- 挙動項目 ---------------------- -------------------- 挙動項目 ----------------------


#【ユーザ内容変更】acount.html
@app.route("/account", methods=["GET", "POST"])
@login_required
def account():
    user = User.query.all()
    if request.method == "POST":
        rename = request.form.get("rename")
        reemail = request.form.get("reemail")

        user = User.query.filter_by(id=user.id).first()

        if rename == "":
            user.email = reemail
        elif reemail == "":
            user.username = rename
        else:
            return redirect("/account")
            
        db.session.add(user)
        db.session.commit()
        return redirect("/account")
    else:
        return render_template("account.html")


#【友達追加】add.html
@app.route("/addfriends", methods=["GET", "POST"])
@login_required
def addfriends():


    return render_template("add.html")


#【ログアウト】(済)
@app.route("/logout", methods=["get"])
@login_required
def logout():
    logout_user()
    return redirect("/")


 #【4-1】: チャットルーム
@app.route("/chatroom" , methods=["GET", "POST"])
def chatroom():
    return render_template("chat_form.html")

#【入力フォーム】
#【退出、消去ボタン】