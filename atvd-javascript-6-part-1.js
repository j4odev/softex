// EXECUTAR NO CHROME COM BASE HTML E SCRIPT INDEXADO.

/* Proposta 1: Crie dois códigos de sistema de notas para uma escola. O primeiro código deve ser um programa que informa se o aluno reprovou, ou não,
com base nas três notas que ele adicionou ao programa. Utilize, no mínimo, um operador de atribuição e um operador ternário. */.

// Criando interação com usuário

const nome = prompt("Qual o seu nome? ");
const matricula = prompt("Qual a sua matrícula? ");

// Atribuindo valores

const nota1 = parseFloat(prompt("Insira a primeira nota: "));
const nota2 = parseFloat(prompt("Insira a primeira nota: "));
const nota3 = parseFloat(prompt("Insira a primeira nota: "));

// Vamos levar em consideração que a média para a aprovação seja 6.0

media = (nota1 + nota2 + nota3) / 3;

// Exibindo resultados utilizando operador ternário

media >= 6
  ? alert(
      nome +
        "matrícula: " +
        matricula +
        " foi aprovado com média " +
        media +
        "."
    )
  : alert("o aluno foi reprovado.");
