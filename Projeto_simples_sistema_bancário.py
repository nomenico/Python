# Situação problema:

# Fomos contratados por um grande banco para desenvolver o seu novo sistema. 
# Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. 
# Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

# Operação de depósito:

# Deve ser possível depositar valores positivos para a minha conta bancária. 
# A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. 
# Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

# Operação de saque:

# O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. 
# Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. 
# Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

# Operação de extrato:

# Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta.
# Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
# 1500.45 -> R$ 1500.45

menu = """
================================================
            Seja bem-vindo ao nosso
            sistema bancário digital!

        MENU DE OPÇÕES
    
        [1] - Depositar
        [2] - Sacar
        [3] - Extrato
        [0] - Sair

        Digite a opção desejada.

================================================
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1" or opcao == "Depositar":
        valor = float(input("Informe o valor do depósito: R$ "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2" or opcao == "Sacar":
        valor = float(input("Informe o valor do saque: R$ "))
        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > limite:
            print("Operação falhou! O valor do saque excede o limite permitido.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques diários excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3" or opcao == "Extrato":
        print("\n================ EXTRATO ================")
        if extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("Limite de saques diários restantes:", LIMITE_SAQUES - numero_saques)
        print("=========================================")

    elif opcao == "0" or opcao == "Sair":
        print("Obrigado por utilizar nosso sistema bancário digital. Até logo!")
        break

    else:
        print("Operação inválida! Por favor, selecione uma opção válida.")