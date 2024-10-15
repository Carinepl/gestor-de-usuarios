import sqlite3

def criar_conexao():
    conexao = sqlite3.connect(':memory:')
    return conexao

def criar_tabela(conexao):
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')

    conexao.commit()

def inserir_usuario(conexao, nome, email):
    cursor = conexao.cursor()
    cursor.execute('INSERT INTO usuarios (nome, email) VALUES (?, ?)', (nome, email))
    conexao.commit()

    print(f'Usuário {nome} inserido com sucesso!')

def buscar_usuario(conexao, nome):
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE nome = ?', (nome,))
    usuario = cursor.fetchone()

    if usuario:
        print(f'Usuário encontrado: ID: {usuario[0]}, Nome: {usuario[1]}, Email: {usuario[2]}')
    else:
        print('Usuário não encontrado.')

def remover_usuario(conexao, nome):
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM usuarios WHERE nome = ?', (nome,))
    conexao.commit()
    print(f'Usuário {nome} removido com sucesso!')

def atualizar_usuario(conn, nome_antigo, novo_nome, novo_email):
    cursor = conn.cursor()
    cursor.execute('UPDATE usuarios SET nome = ?, email = ? WHERE nome = ?', (novo_nome, novo_email, nome_antigo))
    conn.commit()
    print(f'Usuário {nome_antigo} atualizado para {novo_nome}.')


if __name__ == "__main__":
    conexao = criar_conexao()

    criar_tabela(conexao)

    while True:
        print("\nEscolha uma opção:")
        print("1. Inserir usuário")
        print("2. Buscar usuário")
        print("3. Remover usuário")
        print("4. Atualizar usuário")
        print("5. Sair")

        opcao = input(f"\nDigite o número da opção: ")

        if opcao == '1':
            nome = input("Digite o nome do usuário: ")
            email = input("Digite o email do usuário: ")
            inserir_usuario(conexao, nome, email)
        elif opcao == '2':
            nome = input("Digite o nome do usuário a buscar: ")
            buscar_usuario(conexao, nome)
        elif opcao == '3':
            nome = input("Digite o nome do usuário a remover: ")
            remover_usuario(conexao, nome)
        elif opcao == '4':
            nome_antigo = input("Digite o nome do usuário a atualizar: ")
            novo_nome = input("Digite o novo nome: ")
            novo_email = input("Digite o novo email: ")
            atualizar_usuario(conexao, nome_antigo, novo_nome, novo_email)
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

    conexao.close()
