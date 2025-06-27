from models.user import User

class UserSystem:
    """
    Sistema de gerenciamento de usuários.
    Permite cadastro, busca e contagem de usuários.
    """

    def __init__(self):
        self.users = []

    def register_user(self, name, email, password):
        """
        Cadastra um novo usuário após validações.
        """

        # Validação de nome vazio
        if not name.strip():
            raise ValueError("Nome não pode ser vazio")
        
        # Validação de e-mail duplicado (case-insensitive)
        if any(user.email.lower() == email.lower() for user in self.users):
            raise ValueError("E-mail já cadastrado")
        
        user = User(name, email, password)

        if not user.is_valid_email():
            raise ValueError("E-mail inválido.")

        if not user.is_strong_password():
            raise ValueError("Senha fraca.")

        self.users.append(user)
        return user

    def find_user_by_email(self, email):
        """
        Procura um usuário pelo e-mail (case-insensitive).
        """
        email_lower = email.lower()
        for user in self.users:
            if user.email.lower() == email_lower:
                return user
        return None

    def total_users(self):
        """
        Retorna o total de usuários cadastrados.
        """
        return len(self.users)