votacao = True
voto_X = 0
voto_Y = 0
voto_Z = 0
voto_N = 0


while (votacao == True):
  try:
    voto = int(input(print(
        '''Em quem você deseja votar? 
        Para candidato_X digite 889
        Para candidato_Y digite 847
        Para candidato_Z digite 515
        ''')))
    
    if (voto == 889):
      voto_X += 1
      print("Seu voto foi computado com sucesso!")
      encerrar_voto = input(print("Você deseja finalizar a votação? Digite 'sim' para encerrar e 'nao' para continuar."))
      if encerrar_voto == "sim":
        votacao = False
      elif encerrar_voto == "nao":
        continue
      else:
        print(Erros.erro_numero.value)  
        votacao = False
    elif (voto == 847):
      voto_Y += 1
      print("Seu voto foi computado com sucesso!")
      encerrar_voto = input(print("Você deseja finalizar a votação? Digite 'sim' para encerrar e 'nao' para continuar."))
      if encerrar_voto == "sim":
        votacao = False
      elif encerrar_voto == "nao":
        continue
      else:
        print(Erros.erro_numero.value)
        votacao = False
    elif (voto == 515):
      voto_Z += 1
      print("Seu voto foi computado com sucesso!")
      encerrar_voto = input(print("Você deseja finalizar a votação? Digite 'sim' para encerrar e 'nao' para continuar."))
      if encerrar_voto == "sim":
        votacao = False
      elif encerrar_voto == "nao":
        continue
      else:
        print(Erros.erro_numero.value)
        votacao = False
    elif (voto != 889) or (voto != 847) or (voto != 515):
      voto_N += 1
      print("Seu voto foi computado como branco/nulo!")
      encerrar_voto = input(print("Você deseja finalizar a votação? Digite 'sim' para encerrar e 'nao' para continuar."))
      if encerrar_voto == "sim":
        votacao = False
      elif encerrar_voto == "nao":
        continue
      else:
        print(Erros.erro_numero.value)
        votacao = False
  except:
    print(Erros.erro_string.value)

if (voto_X > voto_Y) and (voto_X > voto_Z) and (voto_X > voto_N):
  print(f"O vencedor é candidato_X com {voto_X} votos!")
  print(f"Votos do candidato_Y: {voto_Y}. Votos do candidato_Z: {voto_Z}. Votos brancos/nulos: {voto_N}")
elif (voto_Y > voto_X) and (voto_Y > voto_Z) and (voto_Y > voto_N):
  print(f"O vencedor é candidato_Y com {voto_Y} votos!")
  print(f"Votos do candidato_X: {voto_X}. Votos do candidato_Z: {voto_Z}. Votos brancos/nulos: {voto_N}")
elif (voto_Z > voto_Y) and (voto_Z > voto_X) and (voto_Z > voto_N):
  print(f"O vencedor é candidato_Z com {voto_Z} votos!")
  print(f"Votos do candidato_X: {voto_X}. Votos do candidato_Y: {voto_Y}. Votos brancos/nulos: {voto_N}")
elif voto_N > voto_X and voto_N > voto_Y and voto_N > voto_Z:
  print(f"Os votos em branco/nulo foram em maior quantidade com {voto_N} votos! Percebe-se a vontade grande em mudar a história do país!")
  print(f"Votos do candidato_X: {voto_X}. Votos do candidato_Y: {voto_Y}. Votos do candidato_Z: {voto_Z}")
else:
  print("Deu empate, vamos para o segundo turno galera!")
  print(f"Votos do candidato_X: {voto_X}. Votos do candidato_Y: {voto_Y}. Votos do candidato_Z: {voto_Z}. Votos brancos/nulos: {voto_N}")
