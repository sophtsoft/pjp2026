#Funcão
def saudar_personalizado(nome):
   print(f"Olá, {nome}! Bem-vindo à TechCoffee!")
   print("O que deseja pedir hoje?")
saudar_personalizado("Alice")

def saudar_personalizado(nome):
   print(f"Olá,{nome}! Seu café favorito já está sendo preparado.")

#chamando a função:
   saudar_personalizado("Maria")

  #somar
def soma(n1, n2):
  print(n1 + n2)

  #chamando somar
soma(5, 7)

  #subtrair
def subtrair(n1, n2):
  print(n1 - n2)

  #chamando subtrair
subtrair(10, 3)

  #multiplicar
def multiplicar(n1, n2):
  print(n1 * n2)

  #chamando multiplicar
multiplicar(4, 6)

  #dividir 
def dividir(n1, n2):
  if n2 != 0:
    print(n1 / n2)
  else:
    print("Erro: Divisão por zero não é permitida.")

  #chamando dividir
dividir(10, 2)

def calcular_total(quantidade, preco_unitario):
  total = quantidade * preco_unitario
  return total

#Guardando o resultado em uma variável
valor_da_venda = calcular_total(3,5.50)
print(f"O valor a pagar é: R${valor_da_venda}")