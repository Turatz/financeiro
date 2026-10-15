from banco import conn, cursor
from funcoes.buscar import buscar_por_data, buscar

def apagar():
    linhas = buscar_por_data
    if not linhas:
        return

    try:
        id_transacao = int(input("Digite o id que deseja apagar: "))
    
    except ValueError:
            print("Id inválido.")
            return

    linha = buscar(id_transacao)
    if linha is None:
        print("Não encontrei nenhuma transação com esse id.")
        return

    id, descricao, valor, tipo, data = linha
    print(f"\nVocê vai apagar: {id} | {data} | {descricao} | {tipo} | R$ {valor:.2f}")

    confirmacao = input("Tem certeza? (s/n): ").strip().lower()
    if confirmacao != "s":
        print("Cancelado.")
        return

    cursor.execute("DELETE FROM transacoes WHERE id = ?", (id_transacao,))
    conn.commit()
    print("Gasto apagado!")


def apagar_por_id(id_transacao):
    linha = buscar(id_transacao)
    if linha is None:
        print("Não encontrei nenhuma transação com esse id.")
        return

    id, descricao, valor, tipo, data = linha
    print(f"\nVocê vai apagar: {id} | {data} | {descricao} | {tipo} | R$ {valor:.2f}")

    confirmacao = input("Tem certeza? (s/n): ").strip().lower()
    if confirmacao != "s":
        print("Cancelado.")
        return

    cursor.execute("DELETE FROM transacoes WHERE id = ?", (id_transacao,))
    conn.commit()
    print("Gasto apagado!")