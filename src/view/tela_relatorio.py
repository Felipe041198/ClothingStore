import tkinter as tk
from tkinter import ttk
from typing import List


class TelaRelatorioTkinter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Menu de Relatórios")
        self.root.geometry("800x600")
        self.root.config(bg="#2C2F36")

        self.clientes_var = {}
        self.vendedores_var = {}
        self.periodo_var = tk.StringVar()

        # Frame principal
        main_frame = tk.Frame(self.root, bg="#2C2F36")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Título do menu
        titulo = tk.Label(main_frame, text="MENU DE RELATÓRIOS", font=("Arial", 24), fg="white", bg="#2C2F36")
        titulo.pack(pady=20)

        # Frame para os filtros
        filtros_frame = tk.Frame(main_frame, bg="#2C2F36")
        filtros_frame.pack(padx=5, pady=5)

        # Cor de fundo e dimensões reduzidas
        cor_fundo = "#696969"  # Cinza escuro
        frame_width = 150
        frame_height = 250

        # Frames laterais para Clientes, Vendedores e Período
        clientes_frame = tk.LabelFrame(filtros_frame, text="Clientes", width=frame_width, height=frame_height,
                                       padx=10, pady=10, font=("Arial", 12), bg=cor_fundo)
        vendedores_frame = tk.LabelFrame(filtros_frame, text="Vendedores", width=frame_width, height=frame_height,
                                         padx=10, pady=10, font=("Arial", 12), bg=cor_fundo)
        periodo_frame = tk.LabelFrame(filtros_frame, text="Período", width=frame_width, height=frame_height,
                                      padx=10, pady=10, font=("Arial", 12), bg=cor_fundo)

        # Ajustar altura fixa
        clientes_frame.pack_propagate(False)
        vendedores_frame.pack_propagate(False)
        periodo_frame.pack_propagate(False)

        clientes_frame.pack(side=tk.LEFT, fill=tk.Y, expand=False, padx=5)
        vendedores_frame.pack(side=tk.LEFT, fill=tk.Y, expand=False, padx=5)
        periodo_frame.pack(side=tk.LEFT, fill=tk.Y, expand=False, padx=5)

        # Configuração de scroll
        self.add_scrollable_list(clientes_frame, "clientes", 20)
        self.add_scrollable_list(vendedores_frame, "vendedores", 10)

        # Opções de período
        periodo_opcoes = [
            ("Últimas 24 horas", "1"),
            ("Últimos 7 dias", "2"),
            ("Últimos 15 dias", "3"),
            ("Último mês", "4"),
            ("Todos os registros", "5"),
        ]
        for texto, valor in periodo_opcoes:
            ttk.Radiobutton(
                periodo_frame, text=texto, variable=self.periodo_var, value=valor,
                style="TRadiobutton"
            ).pack(anchor=tk.W)

        # Alinhando os botões lado a lado, abaixo dos frames de filtros
        botoes_frame = tk.Frame(main_frame, pady=10, bg="#2C2F36")
        botoes_frame.pack(pady=10)

        ttk.Button(botoes_frame, text="Última Venda", command=self.ultima_venda, style="TButton").pack(side=tk.LEFT,
                                                                                                       padx=10)
        ttk.Button(botoes_frame, text="Última Compra", command=self.ultima_compra, style="TButton").pack(side=tk.LEFT,
                                                                                                         padx=10)
        ttk.Button(botoes_frame, text="Pesquisar", command=self.pesquisar, style="TButton").pack(side=tk.LEFT, padx=10)
        ttk.Button(botoes_frame, text="Limpar Filtros", command=self.limpar_filtros, style="TButton").pack(side=tk.LEFT,
                                                                                                           padx=10)

        self.resultado_label = None

    def add_scrollable_list(self, parent_frame, tipo: str, count: int):
        """Adiciona uma lista com rolagem ao frame pai."""
        canvas = tk.Canvas(parent_frame, height=150, bg=parent_frame['bg'])
        scrollbar = ttk.Scrollbar(parent_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=parent_frame['bg'])

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Limitando a exibição inicial a cinco itens
        items = [f"{tipo.capitalize()} {i + 1}" for i in range(count)]
        display_limit = 5
        visible_items = items[:display_limit]

        if tipo == "clientes":
            for item in visible_items:
                self.clientes_var[item] = tk.BooleanVar()
                tk.Checkbutton(scrollable_frame, text=item, variable=self.clientes_var[item], font=("Arial", 10),
                               bg=parent_frame['bg'], fg="black").pack(anchor=tk.W)
        elif tipo == "vendedores":
            for item in visible_items:
                self.vendedores_var[item] = tk.BooleanVar()
                tk.Checkbutton(scrollable_frame, text=item, variable=self.vendedores_var[item], font=("Arial", 10),
                               bg=parent_frame['bg'], fg="black").pack(anchor=tk.W)

    def obter_selecionados(self, variaveis: dict) -> List[str]:
        """Obtém os itens selecionados de um dicionário de variáveis."""
        return [item for item, var in variaveis.items() if var.get()]

    def ultima_venda(self):
        """Exibe o relatório da última venda."""
        mensagem = "Exibindo a última venda realizada..."
        self.exibir_resultado(mensagem)

    def ultima_compra(self):
        """Exibe o relatório da última compra."""
        mensagem = "Exibindo a última compra realizada..."
        self.exibir_resultado(mensagem)

    def pesquisar(self):
        """Exibe o relatório com os filtros selecionados."""
        clientes_selecionados = self.obter_selecionados(self.clientes_var)
        vendedores_selecionados = self.obter_selecionados(self.vendedores_var)
        periodo = self.periodo_var.get()

        mensagem = (
            f"Relatório Aplicando Filtros:\n"
            f"Clientes: {', '.join(clientes_selecionados) if clientes_selecionados else 'Nenhum'}\n"
            f"Vendedores: {', '.join(vendedores_selecionados) if vendedores_selecionados else 'Nenhum'}\n"
            f"Período: {periodo if periodo else 'Nenhum selecionado'}"
        )
        self.exibir_resultado(mensagem)

    def limpar_filtros(self):
        """Reseta todos os filtros e limpa a exibição de resultado."""
        for var in self.clientes_var.values():
            var.set(False)
        for var in self.vendedores_var.values():
            var.set(False)
        self.periodo_var.set("")

        if self.resultado_label:
            self.resultado_label.destroy()

    def exibir_resultado(self, mensagem: str):
        """Exibe o resultado do relatório na tela."""
        if self.resultado_label:
            self.resultado_label.destroy()

        self.resultado_label = tk.Label(self.root, text=mensagem, font=("Arial", 12), justify=tk.LEFT, bg="#2C2F36",
                                        fg="white")
        self.resultado_label.pack(pady=10)


if __name__ == "__main__":
    tela = TelaRelatorioTkinter()
    tela.root.mainloop()
