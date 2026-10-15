from datetime import date, datetime
from banco import conn, cursor

def registrar():
    descricao = input("Descrição:").strip()
    if descricao == "":
        print("A descrição não pode ficar vazia.")
        return
    try: 
        valor = float(input("Valor: ").replace(",", ","))
    except ValueError:
        print("Valor inválido")
        return 

    tipo = input("Tipo (cartao/dinheiro): ").strip().lower()
    if tipo not in ("cartao", "dinheiro"):
        print("Tipo inválido.")
        return

    data = input("Data (AAAA-MM-DD) ou enter para hoje: ").strip()
    if data == "":
        data = date.today().isoformat()
    else:
        try:
            datetime.strptime(data, "%Y-%m-%d")
        except ValueError:
            print("Data inválida. Use AAAA-MM-DD.")
            return
    cursor.execute(
        "INSERT INTO transacoes (descricao, valor, tipo, data) VALUES (?, ?, ?, ?)",
        (descricao, valor, tipo, data),
    )
    conn.commit()
    print("Gastos registrado!")