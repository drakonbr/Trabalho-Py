import os
os.system("cls")
# criar um arquivo que verifica os usuario registrados e importar para este arquivo.
# depois subistituir onde solicita o nome do usuario para continuar
usuarios = ["Adriano",]

# Criar também um arquivo que verifica as tabelas criadas de acordo com nome do usuario.
# e subistituir em (criar_tabela, selecionar_tabela, menu_tabela)
tabelas = {}

def main():
    print("\n=-=-= Sistema de Login =-=-=")
    print("1 - Login do Usuário")
    print("2 - Criar novo Usuário")
    print("0 - Encerar sistema")

    menuMain = int(input("Digite sua opção: "))

    if menuMain == 1:
        login_usuario()
    elif menuMain == 2:
        novo_usuario() 
    elif menuMain == 0:
        print('algo') 
            # Subistituir pelo comando que a professa encinal na sala
            # para o comando que salvar o arquivo antes de fechar o programa.
    else:
        print("Opção inválida, tente novamente.")
        main()

def login_usuario():
    print(f"\n=-=-=-=-= Sistema de Login =-=-=-=-=")

    nick=str(input("Nome de Usuário: "))

    if nick in usuarios:
        menu_cliente()
    else:
        print("\n=-=-=-= Usuário não existe =-=-=-=")
        print("1 - Tentar novamente.")
        print("2 - Criar novo Usuário.")
        print("0 - Encerar sistema")      

        opcaoNaoExiste=int(input("\nDigite sua Opção: "))

        if opcaoNaoExiste == 1:
            login_usuario()
        elif opcaoNaoExiste == 2:
            novo_usuario() 
        elif opcaoNaoExiste == 0:
            break 
            # Subistituir pelo comando que a professa encinal na sala
            # para o comando que salvar o arquivo antes de fechar o programa.
        else:
            print("Opção inválida.")
            print("Você sera redirecionado para o Menu inicial.")
            main()

def novo_usuario():
    print(f"\n=-=-=-=-= Novo Usuario =-=-=-=-=")

    novoNick=str(input("Nome de Usúario: "))

    if novoNick in usuarios:
        print("Este usúario ja existe, crie um novo Usuario.")
        novo_usuario()
    else:
        usuarios.append(novoNick)
        print("Novo usúario criado com sucesso. ")
        main()    

def menu_cliente(nick):
    print(f"\n=-=-= Usuario {nick} =-=-=") 
    print("1 - Criar tabela")
    print("2 - Selecionar tabela")
    print("3 - Deletar tabela")
    print("0 - Sair do Usuario")

    menuCliente = int(input("Digite sua opção: "))

    if menuCliente == 1:
        criar_tabela()
    elif menuCliente == 2:
        selecionar_tabela()
    elif menuCliente == 3:
        deletar_tabela()
    elif menuCliente == 0:
        main() 
    else:
        print("Opção inválida. Tente novamente.")

#PERGUNTAR A PROFESORA
def criar_tabela(nick):
    print(f"\n=-=-=-= Nova Tavela =-=-=-=") 
    novaTabela=str(input("Nome da Tabela: "))
    
    #Verifica se o usuario existe na biblioteca
    #E verifica se existe uma tebala com mesmo nome para aquele usuário
    if nick in tabelas and novaTabela in tabelas[nick]:
        print(f"Você Ja tem uma tabela com nome {novaTabela}.")
    else:
        #caso não tena a tabela, ele cria
        if nick in tabelas:
            tabelas[nick].append(novaTabela) 
            # não sei porque no (.append) não ta pegando, ja tentei varias maneiras
            # na parte de cima pegou normalmente
            print("Nova Tabela criada com sucesso")
        else:
            #caso não exista o usuario dentro do dicionario, ele cria o nome dele
            # e depois coloca a nova tabela dentro dele
            tabelas[nick] = [novaTabela]
            menu_cliente()
        #Testar de fica assim no final
        #tabelas = { "andre": ["tabela1", "tabela2"], "maria": ["tabela3", "tabela4"],}

def selecionar_tabela(nick):
    print(f"\n=-=-=-=-= Tabelas Registradas =-=-=-=-=")
    print(tabelas[nick])

    aTabela=str(input("Nome da Tabela: "))

    if aTabela in tabelas and nick in tabelas[aTabela]:
        print("algo")
        # ADICIONAR O COMANDO PARA  ABRIR A TABELA E E PODER ALTERAR ELA
    else:
        print(f"Tabala {aTabela} não existe. Tente novamente")
        selecionar_tabela()

#PERGUNTAR A PROFESORA
def deletar_tabela(nick):
    print(f"\n=-=-=-=-= Deletar tabelas =-=-=-=-=")
    print(tabelas[nick])

    deletarTabela=str(input("Nome da tabela: "))

    if deletarTabela in tabelas[nick]:
        tabelas[nick].remove(deletarTabela)
        print("Tabela deletada.")
        menu_cliente()
    else:
        print(f"Está tabela não existe, tente novamente.")
        deletar_tabela()