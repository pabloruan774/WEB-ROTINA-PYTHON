import sqlite3

def criar_banco():
    conn = sqlite3.connect('sistema_rotina.db')
    cursor = conn.cursor()

    # Tabela para o Projeto Bulking (Rumo aos 57kg)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS progresso_peso (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT,
            peso REAL
        )
    ''')

    # Tabela para os cuidados com o Eren
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cuidados_eren (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT,
            atividade TEXT
        )
    ''')

    conn.commit()
    conn.close()
    print("Banco de dados configurado com sucesso!")

if __name__ == "__main__":
    criar_banco()