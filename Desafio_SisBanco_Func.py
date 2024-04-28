cadastro_clientes = []
contas = []
extrato = """============ Extrato ===========
"""


def saque(*,origem, valor):
    global extrato
    extrato_atual = extrato
    for conta in contas:
            if origem in conta.values():
                if conta["Limite_de_Saque"] > 0:                  
                    if conta["Saldo"] < 0:
                        print("Saldo insuficiente!\n")
                    elif conta["Saldo"] < valor:
                        print("Saldo Insuficiente\n")
                    else:
                        conta["Saldo"] -= valor
                        extrato_atual += f"Saque => -R${valor:.2f}\n"
                        conta["Limite_de_Saque"] -= 1
                        conta["Extrato"] += f"Saque => -R${valor:.2f}\n"
                        print("Saque no valor de:R${:.2f}, Realizado na conta:{}. Saldo final:R${:.2f}.".format(valor,conta["Conta"],conta["Saldo"]))
                        print(extrato_atual)
                        return
                else:
                    print("Limite de saques atingido\n")


def deposito(destino, valor):
    global extrato
    extrato_atual = extrato
    for conta in contas:
        if destino in conta.values():
            conta["Saldo"] += valor
            extrato_atual += f"Deposito => +R${valor:.2f}\n"
            conta["Extrato"] += f"Deposito => -R${valor:.2f}\n"
            print("Depósito no valor de:R${:.2f}, Realizado na conta:{}. Saldo final:R${:.2f}.".format(valor,conta["Conta"],conta["Saldo"]))
            print(extrato_atual)
            return
    

def cria_usuario(nome, cpf, data_nasc, endereco):
    usuario = [nome, cpf, data_nasc, endereco]
    for cadastro in cadastro_clientes:
            if cadastro[1] == cpf:
                print(f"O {cpf} já possui cadastro!")
                return
    cadastro_clientes.append(usuario)
    print("cadastro concluido") 
 

def cria_conta(titular, saldo, limite,lim_saq):
    ag = "0001"
    num =len(contas)+1
    num_conta ="{:06d}".format(num)
    # conta = [ag, num_conta, titular, saldo, limite]
    ext_conta = extrato
    conta = {"Agência":ag,"Conta":num_conta,"Titular":titular,"Saldo":saldo,"Limite":limite,"Limite_de_Saque":lim_saq,"Extrato":ext_conta}
    for cadastro in cadastro_clientes:
        if cadastro[1] == titular:
            contas.append(conta)
            print(f"conta {num_conta} criada.")
            return
    print("Cliente não cadastrado") 
    

def extrato_conta(numero):
    for conta in contas:
        if numero in conta.values():
            print(conta["Extrato"])
            return
    print("Conta não encontrada!")
        

# Testes das funções
# ==========================================
cria_usuario("João","000","00/00/000","Logradouro, 000 - Bairro_01 - Cidade/UF")
cria_usuario("Maria","111","00/00/000","Logradouro, 111 - Bairro_02 - Cidade/UF")
cria_conta("000",0,00,3)
cria_conta("111",0,00,3)
# ==========================================
deposito("000001",500)
deposito("000002",400)
saque(origem ="000001",valor= 150)
saque(valor= 50, origem ="000001")
saque(origem ="000001",valor= 50)
saque(origem ="000001",valor= 50)
saque(origem ="000002", valor= 900)
saque(valor= 50, origem ="000002")
# ===========================================
extrato_conta("000002")
extrato_conta("000001")
extrato_conta("000003")
# ===========================================
for cliente in cadastro_clientes:
    print(cliente)
for conta in contas:
    print(conta)
