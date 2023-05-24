import csv
import os
os.system("cls")

separador = "=-=" * 11

def main():
    while True:
        print(f"\n\033[34m{separador}\033[m")
        print("\tMenu Principal")
        print(f"\033[34m{separador}\033[m\n")
        
        print("1 - Login do Usuário")
        print("2 - Criar novo Usuário")
        print("0 - Encerar sistema\n")

        menuinicial = input("Digite sua opção: ")
        
        if menuinicial == '1':
            login_usuario()
        elif menuinicial == '2':
            novo_usuario() 
        elif menuinicial == '0':
            raise SystemExit
        elif menuinicial != '1' or menuinicial != '2' or menuinicial != '0':
            print("\033[31mOpção inválida.\033[m")
        else:
            print("\033[31mOpção inválida.\033[m")

def login_usuario():
    while True:

        print(f"\n\033[34m{separador}\033[m")
        print("\tSistema de Login")
        print(f"\033[34m{separador}\033[m\n")

        with open('Usuarios.csv', 'rt+') as docLogins:
            linhas = docLogins.readlines()

        nick = input("Seu o Login: ")

        for usuario in linhas:
            conta = usuario.strip().split(',')
            if conta[0] == nick:
                senha = input('Digite sua senha: ')
                if senha == conta[1]:
                    menu_cliente(nick)
                else:
                    print("Senha errada")
        else:
            print(f"\n\033[34m{separador}\033[m")
            print("\t\033[31mUsuário ou Senha errado.\033[m")
            print(f"\033[34m{separador}\033[m\n")
            print("1 - Tentar novamente.")
            print("2 - Criar novo Usuário.")
            print("0 - Voltar\n")

            opcaoNaoExiste = input("Digite sua Opção: ")

            if opcaoNaoExiste == '1':
                continue  # Reinicia o loop para tentar novamente
            elif opcaoNaoExiste == '2':
                novo_usuario()
            elif opcaoNaoExiste == '0':
                main()
            else:
                print("\033[31mOpção inválida.\033[m")

def novo_usuario():
    while True:
        print(f"\n\033[34m{separador}\033[m")
        print("\tNovo Usuario")
        print(f"\033[34m{separador}\033[m\n")

        novaConta = open('Usuarios.csv', 'rt+')
        texto = novaConta.read()
        lertexto = texto.split('\n')
        usuarios = [linha.split(',')[0] for linha in lertexto]
        #Verifica por linha, os usuarios existentes
        novoNick = input("Novo Usuário: ")
        #Caso seja encontrado algum usuario igual ele nao deixa criar
        if novoNick in usuarios:
            print("\033[31m Este usuário já existe. Tente criar outro nome.\033[m")
            novaConta.close()
        else:
            novaSenha = input("Senha: ")
            novaConta.write(f"{novoNick},{novaSenha}\n")
            print("Novo usuário criado com sucesso.\n")
            novaConta.close()
            main()

def menu_cliente(nick):
    while True:
        print(f"\n\033[34m{separador}\033[m")
        print(f"\tUsuario - \033[33m{nick}\033[m") 
        print(f"\033[34m{separador}\033[m\n")

        print("1 - Adicionar Despesa")
        print("2 - Editar Despesa")
        print("3 - Mostrar Despesas")
        print("0 - Sair do Usuario\n")

        menuCliente = input("Digite sua opção: ")

        if menuCliente == '1':
            print()
            criar_tabela(nick)
        elif menuCliente == '2':
            editar_despesa(nick)
        elif menuCliente == '3':
            mostrar_despesa(nick)
        elif menuCliente == '0':
            main()
        elif menuCliente != '1' or menuCliente != '2' or menuCliente != '0':
            print("\033[31mOpção inválida.\033[m")


def criar_tabela(nick):
    while True:
        print(f"\033[34m{separador}\033[m")
        print(f"\tNova Lista")
        print(f"\033[34m{separador}\033[m\n")

        listadoUsuario = f"Arquivos/{nick}.csv"
        #Listas.csv
        with open(listadoUsuario, 'a') as arquivo:
            categoria = input("Tipo de Despesa: ")
            valor = float(input("Valor: "))
            dia = input("Dia/Mês: ")

            arquivo.write(f"{nick},{categoria},{valor},{dia}\n")
            print("\nDespesa adicionada com sucesso!\n")
            arquivo.close()

            print("1 - Adicionar novamente")
            print("0 - Voltar\n")
            repetirAdd = input("Digite sua Opção: ")

            if repetirAdd == '1':
                print()
            elif repetirAdd == '0':
                menu_cliente(nick)
            else:
                print("\033[31mOpção inválida.\033[m")


def editar_despesa(nick):
    while True:
        print(f"\n\033[34m{separador}\033[m")
        print(f"\tEditar Despesas")
        print(f"\033[34m{separador}\033[m\n")

        listadoUsuario = f"Arquivos/{nick}.csv"
        with open(listadoUsuario, "r+") as docListas:
            linhas = docListas.readlines()

            print("\n\tCategoria\t|\tValor\t|\t Dia\n")

            for i, usuario in enumerate(linhas):
                conta = usuario.strip().split(',')
                if conta[0] == nick:
                    usuario = conta[0]
                    categoria = conta[1]
                    valor = conta[2]
                    dia = conta[3]

                    catFormatada = (f"{categoria}\t\tR$ {valor}\t\t {dia}")
                    print(f"{i + 1} - {catFormatada}")

            editarCat = int(input("\nNumero da Categoria: "))-1

            if editarCat >= 0 and editarCat < len(linhas):
                numeroLinha = linhas[editarCat]
                conta = numeroLinha.strip().split(',')

                print("1 - Alterar")
                print("2 - Deletar")
                print("0 - Voltar Menu\n")

                editartudo = input("Qual sua Opção: ")
                
                if editartudo == '1':

                    editaCategoria = input("Nome da categoria: ")
                    editarValor = input("Novo valor: ")
                    EditarDia = input("Qual dia: ")

                    conta[1] = editaCategoria
                    conta[2] = editarValor
                    conta[3] = EditarDia
                    linhas[editarCat] = ",".join(conta) + "\n"
                    # Atualiza a linha no arquivo
                    print("Linha atualizada com sucesso!")

                elif editartudo == '2':
                    del linhas[editarCat]
                    print("Linha deletada com sucesso!")

                elif editartudo == '0':
                    docListas.close()
                    menu_cliente(nick)

                elif editartudo != '1' or editartudo != '2' or editartudo != '0':
                    print("\033[31mOpção inválida.\033[m")
            else:
                editarCat = list(range(1, len(linhas) + 1))
                print("Erro nas Categorias. Número inválido!")
                print(f"Opções válidas: {editarCat}")
                input("Tentar Novamente (Enter)")

        # Sobrescrever o arquivo com as alterações
        with open(listadoUsuario, "w") as docListas:
            docListas.writelines(linhas) 

def mostrar_despesa(nick):
    print(f"\n\033[34m{separador}\033[m")
    print(f"\t Total Despesas")
    print(f"\033[34m{separador}\033[m\n")

    listadoUsuario = f"Arquivos/{nick}.csv"
    with open(listadoUsuario, "r+") as docListas:
        linhas = docListas.readlines()

        print("\n\tCategoria\t|\tValor\t|\t Dia\n")

        for i, usuario in enumerate(linhas):
            conta = usuario.strip().split(',')
            if conta[0] == nick:
                usuario = conta[0]
                categoria = conta[1]
                valor = conta[2]
                dia = conta[3]

                catFormatada = (f"{categoria}\t\tR$ {valor}\t\t {dia}")
                print(f"{i + 1} - {catFormatada}")
            
            print("\n1 - Voltar Menu")
            voltando = input("Sua opção: ")
            if voltando == '1':
                menu_cliente(nick)

            elif voltando != '1':
                print("\033[31mOpção inválida.\033[m")
        



while True:
    print(f"\033[34m{separador}\033[m\n")
    inicar = input("Aperte Enter: ")
    if inicar != "-999":
        main()
    else:
        print("Opção invalida")
