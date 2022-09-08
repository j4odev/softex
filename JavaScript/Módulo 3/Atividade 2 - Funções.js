// Proposta 1:  uma função tradicional com a palavra reservada “Function” e sem nenhum parâmetro;

function soma() {
  a = 0;
  a += 1;
  return a;
}

console.log(soma());

// Proposta 2: uma função tradicional com parâmetros e um retorno de valor;

function sub(x, y) {
  return x - y;
}

console.log(sub(4, 3));

// Proposta 3: uma arrow function com parâmetros e que retorne um valor.

const div = (x, y) => x / y;

console.log(div(4, 2));
