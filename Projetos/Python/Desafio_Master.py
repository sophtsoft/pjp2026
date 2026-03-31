def calcular_item(preco, quantidade):
	return preco * quantidade

def gerar_pontos(valor):
	return int(valor * 10)

preco_cafe = float(input("Digite o valor do café: "))

valor_final = calcular_item(preco_cafe, 1)
pontos = gerar_pontos(valor_final)

print(f"Valor final: R$ {valor_final:.2f}")
print(f"Pontos ganhos: {pontos}")