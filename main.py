import funcoes

funcoes.mostrar_precos(funcoes.get_price_list())
funcoes.mostrar_premios()

recurso = int(open("recurso.tmp", 'r').read())
print("Seu saldo: {} RPs".format(recurso))
entrada = int(input("Quantas dezenas deseja jogar? "))

if(entrada<6 or entrada>15):
  print("Número inválido! Tente um número entre 6 e 15.")
else:
  precos = funcoes.get_price_list()
  dezenas = entrada
  if(recurso<precos[dezenas]):
    print("Você não tem dinheiro suficiente!")
    print("Saldo atual: {0}. {1} RPs restantes.".format(recurso, precos[dezenas]-recurso))
  else:
    entrada = input("Digite suas tentativas: ({} números)\n".format(dezenas))
    tentativa = list(map(int, entrada.split()))
    
    if(funcoes.is_valid_attempt(tentativa, dezenas)):
      recurso -= precos[dezenas]
      sorteio = funcoes.generate_numbers()
      acertos = funcoes.get_hits(tentativa, sorteio)
      premios = [2, 10, 50, 40000, 520000, 20000000]
      if(acertos>0):
        print("\nVocê ganhou {} RPs. Total de acertos: {}".format(premios[acertos-1], acertos))
        recurso += premios[acertos-1]
        a = open("recurso.tmp", 'w')
        a.write("{}".format(recurso))
        a.close()
        print("Saldo atual: {} RPs\n".format(recurso))
        funcoes.print_ticket(tentativa, sorteio, precos[dezenas])
      else:
        print("\nVocê não fez nenhum acerto!")
        a = open("recurso.tmp", 'w')
        a.write("{}".format(recurso))
        a.close()
        print("Saldo atual: {} RPs\n".format(recurso))
        funcoes.print_ticket(tentativa, sorteio, precos[dezenas])