import tkinter as tk
from src.view.abstract_tela import AbstractTela


class TelaSistema(AbstractTela):
    def __init__(self) -> None:
        self.janela = tk.Tk()
        self.janela.title("Sistema de Gerenciamento de Loja de Roupas")
        self.janela.geometry("500x600")
        self.janela.config(bg="#2C2F36")
        self.option = None

    def tela_opcoes(self, opcoes):
        titulo = tk.Label(self.janela, text="MENU PRINCIPAL", font=("Arial", 20), fg="white", bg="#2C2F36")
        titulo.pack(pady=30)

        # Função para cada botão
        def cria_botao(label, opcao):
            botao = tk.Button(self.janela, text=label, width=20, height=2,
                              command=lambda opcao=opcao: self.set_option(opcao),
                              bg="#3E4349", fg="white", font=("Arial", 12),
                              relief="solid", bd=1)
            botao.bind("<Enter>", lambda e, b=botao: b.config(bg="#4B5359"))
            botao.bind("<Leave>", lambda e, b=botao: b.config(bg="#3E4349"))

            if label == "Sair":
                botao.bind("<Enter>", lambda e, b=botao: b.config(bg="red"))
                botao.bind("<Leave>", lambda e, b=botao: b.config(bg="#3E4349"))

            botao.pack(pady=10)
            return botao

        botoes = [
            ("Cadastrar Clientes", 1),
            ("Cadastrar Vendedores", 2),
            ("Cadastrar Produtos", 3),
            ("Registrar Vendas", 4),
            ("Consultar Histórico", 5),
            ("Mock Dados", 99),
            ("Sair", 0)
        ]

        for label, opcao in botoes:
            cria_botao(label, opcao)

        self.janela.mainloop()

        return self.option

    def set_option(self, opcao):
        self.option = opcao
        self.janela.quit()
