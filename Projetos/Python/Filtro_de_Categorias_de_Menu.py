def definir_categoria(codigo_produto):
    if codigo_produto.startswith("BEB"):
        return "Bebida Quente"
    elif codigo_produto.startswith("COM"):
        return "Comida/Salgado"
print(definir_categoria("BEB001"))