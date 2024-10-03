from flask import Flask, render_template, request, make_response, redirect, url_for
from config import Config
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

#Modelos
from models.ModelUser import ModelUser

# Entities

from models.entities.usuario import User

       


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method =='POST':
        user = User(request.form['username'], request.form['password'])
        logged_user =  ModelUser.login(db,user)
        if logged_user != None:
            return redirect(url_for('index'))
        else:
            print("no existes")
        #print(request.form['username'])
        return render_template("auth/login.html")
    else:
        return render_template("auth/login.html")
    

@app.route('/registro', methods=['GET','POST'])
def registro():
    if request.method == 'POST':
        user = User(request.form['nombre'], request.form['password'])
        registro_usuario = ModelUser.RegistroUsuario(db,user)
        if registro_usuario != None:
            return redirect(url_for("index"))
        else:
            print("no existes")
        #print(request.form['username'])
        return render_template("auth/login.html")
    else:
        return render_template("registro.html")


#enrutador
@app.route('/')
def holamundo():
    ip_usuario = request.remote_addr
    response = make_response(redirect('/index'))
    response.set_cookie("usuario", ip_usuario)
    return response

@app.route('/index')
def index():
    ip_user = request.cookies.get("usuario")
    return render_template("index.html", ip_user = ip_user)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/usuario')
def ipUser():
    ip_usuario = request.remote_addr
    return f"Su usuario es {ip_usuario}"

if __name__=='__main__':
    
    app.run(host='0.0.0.0', port = '8080')


