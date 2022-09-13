/* diante o conteúdo prestado na plataforma online, é quase impossível criar um código com métodos, por isso fiz uma aplicação padrão utilizando
ferramentas de estruturas de repetição */

alert("Olá, economista!");
alert("Controle financeiro é na SoftBank :D");

accountNumber = parseFloat(prompt('Digite o número de sua conta: '))
name = "Isaac Pontes"
balance = 2534
let total = balance;

do {
  option = prompt(
    "Olá, " + name + "!" + '\nA sua quantia atual é de R$' +
      total +
      "." +
      "\n\nSelecione uma opção: \n\n1. Depositar\n2. Sacar\n3. Mostrar saldo\n4. Mostrar número da conta\n5. Encerrar"
  );

  switch (option) {
    case "1":
      deposit = parseFloat(prompt("Valor do depósito: "));
      total = balance + deposit;
      break;

    case "2":
      withdraw = parseFloat(prompt("Valor a ser sacado:"));
      total = balance - withdraw;
      break;

    case "3":
      alert("O seu saldo atual é de: " + total);
      break;

    case "4":
      alert('O número de sua conta é: ' + accountNumber)
      break

    case "5":
      alert("Você escolheu encerrar.");
      alert("Encerrando...");
      break

    default:
      alert("Insira uma opção válida.");
  }
} while (option !== "5");