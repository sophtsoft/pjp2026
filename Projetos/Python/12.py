numero = int(input("Digite um número: "))
maior = numero
menor = numero

for i in range(14):
    numero = int(input("Digite um número: "))

    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print("Maior valor:", maior)
print("Menor valor:", menor)