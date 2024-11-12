# Função para ler 10 valores distintos
def ler_valores():
    valores = []
    for i in range(10):
        valor = int(input(f'Digite o valor {i+1}: '))
        while valor in valores:  # Garante que o valor seja único
            print("Valor repetido! Digite outro valor.")
            valor = int(input(f'Digite o valor {i+1}: '))
        valores.append(valor)
    return valores

# Função para verificar e exibir quantos valores são maiores que 100
def verificar_maiores_que_100(numeros):
    maiores_que_100 = [num for num in numeros if num > 100]
    print(f'\nQuantos valores são maiores que 100: {len(maiores_que_100)}')
    print(f'Valores maiores que 100: {maiores_que_100}')

# Função principal que chama as outras funções
def main():
    numeros = ler_valores()
    verificar_maiores_que_100(numeros)

# Chama a função principal
main()
