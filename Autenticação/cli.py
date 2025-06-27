from models.user_system import UserSystem

def main():
    system = UserSystem()
    print("\n=== Sistema de Cadastro de Usuários ===")
    
    while True:
        print("\nOpções:")
        print("1. Cadastrar novo usuário")
        print("2. Buscar usuário por e-mail")
        print("3. Ver total de usuários")
        print("4. Sair")
        
        choice = input("Escolha uma opção: ")
        
        if choice == "1":
            print("\n--- Novo Cadastro ---")
            name = input("Nome: ").strip()
            email = input("E-mail: ").strip()
            password = input("Senha (min 6 caracteres com número): ").strip()
            
            try:
                user = system.register_user(name, email, password)
                print(f"\n Usuário cadastrado com sucesso! ID: {id(user)}")
            except ValueError as e:
                print(f"\n Erro: {e}")
        
        elif choice == "2":
            print("\n--- Buscar Usuário ---")
            email = input("Digite o e-mail: ").strip()
            user = system.find_user_by_email(email)
            
            if user:
                print(f"\nUsuário encontrado:")
                print(f"Nome: {user.name}")
                print(f"E-mail: {user.email}")
            else:
                print("\n Usuário não encontrado")
        
        elif choice == "3":
            print(f"\nTotal de usuários cadastrados: {system.total_users()}")
        
        elif choice == "4":
            print("\nSaindo do sistema...")
            break
        
        else:
            print("\n Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()