
from module import dbAccess
from module import check
from login import User
#importa flask
import flask
from flask import Flask, request, redirect, render_template, url_for
from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required
login_manager = LoginManager()
#nastavi flask
debug = True
app = Flask(__name__)
app.config["debug"] = True

APP_ADDRESS = "localhost"
APP_PORT = 80
APP_URL =  f"http://{APP_ADDRESS}: {APP_PORT}/"
#impora moje module
from module import dbAccess
from module import check
#zažene flask 
def main():
    app.run(host=APP_ADDRESS, port=6969 ,debug=True)
    login_manager.init_app(app)
    
@app.route('/', methods = ["GET"])
def index():
    ip=request.environ['REMOTE_ADDR']
    if dbAccess.CheckMatchIP(ip)==True:
        return redirect("/dashboard")
    else:
        return redirect("/login")
    

    
@app.route('/login', methods = ["GET", "POST"])   
def login():
    error=False
    if error==True:
        return render_template("login.html", error=False)
    if request.method == "POST":
        if request.form["login"]=="login":
            username = request.form["username"]
            password = request.form["password"]
            ip=request.environ['REMOTE_ADDR']
            valid=dbAccess.login(username, password,ip)
            if valid == False:
                ID=dbAccess.IdUser(username)
                return redirect (url_for('.dashboard', number=ID ))
            else:
                return render_template("login.html", error=True)

        elif check.IfEmpty(username) or check.IfEmpty(password):
            print("2")
            return render_template("login.html",error=True)
        else:   
            return render_template("login.html", error=False)
    else:
        print("1")
        return render_template("login.html", error=False)
           
    

@app.route('/register', methods = ["GET", "POST"])
def register():
    if request.method  == "POST" and request.form["register"]=="register":    
        username = request.form["username"]
        password = request.form["password"]
        password=dbAccess.HashPasswd(password)
        ipBool = request.form.get("saveIp")
        print(ipBool)
        if check.IfEmpty(username) or check.IfEmpty(password):
            return render_template("register.html",error=True)
        else:
            if dbAccess.CheckUser(username)==True:
                if  ipBool=="on":   
                    ip=request.environ['REMOTE_ADDR']
                    dbAccess.registerIP(username, password,ip)
                    return redirect("/login")
                else:
                    dbAccess.register(username, password)
                    return redirect("/login")
            else:
                return render_template("register.html",error=True)
    else:return render_template("register.html")

@app.route('/dashboard/<number>', methods = ["GET", "POST"])
def dashboard(number):
    UserID=number
    if dbAccess.ValidID(UserID)==False:
        return redirect("/login")
    if request.method  == "POST":
        if request.form.get("btn")=="add" and request.form["besPolje"]!="":
            vnos = request.form["besPolje"]
            dbAccess.TaskAdd(vnos,UserID)
            return redirect(f"/dashboard/{UserID}")
    else:
        tasks = dbAccess.TaskGet(UserID)
    tasks = dbAccess.TaskGet(UserID)
    print(tasks)
    
    return render_template("dashboard.html",tasks=dbAccess.TaskList(tasks))


if __name__=="__main__":
    main()  