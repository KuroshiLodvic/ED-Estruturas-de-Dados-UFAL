def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        mosca = lista[meio]
        if alvo == mosca:
           return meio
        elif alvo > mosca:
            inicio = meio + 1
        elif alvo < mosca:
            fim = meio - 1
    return -1

# print(busca_binaria([1, 3, 5, 6, 7, 8, 14, 25, 26, 33], 7)) 

def fatorial_iterativo(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

def fatorial_recursivo(numero):
    if numero == 0 or numero == 1:
        return 1
    
    else:
        return numero * fatorial_recursivo(numero - 1)

# numero = int(input())
# print(f"{numero}! = {fatorial_iterativo(numero)}")
# print(f"{numero}! = {fatorial_recursivo(numero)}")

def multiplicar(num1, num2):
    if num2 == 0:
        return 0
    else:
        return num1 + multiplicar(num1, num2 -1)
    
num1 = 4
num2 = 5
print(multiplicar(num1, num2))

def inverter(palavra):
    palavra = palavra[::-1]
    return palavra


palavra = "bipbop"
print(inverter(palavra))