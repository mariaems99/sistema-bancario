# Módulo principal da aplicação

# Importa a classe Banco responsável por gerenciar clientes e contas
from operacoes.banco import Banco

# Importa exceções personalizadas usadas no fluxo de operações
from utilitarios.exceptions import SaldoInsuficienteError, ContaInexistenteError

# Função que exibe o menu principal da aplicação
def menu_principal():
    print("\n --- Sistema Bancário Digital --- \n")
    print("1. Adicionar Cliente")
    print("2. Criar Conta")
    print("3. Acessar Conta")
    print("4. Sair\n")

    # Retorna a opção digitada pelo usuário
    return input("Escolha uma opção: ")

# Função que exibe o menu de operações de uma conta específica
def menu_conta(banco):
    try:
        # Solicita ao usuário o número da conta
        num_conta = int(input("Digite o número da conta: "))

        # Busca a conta no banco; pode gerar exceção se não existir
        conta = banco.buscar_conta(num_conta)

        # Loop de operações dentro da conta
        while True:
            print(f"Operações para a Conta Nº {conta._numero}---")
            print(f"Cliente {conta._cliente.nome} | Saldo: R${conta.saldo:.2f}")
            print("1. Depositar")
            print("2. Sacar")
            print("3. Ver Extrato")
            print("4. Voltar ao menu principal")

            # Lê a opção do usuário
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                valor = float(input("Digite o valor para depósito: "))
                conta.depositar(valor)

            elif opcao == '2':
                try:
                    valor = float(input("Digite o valor para saque: "))
                    conta.sacar(valor)  # Polimorfismo: depende do tipo de conta
                except SaldoInsuficienteError as e:
                    print(f"Erro na operação {e}")

            elif opcao == '3':
                conta.extrato()

            elif opcao == '4':
                break

            else:
                print("Opção inválida, tente novamente.")

    except ContaInexistenteError as e:
        print(f"Erro {e}")

    except ValueError:
        print("Erro: entrada inválida. Por favor, digite um número.")

# Função principal que controla o fluxo do sistema
def main():
    banco = Banco("Banco Digital MR")

    # Loop principal do sistema
    while True:
        opcao = menu_principal()

        if opcao == '1':
            nome = input("Digite o nome do cliente: ")
            cpf = input("Digite o cpf do cliente: ")
            banco.adicionar_cliente(nome, cpf)

        elif opcao == '2':
            # Cria uma nova conta vinculada a um cliente existente
            cpf = input("Digite o CPF do cliente para vincular a conta: ")
            cliente = banco._clientes.get(cpf)

            if cliente:
                tipo = input("Digite o tipo da conta: corrente/poupanca: ")
                banco.criar_conta(cliente, tipo)
            else:
                print("Cliente não encontrado. Cadastre o cliente primeiro.")

        elif opcao == '3':
            menu_conta(banco)

        elif opcao == '4':
            print("\nObrigado por usar o nosso sistema. Até Logo!\n")
            break

        else:
            print("\n Opção inválida. Por favor tente novamente! \n")

# Ponto de entrada da aplicação
if __name__ == "__main__":
    main()