import flet as ft

def main(page):
    page.title = "Calculadora de IMC"
    page.window.width = 600

    def validaAltura (e):
        if not (altura.value.isnumeric() and int(altura.value)>0):
            altura.error_text = "Insira um Valor Númerico Positivo"
            altura.value = None
        else:
            altura.error_text = None
        page.update()
    
    def validaPeso (e):
        if not (peso.value.isnumeric() and int(peso.value)>0):
            peso.error_text = "Insira um Valor Númerico Positivo"
            peso.value = None
        else:
            peso.error_text = None
        page.update()

    def salvar (e):
        if altura.value != "" and peso.value != "":
            pesoFloat = float(peso.value)
            alturaMetros = float(altura.value) / 100
            imc = pesoFloat / (alturaMetros ** 2)

        if imc < 18.5:
            texto.value = f"Seu IMC e {imc:.2f} - Abaixo do peso"
            imagem.src = "src/baixo.png"
        elif 18.5 <= imc < 24.9:
            texto.value = f"Seu IMC e {imc:.2f} - Peso normal"
            imagem.src = "src/normal.png"
        elif 25 <= imc < 29.9:
            texto.value = f"Seu IMC e {imc:.2f} - Sobrepeso"
            imagem.src = "src/acima.png"
        elif 30 <= imc < 34.9:
            texto.value = f"Seu IMC e {imc:.2f} - Obesidade grau 1"
            imagem.src = "src/I.png"
        elif 35 <= imc < 39.9:
            texto.value = f"Seu IMC e {imc:.2f} - Obesidade grau 2"
            imagem.src = "src/II.png"
        else:
            texto.value = f"Seu IMC e {imc:.2f} - Obesidade grau 3"
            imagem.src = "src/III.png"

        page.update()

    page.appbar = ft.AppBar(title = ft.Text("Calculadora de IMC", size = 22, color = "white", weight="bold"), center_title = True, bgcolor = "#4CADE4")
    
    texto = ft.Text("Insira suas Informações", size = 22, weight = "bold", width = 150)
    imagem = ft.Image(src = "src/img.png", width = 150, height = 150)
    
    altura = ft.TextField(label = "Altura (Cm)", hint_text = "Por Favor insira sua Altura",width = 300,on_change = validaAltura , autofocus = True)
    peso = ft.TextField(label = "Peso (Kg)", hint_text = "Por Favor insira seu Peso", width = 300, on_change = validaPeso)

    botao = ft.ElevatedButton("Calcular IMC", on_click=salvar)

    page.add(ft.Row([ft.Column(controls = [ft.Row([texto, imagem], alignment = ft.MainAxisAlignment.CENTER), altura, peso, botao],
                               horizontal_alignment = ft.CrossAxisAlignment.CENTER)], alignment = ft.MainAxisAlignment.CENTER))

ft.app(target = main)