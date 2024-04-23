menu = f"""
Olá, Sr(a) cliente. Em que podemos lhe ajudar hoje? 

Digite a opção desejada: 

[1] Saque
[2] Depósito
[3] Extrato
[4] Sair
"""
saldo = 0
extrato = ""
limite_maximo_saque = 500
quantidade_saques = 0
LIMITE_SAQUE_DIARIO = 3

while True: 
    opcao = int(input(menu)) 
    if opcao == 1: 
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo 
        excedeu_quant_saques = quantidade_saques >= LIMITE_SAQUE_DIARIO 
        excedeu_max_saque = valor > limite_maximo_saque 

        if excedeu_saldo: 
            print("Saldo insuficiente para saque.")
        elif excedeu_quant_saques: 
            print("Você excedeu a quantidade de saques diários!")
        elif excedeu_max_saque: 
            print("VocÊ excedeu o limite máximo de saque!") 
        elif valor > 0:
            saldo -= valor 
            extrato += (f"Saque realizado no valor de: R${valor:.2f}\n")
            quantidade_saques += 1
        else: 
            print("Operação falhou! Tente novamente. ") 
    if opcao == 2: 
        valor = float(input("Informe o valor que deseja depositar: "))

        if valor > 0: 
            saldo += valor
            extrato += (f"Depósito realizado no valor de: R${valor:.2f}\n")
        else: 
            print("Operação falhou. Tente novamente!")
    if opcao == 3:
        print("================ EXTRATO ================\n=")
        print("\nNão foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("\n=== OBRIGADO POR UTILIZAR NOSSOS SERVIÇOS! ===")
    elif opcao == 4:
        break
    else:
        print("Operação inválida. Digite uma opção válida!!")
