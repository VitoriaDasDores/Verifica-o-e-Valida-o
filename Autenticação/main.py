from models.user_system import UserSystem
def main():
    us = UserSystem()

    # Cadastro inicial
    try:
        us.register_user("Alice", "alice@email.com", "alice123")
        print(f"Usuário inicial cadastrado")
    except ValueError as e:
        print(f"Erro no cadastro inicial: {e}")

    print(f"Total de usuários cadastrados: {us.total_users()}")

if __name__ == "__main__":
    main()