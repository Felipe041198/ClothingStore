from src.controller.controlador_clientes import ControladorClientes
from src.controller.controlador_vendedores import ControladorVendedores


def exibir_menu_principal():
    __controlador_clientes = ControladorClientes()
    __controlador_vendedores = ControladorVendedores()

    while True:
        print("\n--- Sistema de Gerenciamento de Loja de Roupas ---")
        print("1. Cadastrar Clientes")
        print("2. Cadastrar Vendedores")
        print("3. Cadastrar Produtos")
        print("4. Registrar Vendas")
        print("5. Consultar histórico")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            __controlador_clientes.menu_clientes()
        elif opcao == '2':
            __controlador_vendedores.menu_vendedores()
        elif opcao == '3':
            pass
            # Chamar o controller de produtos
        elif opcao == '4':
            pass
            # Chamar o controller de vendas
        elif opcao == '5':
            pass
            # Atraves do menu consultar o historico
        elif opcao == '0':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == '__main__':
    exibir_menu_principal()
