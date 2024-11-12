# Função para inserir um item no vetor
def inserir_item(vetor):
    item = int(input('Digite o item a ser inserido: '))  
    vetor.append(item)  
    print(f'Item {item} inserido.')  # Confirma a inserção

# Função para retirar um item do vetor
def retirar_item(vetor):
    if vetor:  
        item = int(input('Digite o item a ser retirado: '))  
        if item in vetor:  
            vetor.remove(item)  
            print(f'Item {item} retirado.') 
        else:
            print(f'O item {item} não existe no vetor.')  
    else:
        print('Vetor está vazio.') 

# Função para listar os itens do vetor
def listar_itens(vetor):
    if vetor:  
        print(f'Itens no vetor: {vetor}')  
    else:
        print('Vetor está vazio.')  

# Função para retirar todos os itens do vetor
def retirar_todos_itens(vetor):
    vetor.clear() 
    print('Todos os itens foram retirados.') 

# Função principal que exibe o menu e chama as funções conforme a opção
def main():
    vetor = []  
    while True:  
        print('\nMenu:')  
        print('1 - Inserir item')
        print('2 - Retirar item')
        print('3 - Listar itens')
        print('4 - Retirar todos os itens')
        print('5 - Sair')
        
        opcao = int(input('Escolha uma opção: '))  
        
        if opcao == 1:
            inserir_item(vetor)  
        elif opcao == 2:
            retirar_item(vetor)  
        elif opcao == 3:
            listar_itens(vetor)  
        elif opcao == 4:
            retirar_todos_itens(vetor)  
        elif opcao == 5:
            print('Saindo...')  
            break  
        else:
            print('Opção inválida, tente novamente.')  

# Chama a função principal
main()
