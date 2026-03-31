soma_pares = 0
soma_impares = 0

for i in range(10):
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        soma_pares += numero
    else:
        soma_impares += numero

print("Soma dos pares:", soma_pares)
print("Soma dos ímpares:", soma_impares)