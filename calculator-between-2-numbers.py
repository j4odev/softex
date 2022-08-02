def soma():
    x = float(input("Valor 1: "))
    y = float(input("Valor 2: "))
    print("A soma dos valores é de: ", x+y)


def subtracao():
    x = float(input("Valor 1: "))
    y = float(input("Valor 2: "))
    print("A subtração dos valores é de: ", x-y)


def multiplicacao():
    x = float(input("Valor 1: "))
    y = float(input("Valor 2: "))
    print("A multiplicação dos valores é de: ", x*y)


def divisao():
    x = float(input("Valor 1: "))
    y = float(input("Valor 2: "))
    print("A divisão dos valores é de: ", x/y)


opcao = 1

while opcao:
    print("---------------------------------")
    print("0. SAIR")
    print("1. SOMA")
    print("2. SUBTRAÇÃO")
    print("3. MULTIPILICAÇÃO")
    print("4. DIVISÃO")
    print("---------------------------------")
    opcao = int(input("Selecione sua opção: "))
    print("---------------------------------")

    if(opcao == 1):
        soma()
    if(opcao == 2):
        subtracao()
    if(opcao == 3):
        multiplicacao()
    if(opcao == 4):
        divisao()
