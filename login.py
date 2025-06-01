import tkinter as tk
from tkinter import messagebox
from banco import conectar

def criar_pagina_login(pai, trocar_tela, usuario_logado):
    frame = tk.Frame(pai, bg="#26b9d1")  
    frame.pack(expand=True, fill="both")

    conteudo = tk.Frame(frame, bg="#26b9d1")
    conteudo.pack(expand=True)

    tk.Label(conteudo, text="Login", font=("Arial", 20), bg="#26b9d1").pack(pady=20)

    tk.Label(conteudo, text="Usuário:", bg="#26b9d1").pack()
    entrada_usuario = tk.Entry(conteudo)
    entrada_usuario.pack()

    tk.Label(conteudo, text="Senha:", bg="#26b9d1").pack()
    entrada_senha = tk.Entry(conteudo, show="*")
    entrada_senha.pack()

    def login():
        usuario = entrada_usuario.get()
        senha = entrada_senha.get()
        with conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE usuario=? AND senha=?", (usuario, senha))
            if cursor.fetchone():
                usuario_logado["nome"] = usuario
                trocar_tela("principal")
            else:
                messagebox.showerror("Erro", "Usuário ou senha inválidos")

    def abrir_cadastro():
        cadastro_win = tk.Toplevel()
        cadastro_win.title("Cadastro de Usuário")

        largura = 300
        altura = 200
        largura_tela = cadastro_win.winfo_screenwidth()
        altura_tela = cadastro_win.winfo_screenheight()
        x = (largura_tela - largura) // 2
        y = (altura_tela - altura) // 2
        cadastro_win.geometry(f"{largura}x{altura}+{x}+{y}")

        tk.Label(cadastro_win, text="Novo Usuário:").pack(pady=5)
        novo_usuario = tk.Entry(cadastro_win)
        novo_usuario.pack()

        tk.Label(cadastro_win, text="Senha:").pack(pady=5)
        nova_senha = tk.Entry(cadastro_win, show="*")
        nova_senha.pack()

        def cadastrar():
            u = novo_usuario.get()
            s = nova_senha.get()
            if not u or not s:
                messagebox.showwarning("Aviso", "Preencha todos os campos.")
                return
            with conectar() as conn:
                cursor = conn.cursor()
                try:
                    cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES (?, ?)", (u, s))
                    conn.commit()
                    messagebox.showinfo("Sucesso", "Usuário cadastrado!")
                    cadastro_win.destroy()
                except:
                    messagebox.showerror("Erro", "Usuário já existe.")

        tk.Button(cadastro_win, text="Cadastrar", command=cadastrar).pack(pady=10)

    tk.Button(conteudo, text="Entrar", command=login).pack(pady=10)
    tk.Button(conteudo, text="Cadastrar novo usuário", command=abrir_cadastro).pack()

    return frame
