'''Faça um algoritmo que preencha um vetor de 8 elementos inteiros. Mostre os valores do vetor e informe:
Quantos números são maior que 30
    Somar estes números. 
Somar todos os números.
'''

def numeros_inteiros():
    numeros = []

    for i in range(8):
        num = float(input('Digite um numero: '))
        numeros.append(num)

    return numeros      

def maior_numeros(numeros):
    maior = 0

def soma_numeros_maiores_30(numeros):
    somar = 0

def soma(numeros):
    somar = sum(numeros)
    print(f'A soma dos números é {numeros} é {somar}')

def main():
    numeros = numeros_inteiros()
    maior_numeros(numeros)
    soma(numeros)

main()
