import sqlite3
from datetime import datetime
from modulo3.sql_praticas.database import DatabaseConnection


class UserModel:
    """Gerencia a tabela 'usuarios' e todas as operações de CRUD."""

    def __init__(self):
        self.db_conn = DatabaseConnection()
        self._create_table()

    def _create_table(self):
        """Método privado para criar a tabela de usuários."""
        self.db_conn.connect()
        self.db_conn.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                senha TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
                data_atualizacao DATETIME DEFAULT CURRENT_TIMESTAMP
            );
        """
        )
        self.db_conn.close()

    def create_user(self, senha, email):
        """Cria um novo usuário."""
        self.db_conn.connect()
        try:
            self.db_conn.cursor.execute(
                """
                INSERT INTO usuarios (senha, email)
                VALUES (?, ?);
            """,
                (senha, email),
            )
            print("Usuário criado com sucesso!")
        except sqlite3.IntegrityError:
            print(f"Erro: O e-mail '{email}' já está em uso.")
        finally:
            self.db_conn.close()

    def find_user_by_id(self, user_id):
        """Busca um usuário pelo ID."""
        self.db_conn.connect()
        self.db_conn.cursor.execute("SELECT * FROM usuarios WHERE id = ?;", (user_id,))
        user = self.db_conn.cursor.fetchone()
        self.db_conn.close()
        return user

    def update_user_by_id(self, user_id, senha=None, email=None):
        """Atualiza informações de um usuário pelo ID."""
        self.db_conn.connect()
        updates = []
        params = []
        if senha:
            updates.append("senha = ?")
            params.append(senha)
        if email:
            updates.append("email = ?")
            params.append(email)

        if not updates:
            print("Nenhum dado para atualizar.")
            self.db_conn.close()
            return

        updates.append("data_atualizacao = ?")
        params.append(datetime.now())
        params.append(user_id)
        query = f"UPDATE usuarios SET {', '.join(updates)} WHERE id = ?;"

        self.db_conn.cursor.execute(query, params)
        print("Usuário atualizado com sucesso!")
        self.db_conn.close()

    def delete_user_by_id(self, user_id):
        """Deleta um usuário pelo ID."""
        self.db_conn.connect()
        self.db_conn.cursor.execute("DELETE FROM usuarios WHERE id = ?;", (user_id,))
        print("Usuário deletado com sucesso!")
        self.db_conn.close()

    def get_all_users(self):
        """Retorna todos os usuários."""
        self.db_conn.connect()
        self.db_conn.cursor.execute("SELECT * FROM usuarios;")
        users = self.db_conn.cursor.fetchall()
        self.db_conn.close()
        return users
    
class BlogModel:
    def __init__(self):
        self.db_conn = DatabaseConnection()
        self._create_table()

    def _create_table(self):
        """Método privado para criar a tabela de usuários."""
        self.db_conn.connect()
        self.db_conn.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS blog (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL UNIQUE,
                conteudo TEXT NOT NULL,
                data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
                data_atualizacao DATETIME DEFAULT CURRENT_TIMESTAMP,
                id_usuario INTEGER,
                Foreign Key (id_usuario) REFERENCES usuarios(id)
            );
        """
        )
        self.db_conn.close()
    def create_user(self, titulo, conteudo):
        """Cria um novo usuário."""
        self.db_conn.connect()
        try:
            self.db_conn.cursor.execute(
                """
                INSERT INTO usuarios (titulo, conteudo)
                VALUES (?, ?);
            """,
                (titulo, conteudo),
            )
            print("Conteúdo criado com sucesso!")
        except sqlite3.IntegrityError:
            print(f"Erro: O título '{titulo}' já está em uso.")
        finally:
            self.db_conn.close()

    def find_user_by_id(self, user_id):
        """Busca um usuário pelo ID."""
        self.db_conn.connect()
        self.db_conn.cursor.execute("SELECT * FROM usuarios WHERE id = ?;", (user_id,))
        user = self.db_conn.cursor.fetchone()
        self.db_conn.close()
        return user

    def update_user_by_id(self, user_id, titulo=None, conteudo=None):
        """Atualiza informações de um usuário pelo ID."""
        self.db_conn.connect()
        updates = []
        params = []
        if titulo:
            updates.append("titulo = ?")
            params.append(titulo)
        if conteudo:
            updates.append("conteudo = ?")
            params.append(conteudo)

        if not updates:
            print("Nenhum dado para atualizar.")
            self.db_conn.close()
            return

        updates.append("data_atualizacao = ?")
        params.append(datetime.now())
        params.append(user_id)
        query = f"UPDATE usuarios SET {', '.join(updates)} WHERE id = ?;"

        self.db_conn.cursor.execute(query, params)
        print("Usuário atualizado com sucesso!")
        self.db_conn.close()
        
    def delete_user_by_id(self, user_id):
        """Deleta um usuário pelo ID."""
        self.db_conn.connect()
        self.db_conn.cursor.execute("DELETE FROM usuarios WHERE id = ?;", (user_id,))
        print("Usuário deletado com sucesso!")
        self.db_conn.close()
