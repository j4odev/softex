/* Proposta: 

Desenvolva um código e crie nele:
- um objeto com, no mínimo, três propriedades;
- um array de tamanho três no mínimo;
- duas funções, a primeira lista as propriedades do objeto e a segunda, os elementos do array. */

// Criando o objeto

let albumOfTheYear = {
  lorde: 'Melodrama',
  lanaDelRey: 'Ultraviolence',
  robyn: 'Honey'
}

// Criando o array

const songOfTheYear = ['Solar Power by Lorde', 'Hold On by Adele', 'All Too Well by Taylor Swift']

// Criando as funções

// Primeira função que irá exibir as propriedades do objeto

function AOTY() {
  console.log('And the nominees for Album of the Year are: ', albumOfTheYear)
}

// Segunda função que irá exibir os elementos do array

function SOTY() {
  console.log('And the nominees for Song of the Year are: ', songOfTheYear)
}

// Exibindo o programa

AOTY()
SOTY()
