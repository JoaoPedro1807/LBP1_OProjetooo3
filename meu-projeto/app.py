from flask import Flask, render_template, session, request, redirect, url_for
from controller import login, admin, carrinho
from model import sessoes, produto, users

app = Flask(__name__)
app.register_blueprint(login.c)
app.register_blueprint(admin.c)
app.register_blueprint(carrinho.c)
app.secret_key = 'senha super secreta'

@app.errorhandler(404)
def page_not_found(error):
    return 'Página não encontrada', 404

@app.errorhandler(401)
def acesso_negado(error):
    return 'Acesso negado!', 401

@app.before_request
def b4_request():
    if request.path not in ['/login', '/logout'] and not sessoes.existe('nome'):
        return redirect(url_for('login.login'))

@app.after_request
def a_request(response):
    print("Depois da requisição")
    return response

@app.route('/')
def index():
    carr = []
    for p in produto.Produtos:
        cookie = request.cookies.get(f'produto_{p.id}')
        if cookie:
            carr.append({
                'nome': p.nome,
                'qntd': cookie,
                'total': int(cookie) * p.preco
            })
    return render_template('index.html', nome=sessoes.get('nome'), produtos=produto.Produtos, carrinho=carr)

if __name__ == '__main__':
    app.run(debug=True)