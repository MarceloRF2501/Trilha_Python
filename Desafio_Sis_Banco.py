menu = """
====== OPCOES ======
D - Depositar
S - Sacar
E - Extrato
Q - Sair

"""

Saldo = 0
Limite = 500
Extrato = """============ Extrato ===========
"""
numero_saques = 0
LIMITE_SAQUES = 3
operacoes = 0

while True:
    opcao = input(menu)

    if opcao.upper() == "D":
        print("Deposito")
        valor_dep = int(input("Valor do depósito: "))
        if valor_dep > 0:
            Saldo = Saldo + valor_dep
            operacoes += 1
            Extrato += f"Deposito => +R${valor_dep:.2f}\n"
            print(f"Seu saldo é:R${Saldo:.2f}")
        else:
            print("O valor deve ser positivo")

    elif opcao.upper() == "S":
        print("Saque")
        valor_saq = int(input("Valor do saque: "))
        if valor_saq > 0:
            if numero_saques < LIMITE_SAQUES:
                if valor_saq > 500:
                    print(f"Valor limite para saque é R${Limite:.2F}")
                elif valor_saq > Saldo:
                    print("Saldo insuficiente")
                else:
                    Saldo = Saldo - valor_saq
                    Extrato += f"Saque => -R${valor_saq:.2f}\n"
                    operacoes += 1
                    numero_saques += 1
                    print(f"Seu saldo é R${Saldo:.2f}")
            else:
                print("Limite de saques atingido.")
        else:
            print("O valor deve ser positivo")

    elif opcao.upper() =="E":
            if operacoes > 0:
                print(Extrato)
                print(f"Saldo: R${Saldo:.2f}")
                input("Pressione ENTER para sair do extrato")
            else:
                print(Extrato)
                print("Não foram realizadas operações.")
                print(f"Saldo: R${Saldo:.2f}")
                input("Pressione ENTER para sair do extrato")

    elif opcao.upper() =="Q":
        break

    else:
        print("Operação invalida!")

    
