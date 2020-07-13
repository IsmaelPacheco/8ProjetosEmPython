#!python
# Gerador de número aleatório
import random


class SimuladorDeNumeroAleatorio:
    def __init__(self):
        self.valor_minimo = 1
        self.mensagem = "Você gostaria de gerar um novo valor aleatório? (S/N) "

    def Iniciar(self):
        resposta = input(self.mensagem).lower()

        try:
            if resposta == "sim" or resposta == "s":
                self.GerarValorAleatorio()
            elif resposta == "não" or resposta == "n":
                print("OK, agradecemos por usar nosso Gerador de Números Aleatórios")

            else:
                print("Por favor, responda com SIM (S) ou NÃO (N)")

        except:
            print("Oh não, ocorreu um erro ao validar suas respostas")

    def GerarValorAleatorio(self):
        valor_maximo = int(
            input("Digite o valor inteiro máximo para o número gerado: "))
        print(random.randint(self.valor_minimo, valor_maximo))


gerador = SimuladorDeNumeroAleatorio()
gerador.Iniciar()
