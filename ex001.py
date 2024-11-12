'''Faça um algoritmo que preencha um vetor de 8 elementos inteiros. Mostre os valores do vetor e informe:
Quantos números são maior que 30
    Somar estes números. 
Somar todos os números.
'''

def numeros_inteiros():
    # Preenche um vetor de 8 números inteiros
    numeros = []
    for i in range(8):
        num = int(input('Digite um numero: '))
        numeros.append(num)
    return numeros       

def maior(numeros):
    # Encontra o maior número do vetor
    maior_numero = numeros[0]  # Inicializa o maior número com o primeiro elemento
    for num in numeros:
        if num > maior_numero:
            maior_numero = num  # Atualiza 'maior_numero' se encontrar um número maior
    return maior_numero

def maiores30(numeros):
    # Conta e soma os números maiores que 30
    contador = 0
    soma_maiores = 0
    for num in numeros:
        if num > 30:
            contador += 1
            soma_maiores += num
    return contador, soma_maiores

def soma(numeros):
    # Soma todos os números do vetor
    soma_num = 0
    for i in numeros:
        soma_num += i  # Adiciona o número à soma
    return soma_num 

def main():
    # Chama a função para preencher o vetor
    numeros_int = numeros_inteiros()
    print(f'Valores do vetor: {numeros_int}')

    # Chama a função para encontrar o maior número
    maior_num = maior(numeros_int)
    print(f'O maior número do vetor é: {maior_num}')

    # Chama a função para contar e somar os números maiores que 30
    contador, soma_maiores_que_30 = maiores30(numeros_int)
    print(f'Quantidade de números maiores que 30: {contador}')
    print(f'Soma dos números maiores que 30: {soma_maiores_que_30}')

    # Chama a função para somar todos os números
    soma_total = soma(numeros_int)
    print(f'Soma de todos os números do vetor: {soma_total}')

# Chama a função principal
main()
