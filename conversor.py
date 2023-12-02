import tkinter as tk
from tkinter import ttk

UNIDADES = {
    "Comprimento": ["Metro", "Quilometro", "Milimetro", "Centimetro", "Polegada", "Pe", "Jarda", "Milha"],
    "Massa": ["Quilograma", "Grama", "Miligrama", "Tonelada", "Libra", "Onca"],
    "Temperatura": ["Celsius", "Fahrenheit"],
    "Tempo": ["Segundo", "Minuto", "Hora", "Dia", "Semana", "Ano"],
}

def converter_comprimento(valor, de_unidade, para_unidade):
    unidades = {
        "Metro": 1,
        "Quilometro": 1000,
        "Milimetro": 0.001,
        "Centimetro": 0.01,
        "Polegada": 0.0254,
        "Pe": 0.3048,
        "Jarda": 0.9144,
        "Milha": 1609.34,
    }
    resultado = valor * unidades[de_unidade] / unidades[para_unidade]
    return resultado

def converter_massa(valor, de_unidade, para_unidade):
    unidades = {
        "Quilograma": 1,
        "Grama": 0.001,
        "Miligrama": 1e-6,
        "Tonelada": 1000,
        "Libra": 0.453592,
        "Onca": 0.0283495,
    }
    resultado = valor * unidades[de_unidade] / unidades[para_unidade]
    return resultado

def converter_temperatura(valor, de_unidade, para_unidade):
    if de_unidade == "Celsius" and para_unidade == "Fahrenheit":
        return (valor * 9/5) + 32
    elif de_unidade == "Fahrenheit" and para_unidade == "Celsius":
        return (valor - 32) * 5/9
    else:
        return valor  # As demais conversões de temperatura não são lineares e precisariam de equações mais complexas

def converter_tempo(valor, de_unidade, para_unidade):
    unidades = {
        "Segundo": 1,
        "Minuto": 60,
        "Hora": 3600,
        "Dia": 86400,
        "Semana": 604800,
        "Ano": 31536000,
    }
    resultado = valor * unidades[de_unidade] / unidades[para_unidade]
    return resultado

def update_opcoes_para(*args):
    global tipo_combobox, de_combobox, para_combobox
    tipo_selecionado = tipo_combobox.get()
    if tipo_selecionado in UNIDADES:
        de_combobox["values"] = UNIDADES[tipo_selecionado]
        para_combobox["values"] = UNIDADES[tipo_selecionado]
        para_combobox.set(UNIDADES[tipo_selecionado][0])

def converter():
    tipo = tipo_combobox.get()
    de_unidade = de_combobox.get()
    para_unidade = para_combobox.get()
    valor = float(valor_entry.get())

    abreviaturas = {
        "Comprimento": {"Metro": "m", "Quilometro": "km", "Milimetro": "mm", "Centimetro": "cm", "Polegada": "in", "Pe": "ft", "Jarda": "yd", "Milha": "mi"},
        "Massa": {"Quilograma": "kg", "Grama": "g", "Miligrama": "mg", "Tonelada": "t", "Libra": "lb", "Onca": "oz"},
        "Temperatura": {"Celsius": "°C", "Fahrenheit": "°F"},
        "Tempo": {"Segundo": "s", "Minuto": "min", "Hora": "h", "Dia": "dia", "Semana": "sem", "Ano": "ano"},
    }

    if tipo in abreviaturas and de_unidade in abreviaturas[tipo] and para_unidade in abreviaturas[tipo]:
        resultado = 0
        unidade_resultado = para_unidade
        abreviatura_unidade = abreviaturas[tipo][para_unidade]

        if tipo == "Comprimento":
            resultado = converter_comprimento(valor, de_unidade, para_unidade)
        elif tipo == "Massa":
            resultado = converter_massa(valor, de_unidade, para_unidade)
        elif tipo == "Temperatura":
            resultado = converter_temperatura(valor, de_unidade, para_unidade)
        elif tipo == "Tempo":
            resultado = converter_tempo(valor, de_unidade, para_unidade)
    else:
        resultado = "Erro: Tipo de conversão não reconhecido."
        unidade_resultado = ""
        abreviatura_unidade = ""

    # Arredonda para no máximo 6 casas decimais
    resultado_arredondado = round(resultado, 6)

    resultado_label.config(text=f"Resultado: {resultado_arredondado} {abreviatura_unidade}", font=("Helvetica", 14, "bold"), foreground="#0074C5")
    
    # Adiciona um efeito de destaque temporário
    resultado_label.after(100, lambda: resultado_label.config(background="#FFFF00"))
    resultado_label.after(500, lambda: resultado_label.config(background="SystemButtonFace"))


# Criar a janela principal
root = tk.Tk()
root.title("Conversor de Unidades")

# Estilizar a janela
style = ttk.Style()

# Criar o frame principal
main_frame = ttk.Frame(root)
main_frame.grid(row=0, column=0, sticky="nsew", padx=50)  # Adicionando um espaçamento à esquerda
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Criar widgets no frame
tipo_label = ttk.Label(main_frame, text="Escolha o tipo de conversão:")
tipo_combobox = ttk.Combobox(main_frame, values=list(UNIDADES.keys()))
tipo_combobox.set("Comprimento")
tipo_combobox.bind("<<ComboboxSelected>>", update_opcoes_para)

de_label = ttk.Label(main_frame, text="De:")
de_combobox = ttk.Combobox(main_frame, values=UNIDADES["Comprimento"])
de_combobox.set("Metro")

para_label = ttk.Label(main_frame, text="Para:")
para_combobox = ttk.Combobox(main_frame, values=UNIDADES["Comprimento"])
para_combobox.set("Metro")

valor_label = ttk.Label(main_frame, text="Digite o valor:")
valor_entry = ttk.Entry(main_frame)

converter_button = ttk.Button(main_frame, text="Converter", command=converter)

resultado_label = ttk.Label(main_frame, text="Resultado: ", style="TLabel", font=("Helvetica", 14, "bold"), foreground="#0074C5")

# Organizar widgets na grade
tipo_label.grid(row=0, column=0, pady=10, padx=(0, 10), sticky="e")  # Alinhando à direita
tipo_combobox.grid(row=0, column=1, pady=10, padx=10)
de_label.grid(row=1, column=0, pady=10, padx=(0, 10), sticky="e")  # Alinhando à direita
de_combobox.grid(row=1, column=1, pady=10, padx=10)
para_label.grid(row=2, column=0, pady=10, padx=(0, 10), sticky="e")  # Alinhando à direita
para_combobox.grid(row=2, column=1, pady=10, padx=10)
valor_label.grid(row=3, column=0, pady=10, padx=(0, 10), sticky="e")  # Alinhando à direita
valor_entry.grid(row=3, column=1, pady=10, padx=10)
converter_button.grid(row=4, column=0, columnspan=2, pady=10, padx=10)
resultado_label.grid(row=5, column=0, columnspan=2, pady=10, padx=10)

# Centralizar entradas de dados
main_frame.place(relx=0.5, rely=0.5, anchor="center")

# Iniciar a aplicação
root.mainloop()
