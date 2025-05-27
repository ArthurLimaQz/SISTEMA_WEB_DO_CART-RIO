from main import app, render_template, redirect, request, flash, session, url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors
import bcrypt

#conexão com banco de dados
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456789'
app.config['MYSQL_DB']='unifeob' 
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql=MySQL(app)



@app.route('/') #O @ no python é dado como decoration, no caso ele da uma funcionalidade para a linha que está a baixo! 
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
    

@app.route('/cadastro', methods=['GET', 'POST']) #O @no python é dado como decoration, no caso ele da uma funcionalidade para a linha que está a baixo! 
def cadastro():
    
    if request.method == 'GET':
        return render_template('cadastro.html')
    else:
        registro = request.form['register']
        senha = request.form['password'].encode('utf-8')
        hash_password = bcrypt.hashpw(senha, bcrypt.gensalt())

        cur= mysql.connection.cursor()
        cur.execute("INSERT INTO cadastro (registro, senha) VALUES (%s, %s)", (registro, hash_password,))
        mysql.connection.commit()
        session['nome'] = registro
        session['senha'] = senha
        flash('CADASTRADO COM SUCESSO')
        return redirect(url_for('home_login')) 
    
   
@app.route('/registro') #O @no python é dado como decoration, no caso ele da uma funcionalidade para a linha que está a baixo! 
def registro():
    return render_template('registro.html')