# Importa a biblioteca necessária
from sys import argv

# Procedimento que aplica a ordenação pelo método bubble sort
def ordena_pela_bolha(vetor):
    tamanho = len(vetor)
    for i in range(tamanho):
        for j in range(0, tamanho):
            chave = vetor[j]
            if j != tamanho - 1:
                if chave > vetor[j+1]:
                    temp = vetor[j]
                    vetor[j] = vetor[j+1]
                    vetor[j+1] = temp                     

# Procedimento que aplica a ordenação pelo método selection sort
def ordena_pela_selecao(vetor):
    tamanho = len(vetor)
    for i in range(tamanho-1, 0, -1):
        index = 0
        for j in range(1, i+1):
            if vetor[j] > vetor[index]:
                index = j
        temp = vetor[i]
        vetor[i] = vetor[index]
        vetor[index] = temp

# Procedimento que aplica a ordenação pelo método insertion sort
def ordena_pela_insercao(vetor):
    tamanho = len(vetor)
    index = 0
    for i in range(0, tamanho):
        for j in range(i+1, tamanho):
            if vetor[j] < vetor[i] and vetor[j] < vetor[index]:
                temp = vetor[j]
                vetor[j] = vetor[i]
                vetor[index] = temp
            else:
                if vetor[j] < vetor[i] and vetor[j] > vetor[index]:
                    temp = vetor[i]
                    vetor[i] = vetor[j]
                    vetor[j] = temp

# Função que possibilita ao usuário ordenar um vetor de sua escolha usando algum dos métodos elementares
def main():
    vetor = []
    try:
        metodo_de_ordenacao = argv[1]
        sequencia = argv[2]
        numeros = sequencia.split(',')
        for numero in numeros:
            vetor.append(int(numero))      
        if metodo_de_ordenacao == '-b':
            ordena_pela_bolha(vetor)
        elif metodo_de_ordenacao == '-s':
            ordena_pela_selecao(vetor)           
        elif metodo_de_ordenacao == '-i':
            ordena_pela_insercao(vetor)
        else:
            return 'Método de ordenação inválido!' 
        return vetor   
    except:
        return 'Método de ordenação ou sequência passada inválida.'


ordenacao = main()
print(ordenacao)
