def calcular_item(preco_unitario, quantidade):
    subtotal = preco_unitario * quantidade
    imposto = subtotal * 0.05
    return subtotal + imposto
print(calcular_item(10, 2))