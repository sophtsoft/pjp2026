negativos = 0

for i in range(10):
    numero = int(input("Digite um número: "))

    if numero < 0:
        negativos += 1

print("Quantidade de números negativos:", negativos)