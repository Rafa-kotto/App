from utils import limpar
limpar()
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
##teste

print("qual menu deseja acessar -- 1 troca senha")
test = input("digite aqui : ")
if test == "1":
    limpar()
    print("para alterar sua senha insira seu usuario e senha atual")
    usuariodigitado = input("Seu usuario : ").strip()
    senhadigitada = input("Sua senha : ").strip()
    limpar()
    if usuariodigitado == nome and senhadigitada == senha:
        senhanova = input("Digite sua nova senha : ")
        senhanova == senha ##quero trocar essa parte para que a senha nova substitua a senha velha 
    else:
        print("Algo esta errado verifique o usuario e a senha") 
        print("ola")