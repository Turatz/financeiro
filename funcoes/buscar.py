from banco import conn, cursor


def buscar_por_data():
    data = input("Digite a data (AAAA-MM-DD) ou (AAAA-MM): ").strip()

    cursor.execute(
        "SELECT * FROM transacoes WHERE data LIKE ?",
        (data + "%",),
    )
    linhas = cursor.fetchall()

    if not linhas:
        print("Nenhuma transação nessa data.")
        return []

    for id, descricao, valor, tipo, data_transacao in linhas:
        print(f"{id} | {data_transacao} | {descricao} | {tipo} | R$ {valor:.2f}")

    return linhas


def buscar(id_transacao):
    cursor.execute("SELECT * FROM transacoes WHERE id = ?", (id_transacao,))
    return cursor.fetchone()