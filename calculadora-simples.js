// EXECUTAR NO CHROME COM BASE HTML E SCRIPT INDEXADO.

// Calculadora simples c/ retorno de sobras

/* Proposta: Com os conceitos aprendidos, crie um programa de calculadora que: 

- receba dois valores, que devem ser salvos em variáveis; 
- o usuário deve colocar qual operador ele vai utilizar por meio dos símbolos aritméticos; 
- com os dois valores e o operador definido, o programa deve fazer a operação e retornar o resultado; 
- se houver divisão, você deve retornar o resultado e a sobra, caso haja alguma. 

*/

// Solicitando o modo de operação ao usuário

const operacao = prompt("Digite uma opção: [- + * /]");

// Atribuindo os valores

const valor1 = prompt("Insira o valor 1: ");
const valor2 = prompt("Insira o valor 2: ");

let resultado = undefined;
let sobras = undefined;
let parteInteira = undefined;

// Adicionando condições

// Subtração

if (operacao === "-") {
  resultado = valor1 - valor2;
  alert(
    "A diferença entre " + valor1 + " e " + valor2 + " é de " + resultado + "."
  );

  // Adição
}
if (operacao === "+") {
  resultado = valor1 + valor2;
  alert("A soma entre " + valor1 + " e " + valor2 + " é de " + resultado + ".");

  // Multiplicação
} else if (operacao === "*") {
  resultado = valor1 * valor2;
  alert(
    "Multiplicando " + valor1 + " e " + valor2 + " teremos: " + resultado + "."
  );

  //Divisão + Sobras + Parte Inteira
} else if (operacao === "/") {
  resultado = valor1 / valor2;
  sobras = valor1 % valor2;
  parteInteira = parseInt(resultado);
  alert(
    "\nA divisão entre " +
      valor1 +
      " e " +
      valor2 +
      " é de " +
      resultado +
      "\n\nSobras: " +
      sobras +
      "\nParte Inteira: " +
      parteInteira
  );
}

// Retornando erro caso nenhum dos operadores seja digitado corretamente ou os valores não sejam númericos.
else {
  alert(
    "ERRO: Digite um operador válido. \n" +
      "\nERRO: Insira um valor númerico, pois caracteres do tipo string não são aceitos."
  );
}
