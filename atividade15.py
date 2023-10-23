# Exercício Python 15: Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo. 
#DICA: PESQUISE E ENTENDA SOBRE DESIGUALDADE TRIANGULAR

lado1 = float(input("Digite o comprimento do primeiro lado do triângulo: "))
lado2 = float(input("Digite o comprimento do segundo lado do triângulo: "))
lado3 = float(input("Digite o comprimento do terceiro lado do triângulo: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("É possível formar um triângulo com esses comprimentos.")
else:
    print("Não é possível formar um triângulo com esses comprimentos.")