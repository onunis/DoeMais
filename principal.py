import tkinter as tk
from paginas.formulario import criar_formulario
from paginas.doacoes import criar_pagina_doacoes

def criar_pagina_principal(pai, usuario_logado):
    frame = tk.Frame(pai, bg="#26b9d1")
    frame.pack(expand=True, fill="both")

    menu = tk.Frame(frame, bg="#26b9d1")
    menu.pack(pady=10)

    conteudo = tk.Frame(frame, bg="#26b9d1")
    conteudo.pack(expand=True, fill="both")

    tk.Label(menu, text=f"Bem-vindo, {usuario_logado.get('nome', '')}!", bg="#26b9d1", font=("Arial", 12)).pack(side="left", padx=10)

    def mostrar_formulario():
        for w in conteudo.winfo_children():
            w.destroy()
        criar_formulario(conteudo)

    def mostrar_doacoes():
        for w in conteudo.winfo_children():
            w.destroy()
        criar_pagina_doacoes(conteudo, usuario_logado)

    tk.Button(menu, text="Nova Doação", command=mostrar_formulario).pack(side="left", padx=10)
    tk.Button(menu, text="Doações Feitas", command=mostrar_doacoes).pack(side="left", padx=10)

    mostrar_formulario()

    return frame
