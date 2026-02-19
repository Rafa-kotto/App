import json
import os

ARQUIVO = "data.json"

class Usuario:
    def __init__(self, nome, senha, email, peso, altura):
        self.nome = nome
        self.senha = senha
        self.email = email
        self.peso = peso
        self.altura = altura
    def to_dict(self):
        """Transforma objeto em dicionário para JSON"""
        return {"nome": self.nome, "senha": self.senha, "email": self.email, "peso" : self.peso, "altura": self.altura}

def carregar_usuarios():
    """Carrega todos os usuários do JSON"""
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r") as f:
        dados = json.load(f)
    return dados.get("usuarios", [])

def salvar_usuario(usuario):
    """Adiciona um usuário no JSON"""
    usuarios = carregar_usuarios()
    usuarios.append(usuario.to_dict())
    with open(ARQUIVO, "w") as f:
        json.dump({"usuarios": usuarios}, f, indent=4)

def atualizar_senha(nome, nova_senha):
    """Atualiza a senha de um usuário"""
    usuarios = carregar_usuarios()
    encontrado = False
    for u in usuarios:
        if u["nome"] == nome:
            u["senha"] = nova_senha
            encontrado = True
            break
    if encontrado:
        with open(ARQUIVO, "w") as f:
            json.dump({"usuarios": usuarios}, f, indent=4)
    return encontrado
