reais = 5
dolares = reais / 5
print(f"R$ {reais:.2f} equivalem a US$ {dolares:.2f}")

def converter_para_dolar(valor_reais):
    return valor_reais / 5

valor_reais = float(input("Digite o valor em reais: "))
valor_dolares = converter_para_dolar(valor_reais)
print("Valor em dólares:", valor_dolares)