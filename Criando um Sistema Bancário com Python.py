menu = """

[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

"""

saldo = 0
limite_saque_valor = 500
extrato = ""
limite_saque_tentativas = 3

while True:

    opcao =input(menu)

    if opcao =="D" or opcao =="d":

        print("Qual valor deseja depositar?")
        valor = float(input(""))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Valor a ser depositador inválido")
            print("Favor inserir valor maior que R$0.00")

    elif opcao =="S" or opcao =="s":

        print("Qual valor deseja sacar?")
        valor = float(input(""))
        
        if limite_saque_tentativas <= 0:
             print("Limite de saques diários atingidos.")

        elif limite_saque_valor > 500:
             print("Limite máximo de R$500.00 por saque excedido.")

        elif valor > saldo:
             Print("Saldo insuficiente para saque.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:    R$ {valor:.2f}\n"
            limite_saque_tentativas -= 1
            
        else:
            print("Valor a ser sacado inválido")
            print("Favor inserir valor maior que R$0.00")

    elif opcao =="E" or opcao =="e":
         print("\n-------------------EXTRATO-------------------\n")
         print("Não foram realizadas movimentações na conta.\n" if not extrato else extrato)
         print("-----------------------------------------------\n")
         print(f"Saldo da conta: R$ {saldo:.2f}\n ")
         print("-----------------------------------------------\n")

    elif opcao =="Q" or opcao =="q":
        break

    else:
        print("Escolha uma opção válida do MENU!")
