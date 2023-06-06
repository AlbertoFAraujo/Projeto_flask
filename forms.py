from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField # Tipos de dados
from wtforms.validators import data_required, length, email, equal_to

class FormCriarConta(FlaskForm):
    username = StringField('Nome do Usuário', validators=[data_required()]) # datarequired é obrigação do campo
    email = StringField('E-mail', validators=[data_required(), email()])
    senha = PasswordField('Senha',validators=[data_required(), length(6, 20)]) # Tamanho de 6 a 20 caracteres
    confirmacao_senha = PasswordField('Confirmação de Senha', validators=[data_required(), equal_to('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')

class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[data_required(), email()])
    senha = PasswordField('Senha', validators=[data_required(), length(6, 20)])
    botao_submit_logi = SubmitField('Fazer Login') # Botão não preeche, não precisa de validators
