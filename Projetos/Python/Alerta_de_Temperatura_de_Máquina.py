def verificar_caldeira(temp_atual):
    if temp_atual < 90:
        return "Aquecendo..."
    
    elif 90 <= temp_atual <= 100:
        return "Pronto para uso."
    
    elif temp_atual > 100:
        return "Alerta: PERIGO: SUPERAQUECIMENTO."
print(verificar_caldeira(98))