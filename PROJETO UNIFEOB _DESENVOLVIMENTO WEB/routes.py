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

    if nome == "admin" and senha == "admin":
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
    
   
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    cur = mysql.connection.cursor()

    if request.method == 'POST':
        # Dados do formulário
        livro = request.form['Livro']
        folha = request.form['Folha']
        termo = request.form['Termo']
        dt_rg = request.form['dt_rg']
        nome = request.form['Nome']
        pai = request.form['Pai']
        mae = request.form['Mae']
        dt_nascimento = request.form['dt_nascimento']

        # Inserir na tabela pessoa
        cur.execute("""
            INSERT INTO pessoa (nome, nome_genitor, nome_genitora, data_nascimento, sexo)
            VALUES (%s, %s, %s, %s, %s)
        """, (nome, pai, mae, dt_nascimento, "M"))
        mysql.connection.commit()

        pessoa_id = cur.lastrowid

        # Inserir na tabela registro
        cur.execute("""
            INSERT INTO registro (livro, folha, termo, data_registro, id_pessoa)
            VALUES (%s, %s, %s, %s, %s)
        """, (livro, folha, termo, dt_rg, pessoa_id))
        mysql.connection.commit()

        # Buscar o registro recém inserido
        cur.execute("""
            SELECT r.livro, r.folha, r.termo, r.data_registro, p.nome 
            FROM registro r 
            JOIN pessoa p ON r.id_pessoa = p.id
            WHERE r.id_pessoa = %s
            ORDER BY r.id DESC LIMIT 1
        """, (pessoa_id,))
        ultimo_registro = cur.fetchone()

        flash('CADASTRADO COM SUCESSO')
        return render_template('registro.html', registros=[ultimo_registro])

    # Se for GET, não exibe nada
    return render_template('registro.html', registros=[])



