# calculadora.py - Versão 2

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero"

print("Calculadora - Versão 2")
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

print("Soma:", somar(a, b))
print("Subtração:", subtrair(a, b))
print("Multiplicação:", multiplicar(a, b))
print("Divisão:", dividir(a, b))
