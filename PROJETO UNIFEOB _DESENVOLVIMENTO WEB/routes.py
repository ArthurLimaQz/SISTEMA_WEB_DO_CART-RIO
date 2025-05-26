from main import app, render_template, redirect, request, flash



@app.route("/") #O @ no python é dado como decoration, no caso ele da uma funcionalidade para a linha que está a baixo! 
def home_login():
    return render_template("index.html")


@app.route('/submit', methods=['POST'])
def login(): 
       
    nome = request.form.get('login')
    senha = request.form.get('password')

    if nome == "arthur.queiroz" and senha == "123":
        return render_template("registro.html")
    else:
        flash('USUARIO INVALIDO')
        return redirect('/')
    

@app.route('/cadastro') #O @no python é dado como decoration, no caso ele da uma funcionalidade para a linha que está a baixo! 
def cadastro():
    nome = request.form.get('login')
    senha = request.form.get('password')
    return render_template('cadastro.html')

@app.route('/registro') #O @no python é dado como decoration, no caso ele da uma funcionalidade para a linha que está a baixo! 
def registro():
    return render_template('registro.html')