entrada = input("Digite o código do cupom: ")

def validar_cupom(codigo):

    if codigo == "CAFÉ10":
        return "0.10 (10%)"
    
    elif codigo == "PROMO5":
        return "0.05 (5%)"
    
    else:
        return "0.00 (0%)"
print(validar_cupom(entrada))