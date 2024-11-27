import flet as ft

def calculaFrequencia(principal, taxa, tempo, frequencia):
    if frequencia == "Mensal":
        numeroFrequencia = 1
    elif frequencia == "Trimestral":
        numeroFrequencia = 4
    elif frequencia == "Semestral":
        numeroFrequencia = 2
    else:
        numeroFrequencia = 12

    calculo = principal * ((1 + (taxa / 100)) ** (tempo /numeroFrequencia))
    return calculo

def main(page):
    page.title = "Calculadora de Juros Compostos"
    page.window.width = 600

    page.appbar = ft.AppBar(title = ft.Text("Calculadora de Juros Compostos", size = 25, color = "BLACK", weight="bold"), center_title = True, bgcolor = "#FFFAFA")

    resultadoGeral = ft.Text("", size=20, color="black", weight="bold")

    valorPrincipal = ft.TextField(label="Valor Principal (R$)", width = 300, autofocus = True)
    valorTaxa = ft.TextField(label="Taxa de Juros (%)", width = 300)
    valorTempo = ft.TextField(label="Tempo (Meses)", width = 300)
    freqJuros = ft.Dropdown(label="Tipo de Frequência de Juros", width = 300, options=[ft.dropdown.Option("Anual"), ft.dropdown.Option("Semestral"),
                                                                                        ft.dropdown.Option("Trimestral"), ft.dropdown.Option("Mensal")])

    def calcular(e):
        try:
            principal = float(valorPrincipal.value)
            taxa = float(valorTaxa.value)
            tempo = float(valorTempo.value)
            frequencia = freqJuros.value
            resultado = calculaFrequencia(principal, taxa, tempo, frequencia)
            resultadoGeral.value = f"Valor Final: R$ {resultado:.2f}"

        except ValueError:
                resultadoGeral.value = "Por favor, insira valores válidos."

        page.update()

    botaoCalcular = ft.ElevatedButton("Calcular Juros Composto", color = "BLACK", on_click = calcular)

    

    page.add(resultadoGeral, valorPrincipal, valorTaxa, valorTempo, freqJuros, botaoCalcular)

ft.app(main)