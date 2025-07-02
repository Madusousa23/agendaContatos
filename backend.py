from database import conectar

def adicionar_contato(nome, telefone, email):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO contatos(nome, telefone, email)
        VALUES (?,?,?)
    """,(nome,telefone,email))

    conn.commit()
    conn.close()