import os

# Obter diretório atual
dir_atual = os.path.dirname(os.path.abspath(__file__))



# Pedir nome e login do usuário
nome = input("Digite seu nome: ")
login = input("Digite seu login: ")

# Inicializar variáveis
saldo = 0
depositos_meses_consecutivos = 0

# Pedir depósitos até que o usuário pare de depositar
while True:
    deposito = input("Digite o valor do depósito (ou 'parar' para terminar): ")

    # Se o usuário digitou "parar", sair do loop
    if deposito == "parar":
        break

    # Converter o depósito em um número de ponto flutuante
    deposito = float(deposito)

    # Aplicar a taxa de depósito
    taxa = 0.01
    deposito -= deposito * taxa

    # Adicionar o depósito ao saldo
    saldo += deposito

    # Verificar se o usuário depositou nos últimos 3 meses
    if depositos_meses_consecutivos < 3:
        depositos_meses_consecutivos += 1
    else:
        # Se o usuário depositou nos últimos 3 meses, dar desconto
        desconto = 0.1
        saldo -= saldo * desconto
        depositos_meses_consecutivos = 0

    #printa o saldo atual no final do comando.    
    print ("Saldo atual é de: ", saldo)



# Salvar as informações do usuário em um arquivo dentro da pasta "contas"
contas = os.path.join(dir_atual, "contas")
if not os.path.exists(contas):
    os.makedirs(contas)
with open(f"{contas}/{login}.txt", "w") as arquivo:
    arquivo.write(f"Nome: {nome}\n")
    arquivo.write(f"Login: {login}\n")
    arquivo.write(f"Saldo: R${saldo:.2f}\n")
