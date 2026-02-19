from utils import limpar
from models import Usuario, salvar_usuario, carregar_usuarios, atualizar_senha

# ===== FUNÇÕES =====   

def tela_inicial():
    limpar()
    print("=== BEM VINDO AO APP FIT ===")
    print("1 - Criar conta")
    print("2 - Login")
    print("0 - Sair")
    opcao = input("Digite aqui: ").strip()
    return opcao

def cadastro():
    limpar()
    print("=== CADASTRO ===")
    nome = input("Seu nome: ").strip()
    senha = input("Sua senha: ").strip()
    email = input("Seu email: ").strip()
    peso = input("Seu peso : ").strip()
    altura = input("Sua altura : ").strip()

    if not nome or not senha or not email or not peso or not altura:
        print("Todos os campos são obrigatórios!")
        input("Pressione ENTER para voltar ao menu")
        return

    # Verifica se email já existe
    usuarios = carregar_usuarios()
    for u in usuarios:
        if u["email"] == email:
            print("Email já cadastrado!")
            input("Pressione ENTER para voltar ao menu")
            return

    usuario = Usuario(nome, senha, email, peso, altura)
    salvar_usuario(usuario)
    print("Cadastro realizado com sucesso!")
    input("Pressione ENTER para voltar ao menu")

def login():
    limpar()
    print("=== LOGIN ===")
    nome = input("Seu nome: ").strip()
    senha = input("Sua senha: ").strip()

    usuarios = carregar_usuarios()
    for u in usuarios:
        if u["nome"] == nome and u["senha"] == senha:
            print(f"Bem-vindo {nome}!")
            input("Pressione ENTER para voltar ao menu")
            return nome  # retorna o usuário logado
    print("Usuário ou senha incorretos!")
    input("Pressione ENTER para voltar ao menu")
    return None

def trocar_senha(usuario_logado):
    limpar()
    print("=== TROCAR SENHA ===")
    senha_atual = input("Digite sua senha atual: ").strip()
    usuarios = carregar_usuarios()
    for u in usuarios:
        if u["nome"] == usuario_logado and u["senha"] == senha_atual:
            nova_senha = input("Digite sua nova senha: ").strip()
            while nova_senha == senha_atual:
                print("Nova senha deve ser diferente da atual!")
                nova_senha = input("Digite sua nova senha: ").strip()
            atualizar_senha(usuario_logado, nova_senha)
            print("Senha atualizada com sucesso!")
            input("Pressione ENTER para voltar ao menu")
            return
    print("Senha incorreta!")
    input("Pressione ENTER para voltar ao menu")
    
    
def alterar_informações(usuario):
    limpar()
    usuarios = carregar_usuarios()
    dados_usuario = None
    for u in usuarios:
        if u["nome"] == usuario:
            dados_usuario = u
            break

    if not dados_usuario:
        print("Usuario não encontrado")
        print("Precione ENTER para tentar novamente")
    print(f"Seu peso atual é :{dados_usuario.get('peso', 'nao informado')} KG")
    print(f"Sua altura atual é :{dados_usuario.get('altura', 'nao informado')}Metros")
    troca = input("Deseja ainda alterar as informações ? (y/n)")
    if troca == "y":
            novopeso = input("Seu novo peso = ")
            novaaltura= input("Sua nova altura = ")
    elif troca == "n":
            print("Voltando ao menu principal...")
            return
    else:
            print("Valor invalido digitado")

# ===== LOOP PRINCIPAL =====
usuario_logado = None
while True:
    opcao = tela_inicial()

    if opcao == "1":
        cadastro()
    elif opcao == "2":
        usuario_logado = login()
        if usuario_logado:
            while True:
                limpar()
                print("=== MENU USUÁRIO ===")
                print("0 - Logout")
                print("1 - Trocar senha")
                print("2 - Alterar configurações do perfil")
                escolha = input("Digite aqui: ").strip()
                if escolha == "1":
                    trocar_senha(usuario_logado)

                elif escolha == "2":
                    alterar_informações(usuario_logado)
                elif escolha == "0":
                    usuario_logado = None
                    break
                else:
                    print("Opção inválida!")
                    input("Pressione ENTER para voltar ao menu")
    elif opcao == "0":
        print("Saindo do App Fit...")
        break
    else:
        print("Opção inválida!")
        input("Pressione ENTER para voltar ao menu")
