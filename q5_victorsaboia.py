from flask import Flask, request, render_template
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import os

##FOI ESCOLHIDO A QUESTÃO 1 ONDE EU TENHO UMA LISTA DE USUARIOS COM SENHA E AUTENTICO , ENTÃO TROUXE ESSA IMPLEMENTAÇÃO
##E ADAPTEI PARA A REALIDADE DO SERVIDOR COM ENCRIPTOGRAFIA




app = Flask(__name__, template_folder='templates_folder')

# Gerar chave e IV para AES
key = os.urandom(16)  # Em produção, isso deve ser armazenado e recuperado com segurança
iv = os.urandom(16)

# Lambdas para criptografia e verificação de senha
encrypt_password = lambda password: AES.new(key, AES.MODE_CBC, iv).encrypt(pad(password.encode(), AES.block_size))
decrypt_password = lambda stored_password: unpad(AES.new(key, AES.MODE_CBC, iv).decrypt(stored_password), AES.block_size)

# Armazenando as senhas de usuários de forma segura como uma função lambda
users = lambda: {
    "marcos": encrypt_password('atlantico1'),
    "luiza": encrypt_password('victor34'),
    "roberto": encrypt_password('rob345')
}

# Mensagens como expressões lambda
welcome = lambda username: f'WELCOME {username}!!!'
wrong = lambda: 'WRONG PASSWORD!!!'
invalid = lambda: 'User does not exist!'

# Verificação de senha e existência do usuário
check_password = lambda username, input_password: welcome(username) if username in users() and decrypt_password(users()[username]).decode() == input_password else wrong()
check_if_user_exists = lambda username, input_password: check_password(username, input_password) if username in users() else invalid()

# Resposta da requisição como expressão lambda
reqresp = lambda: check_if_user_exists(request.form['username'], request.form['password']) if request.method == 'POST' else render_template('index.html')

# Adicionar regra de URL e executar o aplicativo
app.add_url_rule('/index/', 'index', reqresp, methods=['GET', 'POST'])
app.run(host='0.0.0.0', port=8081)
