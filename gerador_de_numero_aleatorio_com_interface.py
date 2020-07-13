#!python
# Gerador de número aleatório
import random
import PySimpleGUI as sg


class GeradorDeNumeroAleatorio:
    def __init__(self):
        self.valor_minimo = 1

        # Definir layout da aplicação
        self.layoutTela = [
            [sg.Text("Gerar número aleatório?")],
            [sg.Button("Sim"), sg.Button("Não")],
        ]
        self.layoutTelaDeValorMax = [
            [sg.Text("Digite o valor máximo do número gerado"), sg.Input()],
            # [sg.Input(key='-IN-', enable_events=True)],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]
        self.mensagem_final = [
            [
                sg.Text(
                    "OK, agradecemos por usar nosso Gerador de Números Aleatórios"),
                sg.Button("Fechar")]
        ]
        self.error = [
            [
                sg.Text("Oh não, ocorreu um erro ao validar suas respostas"),
                sg.Button("Fechar")]
        ]

    def Iniciar(self):
        # Criar uma janela
        self.janela = sg.Window(
            "Gerador de número aleatório", layout=self.layoutTela)
        # Ler os valores da Tela
        self.eventos, self.valores = self.janela.Read()

        if self.eventos == "Sim":
            self.janelaInput = sg.Window(
                "Gerador de número aleatório", layout=self.layoutTelaDeValorMax)

            self.eventosInput, self.valoresInput = self.janelaInput.Read()

            valor_aleatorio_final = "Seu número aleatório é: {}".format(random.randint(
                self.valor_minimo, int(self.valoresInput[0])))

            self.valor_aleatorio = [
                [
                    sg.Text(valor_aleatorio_final),
                    sg.Button("Fechar")
                ]
            ]

        elif self.eventos == "Não":
            self.msg = sg.Window(
                "Gerador de número aleatório", layout=self.mensagem_final)
            self.msgFinal = self.msg.Read()

        # Fazer alguma coisa com os valores
        try:
            if self.eventos == "Sim":
                if self.eventosInput == "OK":
                    self.GerarValorAleatorio()

                elif self.eventosInput == "Cancelar":
                    self.msg = sg.Window(
                        "Gerador de número aleatório", layout=self.mensagem_final)
                    self.msgFinal = self.msg.Read()

        except:
            self.msg = sg.Window(
                "Gerador de número aleatório", layout=self.error)
            self.msgFinal = self.msg.Read()

    def GerarValorAleatorio(self):
        # valor_max = int(self.valoresInput[0])
        random.randint(self.valor_minimo, int(self.valoresInput[0]))

        self.msg = sg.Window(
            "Gerador de número aleatório", layout=self.valor_aleatorio)
        self.msgFinal = self.msg.Read()
        # print(random.randint(self.valor_minimo, valor_max))


gerador = GeradorDeNumeroAleatorio()
gerador.Iniciar()
