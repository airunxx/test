from os import path
from typing import List
from flask import Flask, render_template, request, session, app, redirect, make_response
from DB import *
import secrets
from datetime import datetime
from flask_bcrypt import Bcrypt

# localhost = socket.gethostbyname(socket.gethostname())
localhost = '127.0.0.1'

app = Flask(__name__)
bcrypt = Bcrypt(app)

@app.route('/')
@app.route('/home')
def home():
    if "ID" in session:
        return render_template('home.html', logininfo="당신은 회원입니다.")
    return render_template('home.html', logininfo="당신은 비회원입니다.")

@app.route('/logout',methods=['POST'])
def logout():
    session.clear()
    return redirect("http://{0}:8080/home".format(localhost))

@app.route('/user')
def user():
    return render_template('notice.html')

@app.route("/register")
def register():
    return render_template('regist.html')

@app.route("/registfinish",methods=['POST'])
def registfinish():
    if request.method == "POST":
        email = request.form['email']
        pwd = request.form['pwd']
        nickname = request.form['nik']
        pw_hash = bcrypt.generate_password_hash(pwd).decode('utf-8')
        createacc(nickname, email, pw_hash)
        return redirect('http://{0}:8080/login'.format(localhost))
    else:
        return render_template("wrongaccess.html")
    
@app.route("/loginfinish",methods=['POST', 'GET'])
def loginfinish():
    if request.method == "POST":
        emails = request.form['idl']
        pwds = request.form['pwdl']
        if bringemail(emails) is None:
            print("DB에 등록된 정보가 없습니다.")
            return redirect('http://{0}:8080/login'.format(localhost))
        password1 = str(bringpassword(emails)).encode(encoding="utf-8")
        if bcrypt.check_password_hash(password1, pwds):
            print("로그인 성공")
            print(checkuserrank(emails))
            if "30_day" not in checkuserrank(emails):
                now = datetime.now()
                date_to_compare = bringcreatetime(emails)
                date_diff = now - date_to_compare
                print ("차이: ", date_diff.days)
                a = int(date_diff.days)
                if a >= 30:
                    print ("유저랭크 30_day 설정완료!")
                    setuserrank(emails, "30_day")
            session['loggedina'] = True
            session['ID'] = emails
            session['username'] = checklogin(emails, bringpassword(emails))
            session['userrank'] = checkuserrank(emails)
            return redirect('http://{0}:8080/home'.format(localhost))
        else:
            print("로그인 실패")
            return redirect('http://{0}:8080/login'.format(localhost))
    else:
        return render_template("wrongaccess.html")

@app.route("/rement")
def rearrangement():
    info = 'userinfo'
    ID = 'USERID'
    numberset(info, ID)
    msg = "에러방지"
    return msg

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/checkcookie",methods=['POST', 'GET'])
def checkcookie():
    if request.method == "POST":
        name = request.cookies.get("userID")
        print(name)
        return redirect('http://{0}:8080/home'.format(localhost))
  
@app.route("/removecookies",methods=['POST'])
def removecookies():
    if request.method == "POST":
        resp = make_response("setcookie")
        resp.set_cookie('userID', '', expires=0)
        resp.set_cookie('pwd', '', expires=0)
        print("쿠키삭제완료!")
        return redirect('http://{0}:8080/home'.format(localhost))
    else:
        return render_template("wrongaccess.html")
    
@app.route("/accountinfo")
def accountinfo():
    if session['loggedina'] == True:
        return render_template("account.html", user=session['username'])
    return redirect('http://{0}:8080/home'.format(localhost))

@app.route("/recent_change")
def recent_change():
    bringrecent()
    return render_template("recent.html")

@app.route("/edit/<pagename>")
def edit(pagename):
    if "ID" not in session:
        session['ID'] = request.environ.get(request.remote_addr)
        session['userrank'] = "normal"
        session['loggedina'] = "X"
        print(request.remote_addr)
    if checktext(pagename) is None:
        if session['loggedina'] == "X":
            createtext(pagename, session['id'])
        else:
            return redirect('http://{0}:8080/home'.format(localhost))
    abc = checktext(pagename)
    return render_template("edit.html", edittext=abc, edittitle=pagename)

@app.route("/w/<pagename>")
def w(pagename):
    print(checktext(pagename))
    return render_template("viewer.html", title=pagename, text=checktext(pagename), editnumber=checkrnumber(pagename))
    
@app.route("/editfinish", methods=['POST', 'GET'])
def editfinish():
    if request.method == "POST":
        nickname = request.form['edittext']
        title = request.form['submit']
        count = len(nickname)
        if session['loggedina'] != "X":
            print(session['ID'])
            addeditcount(session['ID'])
            beforeedit(session['ID'], title)
            print("test")
            if "50_day" not in checkuserrank(session['id']):
                if 50 >= int(bringcounter(session['id'])):
                    setuserrank(session['id'], "50_edit")
        print("닉네임 ", nickname)
        print("타이틀 ", title)
        changetext(nickname, title, count)
        createrecent(title, session['ID'], checkrnumber(title), count)
        return redirect('http://{0}:8080/w/{1}'.format(localhost, title))
    else:
        return render_template("wrongaccess.html")

@app.route('/asdw')
def asdw():
    return render_template("index.html")

@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    if request.method == "POST":
        user = request.form['nm']
    emails = "bugdoliii@gmail.com"
    resp = make_response("Cookie Setting Complete")
    resp.set_cookie("userID", user)
    resp.set_cookie("pwd", bringpassword(emails))
    return resp

@app.route("/acl/<pagename>")
def acl(pagename):
    return render_template("ACL.html")

@app.route("/getcookie")
def getcookie():
    name = request.cookies.get("userID")
    pwd = request.cookies.get("pwd")
    return '<h1>welcome '+name+pwd+'</h1>'

@app.route("/removetext/<pagename>")
def removetext(pagename):
    dbremovetext(pagename)
    return redirect('http://{0}:8080/home'.format(localhost))

if __name__ == '__main__':
    secret = secrets.token_hex(nbytes=32)
    app.secret_key = secret
    app.config['SECRET_KEY'] = secret
    app.config['Bcrypt_LEVEL'] = 10
    app.run(port=8080)