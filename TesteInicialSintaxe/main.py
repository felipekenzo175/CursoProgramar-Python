# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

nome = input("Qual é o seu nome? ")
print(nome)
print(len(nome))

if nome == "Felipe":
    print(f"Olá, {nome}")
    estado = input("Como você está? ")
    if estado == "Bem":
        print("Que bom")
    else:
        print("Vai melhorar")
    tempo = input("E o tempo? ")
    if tempo == "Sol":
        print("Maravilha")
    else:
        print("Vai melhorar")

sobrenome = input("Qual é o seu sobrenome? ")
if sobrenome == "Kenzo":
    print("Olá, Kenzo")
elif sobrenome == "Ojima":
    print("Olá, Ojima")
else:
    print("Desculpe, não o conheço")

idade = input("Quantos anos vc tem? ")
print(idade)
print(type(idade))

idadeFutura = int(idade) + 10
print(idadeFutura)
print(type(idadeFutura))

for ano in idade:
    print(ano)

numero = int(input("Digite um número "))

quadrado = numero ** 2
print(f"O quadrado desse número é {quadrado}")

raiz = math.sqrt(quadrado)
print(f"A raíz do quadrado desse número é {raiz}")

pi = math.pi
print(f"O número pi vale {pi}")

opcao = ""
while opcao != 9:
    print("1 - login")
    print("2 - cadastro")
    print("3 - consulta")
    print("4 - inserção")
    print("5 - exclusão")
    print("9 - sair")
    opcao = int(input("Escolha uma opção => "))
