from random import randint

def get_price_list():
  index = 0
  precos = dict()
  lista = [3, 24, 98, 294, 735, 1617, 3234, 6000, 10510, 17500]
  for i in range(6, 16):
    precos[i] = lista[index]
    index += 1
  return precos

def mostrar_precos(dicionario):
  print("TABELA DE PREÇOS\n==========================\n")
  for i in dicionario:
    print("{0} dezenas: {1} RPs".format(i, dicionario[i]))
  print()

def mostrar_premios():
  index = 0
  premios = [2, 10, 50, 40000, 520000, 20000000]
  print("TABELA DE PRÊMIOS\n==========================\n")
  for i in range(1, 7):
    print("{} acertos: {} RPs".format(i, premios[index]))
    index += 1
  print()

def is_valid_attempt(tentativa, dezenas):
  if(len(tentativa)!=dezenas):
    print("Você fez uma aposta inválida!")
    return False
  else:
    for i in range(1, len(tentativa)):
      if(tentativa[0]==tentativa[i]):
        print("Aposta inválida! Há números iguais.")
        return False
  for i in tentativa:
    if(i>60 or i<1):
      print("Aposta inválida! Existem números inválidos.")
      return False
  return True

def generate_numbers():
  lista = []
  for i in range(0, 6):
    r = randint(1, 61)
    if(r not in lista):
      lista.append(r)
  return sorted(lista)

def get_hits(tentativa, sorteio):
  acertos = 0
  for i in tentativa:
    if i in sorteio:
      acertos += 1
  return acertos

def print_ticket(tentativa, sorteio, valor):
  print("==============================")
  print("Seu jogo: ", ' '.join(list(map(str, tentativa))))
  print("==============================")
  print("Sorteio: ", ' '.join(list(map(str, sorteio))))
  print("==============================")
  print("Total gasto: {} RPs".format(valor))
  print("==============================")