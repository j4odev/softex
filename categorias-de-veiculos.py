print('---------------------')
print('Categoria de veículos')
print('---------------------')
print('')

qtdRodas = int(input('Qual a quantidade de rodas presentes no veículo? '))
Kg = float(input('Qual o peso do veículo em quilogramas (Kg)? '))
qtdPessoas = int(input('Quantas pessoas o veículo suporta? '))

print('-------------------------------------')
if qtdRodas <=3:
  print('A categoria do veículo é A.')
elif qtdRodas ==4 and Kg <= 3500 and qtdPessoas <=8:
  print('A categoria do veículo é B.')
elif qtdRodas >=4 and Kg >= 3500 <=6000:
  print('A categoria do veículo é C.')
elif qtdRodas >=4 and qtdPessoas > 8:
  print('A categoria do veículo é D.')
elif qtdRodas >=4 and Kg > 6000:
  print('A categoria do veículo é E.')

print('-------------------------------------')
print('Copyright (C) Femdev/João Lucas 2022.')
print('-------------------------------------')
print('')
