menu = """"
    ============== Bem-vindo ao seu sistema bancário =================

    Selecione a operação que deseja efetuar

    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [0] - Sair


    =============== Obrigado por ser nosso cliente! ===================

"""

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_SAQUES = 3
movimentacao = 0

while True:

    opcao = input(menu)

    if opcao == "1":
        valor_deposito = float(input("Digite a quantia que deseja depositar: R$ "))
        saldo = float(saldo) + valor_deposito
        print(f"""
        Valor depositado com sucesso!

        Seu saldo atual é de: R$ {saldo:.2f}
        """)
        movimentacao = movimentacao + 1
        extrato = extrato + f" {movimentacao} - DEPÓSITO efetuado no valor de R$ {valor_deposito:.2f}\n"

    
    elif opcao == "2":
        valor_saque = float(input("Digite a quantia que deseja sacar: R$ "))

        if (saldo >= valor_saque and valor_saque <= limite) and numero_de_saques < LIMITE_SAQUES:
            saldo = saldo - valor_saque
            print(f"""
            Valor sacado com sucesso!
        
            Seu saldo atual é de: R$ {saldo:.2f}
            """)

            numero_de_saques = numero_de_saques + 1

            movimentacao = movimentacao + 1

            extrato = extrato + f" {movimentacao} - SAQUE efeuado no valor de R$ {valor_saque:.2f}\n"

        elif saldo < valor_saque:
            print("Saldo insuficiente, recomeçe a sua solicitação.")

        elif valor_saque > limite:
            print("Solicitação maior que o limite permitido, recomeçe a sua solicitação.")

        else:
            print("Você atingiu a quantidade máxima de saques permitidas hoje, volte no próximo dia útil.")

    
    elif opcao == "3":
        print(f""" 
            
        
=============== Extrato ==================

{extrato}

    
        """)
    
    elif opcao == "0":
        print("Obrigado por ser nosso cliente, tenha um ótimo dia!")
        break

    else:
        print("Opção inválida! Tente novamente.")