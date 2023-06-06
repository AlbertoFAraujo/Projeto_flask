from flask import Flask, render_template, url_for
from forms import FormLogin, FormCriarConta

app = Flask(__name__)
lista_usuarios = ['Alberto', 'Ferreira', 'Araujo']

app.config['SECRET_KEY'] = '3f95d5541d9e7e92bd647fc0fe750eba'


# Barra informa o caminho a ser rodado o def
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

@app.route('/login')
def login():
    form_login = FormLogin()
    form_criarConta = FormCriarConta()
    return render_template('login.html', lista_usuarios=lista_usuarios, form_login=form_login, form_criarConta=form_criarConta)


if __name__ == '__main__':
    app.run(debug=True)
