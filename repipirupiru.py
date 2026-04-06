lista = [1,2,3,4,5,6,12,14,15,23,27,30,44]

def busca_bin_recursiva(lista:list, alvo, inicio = 0, fim = None):
    if fim == None:
        fim = len(lista) - 1

    if inicio > fim:
        return "Não encontrado"
    
    meio = (inicio + fim) // 2
    mosca = lista[meio]

    if alvo == mosca:
        return f"Encontrado na posição {meio}"

    elif alvo > mosca:
        return busca_bin_recursiva(lista, alvo, meio + 1, fim)
    
    else:
        return busca_bin_recursiva(lista, alvo, inicio, meio - 1)
    
def busca_bin(lista:list, alvo):

    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        mosca = lista[meio]

        if alvo == mosca:
            return f'Encontrado na posição {meio}'
        elif alvo > mosca:
            inicio = meio + 1
        elif alvo < mosca:
            fim = meio -1
    return 'Não encontrado'

def busca_sequencial(lista:list, alvo):
    for i in range(len(lista)):
        if alvo == lista[i]:
            return f'Encontrado na posição {i}'
    return 'Não encontrado'    
