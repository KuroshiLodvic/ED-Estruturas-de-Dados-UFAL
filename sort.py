lista = [14,21,5,45,12,3,86,98,46,53,24,2,1,15,90,47]

def bubble_sort(lista:list):
    
    n = len(lista)

    for i in range(n):
        troca = False
        
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j+ 1] = lista[j+1], lista[j]
                troca = True
        
        if not troca:
            return lista

def selection_sort(lista:list):
    n = len(lista)

    for i in range(n):
        min_index = i

        for j in range(i+1, n):
            if lista[j] < lista[min_index]:
                min_index = j

        if (i != min_index):
            lista[i], lista[min_index] = lista[min_index], lista[i]

    return lista

def insertion_sort(lista:list):
    for i in range(1, len(lista)):
        chave = lista[i]

        j = i - 1

        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = chave

    return lista

def merge_sort(lista:list):
    if len(lista) > 1:

        meio = len(lista) // 2
        metade_esquerda = lista[:meio]
        metade_direita = lista[meio:]

        merge_sort(metade_esquerda)
        merge_sort(metade_direita)

        i = j = k = 0
        
        while i < len(metade_esquerda) and j < len(metade_direita):
            if metade_esquerda[i] < metade_direita[j]:
                lista[k] = metade_esquerda[i]
                i += 1
            else: 
                lista[k] = metade_direita[i]
                j += 1
            k += 1

        while i < len(metade_esquerda):
            lista[k] = metade_esquerda[i]
            i += 1
            k += 1

        while j < len(metade_direita):
            lista[k] = metade_direita[j]
            j += 1
            k += 1
        
    return lista
    
def quick_sort(lista:list):
    if len(lista) > 1:
        return lista
    
    else:
        pivot = lista[len(lista) // 2]
        esquerda = [x for x in lista if x < pivot]
        meio = [x for x in lista if x == pivot]
        direita = [x for x in lista if x > pivot]
        return quick_sort(esquerda) + meio + quick_sort(direita)
