algoritmo "NotasdosAlunos"


var

inicializador: inteiro
numAprovados: inteiro
A, B, C, D: caractere
nomeAluno: caractere
nota: real
melhorNota: real
resposta: caractere



inicioalgoritmo

Escreva("Digite qual a turma: ")
Leia(resposta)
Enquanto resposta faça
    caso "A"
        Escreva("Vamos cadastrar os alunos da turma ", resposta)
    caso "B"
        Escreva("Vamos cadastrar os alunos da turma ", resposta)
    caso "C"
         Escreva("Vamos cadastrar os alunos da turma ", resposta)
    caso "D"
         Escreva("Vamos cadastrar os alunos da turma ", resposta)


 Fimenquanto

      inicializador <- 1
      melhorNota <- 0
      numAprovados <- 0

      Para inicializador de 1 ate 25 faça

         Escreva("Aluno(a)", inicializador)
         Escreva("Nome do(a) aluno(a): ")
         Leia(nomeAluno)
         Escreval("Nota do(a) aluno(a):  " , nomeAluno)
         Leia (nota)

         
         Se (nota > melhorNota) então
	melhorNota <- nota

            Se(nota >= 7) entao
               Escreva("Aluno(a) foi aprovado(a)!")
               numAprovados <- numAprovados + 1
            Senao
               Escreva("Aluno(a) foi reprovado(a)!")
            Fimse


      Fimpara

Fimenquanto

Escreva("A maior nota foi do(a) aluno(a) ", nomeAluno, " com nota ", melhorNota, “e da turma”, resposta)
Escreva("A quantidade de aprovados foi " , numAprovados)


fimalgoritmo
