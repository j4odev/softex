print('Idade')
print('-----')
print(" ")

nome = input("Qual o seu nome? ")
ano_nasc = int(input('Em que ano você nasceu? '))
mes_aniv = int(
    input('Em que mês você nasceu? [1 - Janeiro, 2 - Fevereiro {...}] '))
mes_atual = int(input('Que mês deste ano você está? '))

if ano_nasc < 1922 or ano_nasc > 2021:
    print("Digite um número entre 1922 e 2021.")

elif mes_atual < mes_aniv:
    res = 2022 - ano_nasc
    futuro = mes_aniv - mes_atual
    print(nome, 'você terá ', res, 'anos em ', abs(futuro), 'meses.')

else:
    res = 2022 - ano_nasc
    print(nome, 'você tem ', res, 'anos.')
