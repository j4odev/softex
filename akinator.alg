Var
   resposta: caracter

Inicio
   
   escreval("Jogo do Mentalista")
   escreval("Entre os meios de transporte, considere um: ")
   escreval("- Trator")
   escreval("- Moto")
   escreval("- Bicicleta")
   escreval("- Trem")
   escreval("- Carro")
   escreval("- Caminhão")
   escreval("- Ônibus")
   escreval("- Paraquedas")
   escreval("- Balão")
   escreval("- Avião")
   escreval("- Helicóptero")
   escreval("- Submarino")
   escreval("- Barco")
   escreval("- Navio")
   escreval("- Lancha")

   escreval("")

   escreval ("É aquático?")
   leia(resposta)
   se (resposta = "sim") entao
      escreval ("é coberto d'água?")
      leia(resposta)
      se (resposta = "sim") entao
         escreval ("É um submarino")
      senao
         escreval ("Navega na água?")
         leia(resposta)
         se (resposta = "sim") entao
            escreval ("Possui vela?")
            leia (resposta)
            se (resposta = "sim") entao
               se (resposta = "sim") entao
                  escreval("O seu transporte é um Barco!")
               fimse
            fimse
         fimse
      fimse


   senao
      escreval("É terrestre?")
      leia(resposta)
      se (resposta = "sim") entao
         escreval("É pesado?")
         leia(resposta)
         se (resposta = "sim") entao
            escreval("É um trator")
         senao
            escreval("Usa capacete?")
            leia(resposta)
            se (resposta = "sim") entao
               escreval("O transporte é uma moto")
            senao
               escreval("Tem pedal?")
               leia(resposta)
               se (resposta = "sim") entao
                  escreval("O transporte é uma Bicileta")
               senao
                  escreval("usa Trilho?")
                  leia(resposta)
                  se (resposta = "sim") entao
                     escreval("O transporte é um Trem")

                  senao
                     escreval("é um veículo leve?")
                     leia(resposta)
                     se (resposta = "sim") entao
                        escreval("O transporte é um Carro")
                     senao
                        escreval("pode ter cobrador?")
                        leia(resposta)
                        se (resposta = "sim") entao
                           escreval("O transporte é um Ônibus")
                        senao
                           escreval("Usa carroceria?")
                           leia(resposta)
                           se (resposta = "sim") entao
                              escreval("O transporte é um caminhão")
                           fimse
                        fimse
                     fimse
                  fimse
               fimse
            fimse
         fimse

      senao
         escreval("É Aéreo?")
         leia(resposta)
         se (resposta = "sim") entao
            escreval("Precisa Pular?")
            leia(resposta)
            se (resposta = "sim") entao
               escreval("É uma Asa Delta")
            senao
               escreval ("É devagar?")
               leia (resposta)
               se (resposta = "sim") entao
                  escreval ("O transporte é um balão")
               senao
                  escreval ("Possuí Asas Fixas?")
                  leia (resposta)
                  se (resposta = "sim") entao
                     escreval ("O transporte é Avião)
                  senao
                     escreval ("Faz voo vertical?")
                     leia (resposta)
                     se (resposta = "sim") entao
                        escreval ("o transporte é Helicóptero")
                     fimSe
                  fimSe
               fimSE
            fimSe
         fimSe
      fimSe
   fimSe
fimse
fimse
fimse
fimse
fimse
fimse
fimse
fimse
fimse
fimse
Fimalgoritmo

