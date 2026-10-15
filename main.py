import banco
from funcoes.editar_gastos import atualizar
from funcoes.buscar import buscar_por_data
from funcoes.registrar import registrar

def mostrar_menu():
    print("\nAssistente financeiro no terminal")
    print("1 - Editar gasto")
    print("2 - Mostrar gastos")
    print("3 - Registrar gasto")
    print("0 - Sair")


while True:
    mostrar_menu()

    try:
        opcao = int(input("Qual opção deseja escolher: "))
    except ValueError:
        print("Digite apenas números.")
        continue

    match opcao:
        case 1:
            atualizar()
        case 2:
            buscar_por_data()
        case 3:
            registrar()
        case 0:
            print("Saindo...")
            banco.fechar()
            break
        case _:
            print("Opção inválida.")