from flask import Flask, render_template, redirect, request, flash

#flask sqlalchemy

app = Flask(__name__)
app.secret_key = 'ARTHURQUEIROZ' #O Flask usa a secret_key para criptografar dados da sessão e garantir que ninguém consiga alterá-los do lado do cliente. Sem isso, recursos como flash, session e login não funcionam.

from routes import *

if __name__ == "__main__":
    app.run(debug=True) 