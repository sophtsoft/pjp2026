while True:
    print("\nMENU DE OPERAÇÕES")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
        print("Resultado da soma:", a + b)

    elif opcao == 2:
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
        print("Resultado da subtração:", a - b)

    elif opcao == 3:
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida!")
