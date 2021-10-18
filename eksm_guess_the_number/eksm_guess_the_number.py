# Importando a biblioteca para gerar números aleatórios
import random

# Criando mensagem de boas vindas
print("*********************************", end='\n \n')
print("Bem vindo ao jogo de adivinhação!", end='\n \n')
print("*********************************", end='\n \n')

# Definindo o número secreto
numero_secreto = round(random.randrange(1, 21))

# Definindo variável que controla as tentativas
total_de_tentativas = 0

# Definindo variável que controla os pontos
pontos = 100

# Escolha de dificuldade
print("Níveis de dificuldade:")
print("(1) Fácil, (2) Médio ou (3) Difícil")

nivel = int(input("Defina o nível: "))

if(nivel == 1):
  total_de_tentativas = 5
elif(nivel == 2):
  total_de_tentativas = 4
elif(nivel == 3):
  total_de_tentativas = 3

# Contagem de tentativas
for rodada in range(1, total_de_tentativas + 1):
  print("Tentativa {} de {}".format(rodada, total_de_tentativas))

  chute_str = input("Digite um número entre 1 e 20: ") # Coletando o chute
  print("Você digitou ", chute_str)
  chute = int(chute_str)

  if(chute < 1 or chute > 100): # Chute inválido
    print("Você deve digitar um número entre 1 e 20!")
    continue

  acertou = chute == numero_secreto # Chute certo
  maior = chute > numero_secreto # Chute maior que numero secreto
  menor = chute < numero_secreto # Chute menor que número secreto

  if(acertou): # Se chute for certo, mostra pontuação final
    print("Paranéns! Você acertou e fez {} pontos.".format(pontos),
          end = "\n \n")
    break 
  else:
    if(maior): # Se chute for maior, apresenta pista
      print("Você errou! O seu chute foi maior do que o número secreto.")
      print()
    elif(menor): # Se chute for menor, apresenta pista
      print("Você errou! O seu chute foi menor do que o número secreto.")
      print()
    pontos_perdidos = abs(numero_secreto - chute) # Erro diminui pontos
    pontos = pontos - pontos_perdidos

# Mensagem final
print("O número era {}.\nFim do jogo".format(numero_secreto))

