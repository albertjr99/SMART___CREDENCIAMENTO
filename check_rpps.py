import sqlite3

conn = sqlite3.connect('credenciamento.db')
c = conn.cursor()

print("=== RPPS cadastrados ===")
c.execute("SELECT id, name, role, cpf_cnpj FROM users WHERE role='rpps'")
rpps = c.fetchall()
for r in rpps:
    print(f"ID: {r[0]}, Nome: {r[1]}, Role: {r[2]}, CNPJ: {r[3]}")

if not rpps:
    print("Nenhum RPPS encontrado!")

print("\n=== Todos os usuários ===")
c.execute("SELECT id, name, role FROM users")
for r in c.fetchall():
    print(f"ID: {r[0]}, Nome: {r[1]}, Role: {r[2]}")

conn.close()
