print("-----")
print("Notas")
print("-----")
print("")

aluno = input("Nome do aluno: ")
n1 = float(input("Insira a primeira nota: "))
n2 = float(input("Insura a segunda nota: "))
n3 = (n1 + n2) / 2
f = float(input("Insura a quantidade de faltas: "))

if n3 >= 7 and f < 3:
    print(aluno, "teve a média de", n3,
          "e teve uma ótima presença, com total de ", f, "faltas e foi aprovado(a).")
elif n3 >= 7 and f >= 3:
    print(aluno, "teve a média de", n3,
          "mas foi reprovado(a) por ter um total de", f, "faltas.")
elif n3 <= 6.9 and f < 3:
    print(aluno, "teve uma boa presença, com um total de", f,
          "faltas, mas ficou com a média", n3, "e foi reprovado(a).")
elif n3 <= 6.9 and f >= 3:
    print(aluno, "não participou devidamente das aulas, com um total de",
          f, "faltas, e também ficou uma média de", n3, "e foi reprovado(a).")

print("")
print("-----")
print("Copyright (C) 2022 João Lucas.")
print("-----")
