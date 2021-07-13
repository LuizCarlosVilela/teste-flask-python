from flask import Flask, render_template
import datetime

TEMPLATES = './templates'
STATIC = './static'

app = Flask(__name__, template_folder=TEMPLATES, static_folder=STATIC)


@app.route('/')
def home():
    data = datetime.datetime.now()
    usuarios = ['Luiz', 'Amós', 'Arthur']
    mostrarUsuarios = True
    return render_template('home.html', dataAtual=data, usuarios=usuarios, mostrarUsuarios=mostrarUsuarios)