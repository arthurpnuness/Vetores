# Função para ler 10 valores distintos
def ler_valores():
    valores = []  
    for i in range(10):  
        valor = int(input(f'Digite o valor {i+1}: '))
        while valor in valores:  
            print("Valor repetido! Digite outro valor.")  
            valor = int(input(f'Digite o valor {i+1}: '))
        valores.append(valor)  
    return valores  

# Função para criar o vetor B com os valores do vetor A na ordem contrária
def criar_vetor_b(numeros):
    vetor_b = numeros[::-1]  # Cria o vetor B invertendo a ordem do vetor A
    print(f'Vetor A: {numeros}')  
    print(f'Vetor B (invertido): {vetor_b}')  

# Função principal que chama as outras funções
def main():
    numeros = ler_valores()  
    criar_vetor_b(numeros)  

# Chama a função principal
main()
