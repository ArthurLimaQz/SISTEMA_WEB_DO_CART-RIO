from flask import Flask, render_template, redirect, request, flash, session, url_for
from routes import *

#flask sqlalchemy

app = Flask(__name__)
app.secret_key = 'ARTHURQUEIROZ' #O Flask usa a secret_key para criptografar dados da sessão e garantir que ninguém consiga alterá-los do lado do cliente. Sem isso, recursos como flash, session e login não funcionam.

# Pegando a URL do PostgreSQL da variável de ambiente
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True) 
