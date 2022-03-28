from flask import Flask, render_template, request
#from psutil import cpu_freq

app = Flask(__name__, template_folder='view')

@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html")

# @app.route("/index")
# def home():
#     return render_template("index.html")

@app.route("/login") #página de autenticação
def login():
    return render_template("login.html") 

@app.route("/autentica", methods=['POST']) #autenticação de parâmetros de login
def autentica():
    usr = request.form['usuario']
    pswrd = request.form['senha']
    #print ('Usuario: ' + usr + ' e senha: ' + pswrd) 
    # busca o usuario no banco de dados
    return render_template('usuario.html', usuario=usr, senha=pswrd)
    #return render_template("usuario.html") 

@app.route("/cadastra", methods=['POST']) #autenticação de parâmetros de login
def cadastra():
    nome = request.form['nome']
    cpf = request.form['cpf']
    email = request.form['email']
    usr = request.form['usuario']
    pswrd = request.form['senha']
    return render_template('usuario.html', nome=nome, cpf=cpf, email=email, usuario=usr, senha=pswrd)
    
@app.route("/signin") #página de criação de conta
def signin():
    return render_template("formCli.html") 

if __name__ == "__main__":
    app.run()