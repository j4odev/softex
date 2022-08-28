// EXECUTAR NO CHROME COM BASE HTML E SCRIPT INDEXADO.

/* Proposta 2: O segundo código é um programa que o aluno deve escrever duas notas e o retorno informa a nota mínima que ele deve tirar na próxima prova para
poder passar com nota sete. */

// Criando interação com usuário

const nota1 = parseFloat(prompt("Insira sua primeira nota: "));
const nota2 = parseFloat(prompt("Insira sua segunda nota: "));

// Atribuindo resultados 

prox_nota = 21 - nota1 - nota2;

// Adicionando condições e exibindo os resultados

prox_nota < 10
  ? alert("Você precisa de " + prox_nota + " pontos para ser aprovado(a).")
  : alert(
      "Você precisaria de " +
        prox_nota +
        " pontos para ser aprovado(a). Não sendo possível, você está reprovado(a)"
    );
