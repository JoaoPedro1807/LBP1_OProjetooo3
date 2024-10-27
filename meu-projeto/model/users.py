class User:
    def __init__(self, nome, senha, tipo):
        self.nome = nome
        self.senha = senha
        self.tipo = tipo

Users = [
    User("Adm", '7081', 'admin'),
    User("Joao", '1807', 'padrao')
]