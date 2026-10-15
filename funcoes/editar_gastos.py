from banco import conn, cursor
from funcoes.buscar import buscar_por_data, buscar
from datetime import datetime
from funcoes.apagar import apagar_por_id

def atualizar():
    linhas = buscar_por_data()
    if not linhas:
        return

    try:
        id_transacao = int(input("Digite o id que deseja editar: "))
    except ValueError:
        print ("Id inválido.")
        return 
    
    linha = buscar(id_transacao)

    if linha is None:
        print("Não encontrei nenhuma transação com esse id.")
        return

    print("\nO que deseja mudar?")
    print("1 - Descrição")
    print("2 - Valor")
    print("3 - Tipo (cartao/dinheiro)")
    print("4 - Data")
    print("5 - Apagar")
    print("0 - Cancelar")

    try: 
        escolha = int(input("Escolha:"))
    except ValueError:
        print("Opção inválida.")
        return

    match escolha:
        case 1:
            coluna = "descricao"
            novo = input("Nova descrição: ").strip()
        case 2:
            coluna = "valor"
            try:
                novo = float(input("Novo valor: ").replace(",", "."))
            except ValueError:
                print("Valor inválido.")
                return
        case 3:
            coluna = "tipo"
            novo = input("Novo tipo (cartao/dinheiro): ").strip().lower()
            if novo not in ("cartao", "dinheiro"):
                print("Tipo inválido.")
                return
        case 4:
            coluna = "data"
            novo = input("Nova data (AAAA-MM-DD): ").strip()
            try:
                datetime.strptime(novo, "%Y-%m-%d")
            except ValueError:
                print("Data inválida. Use AAAA-MM-DD.")
                return
        case 5:
            apagar_por_id(id_transacao)
            return
        case 0:
            print("Cancelado.")
            return
        case _:
            print("Opção inválida.")
            return
    cursor.execute(
        f"UPDATE transacoes SET {coluna} = ? WHERE id= ?",
        (novo, id_transacao),
    )
    conn.commit()
    print("Atualizado!")