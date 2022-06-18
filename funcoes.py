from random import randint

# Função: obter a lista de preço dos jogos
# Retorno: dicionário com números de tentativas (chave) e preços (valor)
#
# Definição das variáveis utilizadas:
#
# index: variável de controle para auxiliar no preenchimento do dict
# prices: dicionário contendo o número de tentativas (chave) e seus preços (valor)
# prices_list: lista com os preços a serem adicionados no dict

def get_price_list():
  index = 0
  prices = dict()
  prices_list = [3, 24, 98, 294, 735, 1617, 3234, 6000, 10510, 17500]
  for i in range(6, 16):
    prices[i] = prices_list[index]
    index += 1
  return prices


# Função: exibir a lista de preços

def show_price_list(dicionario):
  print("TABELA DE PREÇOS\n==========================\n")
  for i in dicionario:
    print("{0} dezenas: {1} RPs".format(i, dicionario[i]))
  print()


# Função: exibir a lista de prêmios
#
# Definição das variáveis utilizadas:
#
# index: variável de controle
# prizes: lista de prêmios

def show_prize():
  index = 0
  prizes = [2, 10, 50, 40000, 520000, 20000000]
  print("TABELA DE PRÊMIOS\n==========================\n")
  for i in range(1, 7):
    print("{} acertos: {} RPs".format(i, prizes[index]))
    index += 1
  print()


# Função: verificar se a tentativa é válida ou não
# Retorno: True se for válida, False se não

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

# Função: gerar números aleatórios
# Retorno: lista ordenada de números aleatórios

def generate_numbers():
  lista = []
  for i in range(0, 6):
    r = randint(1, 61)
    if(r not in lista):
      lista.append(r)
  return sorted(lista)


# Função: verificar os acertos
# Retorno: inteiro referente ao número de acertos

def get_hits(tentativa, sorteio):
  acertos = 0
  for i in tentativa:
    if i in sorteio:
      acertos += 1
  return acertos


# Função: exibir resumo da jogada

def print_ticket(tentativa, sorteio, valor):
  print("==============================")
  print("Seu jogo: ", ' '.join(list(map(str, tentativa))))
  print("==============================")
  print("Sorteio: ", ' '.join(list(map(str, sorteio))))
  print("==============================")
  print("Total gasto: {} RPs".format(valor))
  print("==============================")