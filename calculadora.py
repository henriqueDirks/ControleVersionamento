# calculadora.py - Versão 3

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: Divisão por zero"

def menu():
    print("\nEscolha a operação:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")

print("Calculadora - Versão 3")

while True:
    menu()
    escolha = input("Operação: ")

    if escolha == '0':
        print("Encerrando a calculadora.")
        break

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print("Resultado:", somar(num1, num2))
        elif escolha == '2':
            print("Resultado:", subtrair(num1, num2))
        elif escolha == '3':
            print("Resultado:", multiplicar(num1, num2))
        elif escolha == '4':
            print("Resultado:", dividir(num1, num2))
        else:
            print("Operação inválida!")
    except ValueError:
        print("Erro: Entrada inválida. Digite números válidos.")
