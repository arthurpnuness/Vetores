# Função para ler 10 valores distintos
def ler_valores():
    valores = []  
    for i in range(10): 
        valor = int(input(f'Digite o valor {i+1}: '))
        while valor in valores:  
            print('Valor repetido! Digite outro valor.')  
            valor = int(input(f'Digite o valor {i+1}: '))
        valores.append(valor)  
    return valores  

# Função para exibir os valores pares e suas posições no vetor
def exibir_pares_e_posicoes(numeros):
    for i in range(len(numeros)):  
        num = numeros[i] 
        if num % 2 == 0:  
            print(f'O número {num} é par e está na posição {i}') 

# Função principal que chama as outras funções
def main():
    numeros = ler_valores() 
    exibir_pares_e_posicoes(numeros)  

# Chama a função principal 
main()
