from modulo3.sql_praticas.user_model import UserModel

def display_menu():
    print("\n--- Gerenciador de Usuários ---")
    print("1. Cadastrar novo usuário")
    print("2. Buscar usuário por ID")
    print("3. Atualizar usuário")
    print("4. Deletar usuário")
    print("5. Listar todos os usuários")
    print("6. Sair")
    print("---------------------------------")

def main():
    user_model=UserModel()
    while True:
        display_menu()
        choice= input('Escolha uma opção:')
        
        if choice=='1':
            print('Cadastro de Usuarios')
            senha=input('Senha:')
            email=input('E-mail:')
            user_model.create_user(senha,email)
        
        elif choice =='2':
            print('Buscar Usuários')
            try:
                user_id=int(input('Digite o id do usuário:'))
                user=user_model.find_user_by_id(user_id)
                if user:
                    print('Usuario Encontrado')
                    print(f"ID:{user['id']}")
                    print(f"E-mail:{user['email']}")
                    print(f"Data de Criação:{user['data_criacao']}")
                else:
                    print('Usuario não encontrado')
            except:
                print('ID inválido')
        
        elif choice=='3':
            print('Atualizar Usuario')
            try:
                user_id=int(input('Digite o id do usuário:'))
                print('Deixe em branco os campos que não deseja alterar.')
                senha=input('Nova senha:') or None
                email=input('Novo email:') or None
                user_model.update_user_by_id(user_id,senha,email)
            except ValueError:
                print('ID inválido')
        elif choice=='4':
            print('Deletar Usuário')
            try:
                user_id=int(input('Digite o id do usuário:'))
                user_model.delete_user_by_id(user_id)
            except ValueError:
                print('ID inválido')
        
        elif choice=='5':
            print('Listas de Usuarios')
            users=user_model.get_all_user()
            if users:
                for user in users:
                    
                    print(f"ID:{user['id']}")
                    print(f"E-mail:{user['email']}")
                    print(f"Data de Criação:{user['data_criacao']}")
                print('Fim da lista')
            else:
                print('Nenhum usuários cadastrados')
                
        elif choice =='6':
            print('Saindo do programa')
            break
        else:
            print('Opção inválida')

if __name__=='__main__':
    main()