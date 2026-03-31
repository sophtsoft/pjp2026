soma = 0
contador = 0

while True:
    idade = int(input("Digite a idade (0 para sair): "))
    if idade == 0:
        break

    soma += idade
    contador += 1

if contador > 0:
    print("Média das idades:", soma / contador)
else:
    print("Nenhuma idade informada")