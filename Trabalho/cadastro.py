import os
os.system("cls")
dic ={'nome':'a','login':'b'}

#cadastro usando dicionario fica errado
def cadastro():
    arquivo = open("c:/Users/filip/Documents/Faculdade Cesar School/1º PERIODO/Programação/1 PROJETO/Trabalho-Py/Trabalho/contas/loginscadastro.txt","w")
    #ou (testa ai pls): arquivo = open("Trabalho-Py/Trabalho/contas/login.txt")
    #'nome': input(),'login': input() 
    arquivo.write(f"{'nome'},{'login'}")
    dic.get['nome']
    dic.get['login']
    arquivo.close()


#arquivo = open("Trabalho-Py/Trabalho/contas/login.txt")
#nenhuma função funciona
def login():
    arquivo = open("c:/Users/filip/Documents/Faculdade Cesar School/1º PERIODO/Programação/1 PROJETO/Trabalho-Py/Trabalho/contas/loginscadastro.txt","r")
    dic.get('nome')
    dic.get('login')
    
    if dic.get('nome') == True and dic.get('login') == True:
        print("Login aceito")
    else:
        print("Nome ou Login errados.")
        return False
    arquivo.close()

#loop para o usuário escolher a ação (o botão de sair funciona)
while True:
    print("0 - Cadastro")
    print("1 - Login")
    print("2 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 0:
        cadastro()
    elif opcao == 1:
        login()
    elif opcao == 2:
        break
    else:
        print("opcao invalida")

