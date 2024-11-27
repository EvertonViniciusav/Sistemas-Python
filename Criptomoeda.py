import flet as ft
import requests

criptomoedas = ["bitcoin", "ethereum", "ripple", "litecoin", "cardano", "polkadot", "dogecoin", "binancecoin", "solana", "uniswap"]

def main(page):
    page.title = "Consulta Valor Criptomoeda"
    page.window.width = 600

    page.appbar = ft.AppBar(title=ft.Text("Sistema de Consultar Valor de Criptomoeda", size=25, color="BLACK", weight="bold"), center_title=True, bgcolor="#FFFAFA")

    def carregarImg(e):
        imagem.src = f"https://c1.coinlore.com/img/25x25/{dropdownMoeda.value.lower()}.png"
        page.update()

    quantidadeMoeda = ft.TextField(label="Digite a Quantidade de Criptomoedas.", autofocus=True)
    dropdownMoeda = ft.Dropdown(label="Selecione a Criptomoeda", options=[ft.dropdown.Option(moeda.capitalize()) for moeda in criptomoedas], on_change= carregarImg)
    resultado = ft.Text()
    resultadoqtd = ft.Text()
    imagem = ft.Image(src = "https://c1.coinlore.com/img/25x25/bitcoin.png")

    def requisitarAPI(e):
        moeda = dropdownMoeda.value.lower()

        url = f"https://api.coingecko.com/api/v3/simple/price?ids={moeda}&vs_currencies=usd"

        try:
            requisicao = requests.get(url)
            if requisicao.status_code == 200:
                valor = requisicao.json()[moeda]["usd"] 
                resultado.value = f"O preço de 1 {moeda.capitalize()} é ${valor:.2f} USD."

                try:
                    quantidade = float(quantidadeMoeda.value)
                    if quantidade > 0:
                        resultadoqtd.value = f"O preço de {quantidade} {moeda.capitalize()} é ${valor * quantidade:.2f} USD."
                    else:
                        resultadoqtd.value = "Por favor, insira uma quantidade válida!"
                except ValueError:
                    resultadoqtd.value = "Insira um número válido para a quantidade de criptomoedas."

            else:
                resultado.value = "Criptomoeda não encontrada."
        except Exception:
            resultado.value = f"Erro ao buscar dados para {moeda.capitalize()}."

        page.update()

    botaoBuscar = ft.ElevatedButton("Buscar Preço", on_click=requisitarAPI)

    page.add(quantidadeMoeda, dropdownMoeda, botaoBuscar, resultado, resultadoqtd, imagem)

ft.app(main)