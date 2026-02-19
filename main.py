from utils import limpar

nome = "a"
senha = "1"
limpar()
def tela_inicial():
    print ("Olá bem vindo ao meu App fit")
    print("Para primeiro acesso digite 1, caso já tenha um usuário digite 2")
    comeco = input("Digite aqui :") 
    if comeco == "1" : 
        limpar()
    print("Crie seu cadastro")
    nome = input("Seu nome : ").strip()
    senha = input("Sua senha : ").strip()
    email = input("Seu email : ").strip()
    if not nome or not senha or not email:
        print("Todos os campos são obrigatorios")
    else:
        print("Cadastrado com sucesso!")
        limpar()

tela_inicial()
def tela_senha():
    print("para alterar sua senha insira seu usuario e senha atual")
    usuariodigitado = input("Seu usuario : ").strip()
    senhadigitada = input("Sua senha : ").strip()
    limpar()
    if usuariodigitado == nome and senhadigitada == senha:
        senhanova = input("Digite sua nova senha : ")
    
        while senhanova == senha:
            print("Sua nova senha deve ser diferente da atual, tente novamente.")
            senhanova = input("Digite sua nova senha : ")
            ##mexi aqui, agora deu boa
        novasenha = senhanova 

    else:
        print("Algo esta errado verifique o usuario e a senha") 
    
    print(f"Senha atual agora é: {novasenha}")

##teste ok, funcionando*
def menu_principal():
    print("Qual menu você deseja acessar? 1 - trocar senha.")
    test = input("digite aqui : ")
    if test == "1":
        tela_senha()
menu_principal()
