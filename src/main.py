def exibir_menu_principal():
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
            pass
            # Chamar o controller de clientes
        elif opcao == '2':
            pass
            # Chamar o controller de vendedores
        elif opcao == '3':
            pass
            # Chamar o controller de produtos
        elif opcao == '4':
            pass
            # Chamar o controller de vendas
        elif opcao == '5':
            pass
            # Atraves do menu consultar o historico
        elif opcao == '6':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == '__main__':
    exibir_menu_principal()
