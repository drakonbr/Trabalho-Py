
# criar um arquivo que verifica os usuario registrados e importar para este arquivo.
# depois subistituir onde solicita o nome do usuario para continuar
usuarios = ['Adriano',]

tabelas = {'Adriano':[],}


def main():
    print("\n=-=-= Sistema de Login =-=-=")
    print("1 - Login do Usuário")
    print("2 - Criar novo Usuário")
    print("0 - Encerar sistema")

    menuinicial = int(input("Digite sua opção: "))

    if menuinicial == 1:
        login_usuario()
    elif menuinicial == 2:
        novo_usuario() 
    elif menuinicial == 0:
        raise SystemExit
        # atexit.register(salvar_arquivo)
        #
            # Subistituir pelo comando que a professa encinal na sala
            # para o comando que salvar o arquivo antes de fechar o programa.
    else:
        print("Opção inválida, tente novamente.")
        main()


def login_usuario():
    print("\n=-=-=-=-= Sistema de Login =-=-=-=-=")
    nick= input("Nome de Usuário: ")

    if nick in usuarios:
        menu_cliente(nick)
    else:
        print("\n=-=-=-= Usuário não existe =-=-=-=")
        print("1 - Tentar novamente.")
        print("2 - Criar novo Usuário.")
        print("0 - voltar")      

        opcaoNaoExiste=int(input("\nDigite sua Opção: "))

        if opcaoNaoExiste == 1:
            login_usuario()
        elif opcaoNaoExiste == 2:
            novo_usuario() 
        elif opcaoNaoExiste == 0:
            main()
        else:
            print("Opção inválida.")
            print("Você sera redirecionado para o Menu inicial.")
            main()

def novo_usuario():
    print("\n=-=-=-=-= Novo Usuario =-=-=-=-=")
    novoNick= input("Nome de Usúario: ")

    if novoNick in usuarios:
        print("Este usúario ja existe, crie um Usuario novo.")
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

def criar_tabela(nick):
    print(f"\n=-=-=-= Nova Tavela =-=-=-=") 
    novaTabela= input("Nome da Tabela: ")
    
    #Verifica se o usuario existe na biblioteca
    #E verifica se existe uma tebala com mesmo nome para aquele usuário
    if nick in tabelas and novaTabela in tabelas[nick]:
        print(f"Você Ja tem uma tabela com nome {novaTabela}.\nTente novamente.")
        criar_tabela()
    else:
        #caso não tena a tabela, ele cria
        if nick in tabelas:
            tabelas[nick].append(novaTabela)
            # testar se esta criando assim
            #tabelas = { "andre": ["tabela1", "tabela2"]
            print("Nova Tabela criada com sucesso")
            menu_cliente()
        else:
            #caso não exista o usuario dentro do dicionario, ele cria o nome dele
            # e depois coloca a nova tabela dentro dele
            tabelas[nick] = [novaTabela]
            menu_cliente()
        #Testar de fica assim no final
        #tabelas = { "andre": ["tabela1", "tabela2"], "maria": ["tabela3", "tabela4"],}

def selecionar_tabela(nick):
    print(f"\n=-=-=-=-= Tabelas Registradas =-=-=-=-=")
    aTabela=str(input("Nome da Tabela: "))

    if aTabela in tabelas and nick in tabelas[aTabela]:
        with open('Arquivo.txt','w+') as arquivo:
            for editLinha in arquivo:
                #grava cada item em uma nova linha
                arquivo.write('%s\n' % editLinha)
                
    else:
        print(f"Tabala {aTabela} não existe. Tente novamente")
        menu_cliente()


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
        menu_cliente()

inicar = input("Digite 1: ")
if inicar != -999:
    main()
else:
    exit()