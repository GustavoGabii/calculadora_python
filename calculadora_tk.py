import tkinter as tk


def clicar_botao(valor):

    if valor == "C":
        visor.delete(0, tk.END)

    elif valor == "⌫":
        texto = visor.get()

        if texto:
            visor.delete(len(texto) - 1, tk.END)

    elif valor == "=":
        expressao = visor.get()

        if not expressao:
            return

        try:
            resultado = eval(expressao, {"__builtins__": {}}, {})
            visor.delete(0, tk.END)
            visor.insert(0, str(resultado))

        except ZeroDivisionError:
            visor.delete(0, tk.END)
            visor.insert(0, "Divisão por zero")

        except Exception:
            visor.delete(0, tk.END)
            visor.insert(0, "Expressão inválida")

    else:
        visor.insert(tk.END, valor)

janela = tk.Tk()
janela.title("Minha Calculadora")
janela.resizable(False, False)

visor = tk.Entry(
    janela,
    width=18,
    font=("Arial", 20),
    justify="right"
)
visor.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=8,
    pady=8
)

botoes = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
    ("⌫", 5, 0), ("=", 5, 1),
]

for texto, linha, coluna in botoes:
    botao = tk.Button(
        janela,
        text=texto,
        width=5,
        height=2,
        font=("Arial", 14),
        command=lambda valor=texto: clicar_botao(valor)
    )
    botao.grid(
        row=linha,
        column=coluna,
        padx=3,
        pady=3
    )

janela.mainloop()

