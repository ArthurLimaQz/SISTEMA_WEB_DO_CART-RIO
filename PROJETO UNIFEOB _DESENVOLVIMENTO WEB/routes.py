from main import app
from flask import render_template
from flask import redirect
from flask import request


@app.route("/") #O @ no python é dado como decoration, no caso ele da uma funcionalidade para a linha que está a baixo! 
def home_login():
    return render_template("index.html")


@app.route('/submit', methods=['POST'])
def login(): 
       
    nome = request.form.get('login')
    senha = request.form.get('password')

    if nome == "arthur.queiroz" and senha == "123":
        return render_template("registro.html")
    return redirect('/')

@app.route("/registro") #O @no python é dado como decoration, no caso ele da uma funcionalidade para a linha que está a baixo! 
def registro():
    return render_template("registro.html")