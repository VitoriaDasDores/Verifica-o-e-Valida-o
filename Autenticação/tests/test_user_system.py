import pytest
import time
from models.user_system import UserSystem

@pytest.fixture
def user_system():
    system = UserSystem()
    system.register_user("Admin", "admin@sys.com", "admin123")
    return system

def test_register_valid_user(user_system):
    """CT01: Testa cadastro com dados válidos"""
    user = user_system.register_user("Maria", "maria@mail.com", "maria123")
    assert user_system.total_users() == 2

def test_invalid_email(user_system):
    """CT02: Testa e-mail inválido"""
    with pytest.raises(ValueError, match="E-mail inválido"):
        user_system.register_user("Pedro", "pedro_mail", "pedro123")

def test_weak_password(user_system):
    """CT03: Testa senha fraca (curta)"""
    with pytest.raises(ValueError, match="Senha fraca"):
        user_system.register_user("Carlos", "carlos@mail.com", "abc")

def test_find_existing_user(user_system):
    """CT04: Busca usuário existente"""
    user = user_system.find_user_by_email("admin@sys.com")
    assert user.name == "Admin"

def test_find_non_existing_user(user_system):
    """CT05: Busca usuário inexistente"""
    assert user_system.find_user_by_email("inexistente@mail.com") is None

def test_duplicate_email(user_system):
    """CT06: Testa e-mail duplicado"""
    with pytest.raises(ValueError, match="E-mail já cadastrado"):
        user_system.register_user("Admin2", "admin@sys.com", "senha123")

def test_password_without_numbers(user_system):
    """CT07: Testa senha sem números"""
    with pytest.raises(ValueError, match="Senha fraca"):
        user_system.register_user("Diana", "diana@mail.com", "abcdef")

def test_empty_fields(user_system):
    """CT08: Testa campos vazios"""
    # Teste de nome vazio
    with pytest.raises(ValueError) as e:
        user_system.register_user("", "vazio@mail.com", "senha123")
    assert "nome" in str(e.value).lower() or "obrigatório" in str(e.value).lower()
    
    # Teste de email vazio
    with pytest.raises(ValueError, match="E-mail inválido"):
        user_system.register_user("Nome", "", "senha123")
    
    # Teste de senha vazia
    with pytest.raises(ValueError, match="Senha fraca"):
        user_system.register_user("Nome", "email@mail.com", "")

def test_special_characters_in_name(user_system):
    """CT09: Testa nome com caracteres especiais"""
    user_system.register_user("João Silva", "joao@mail.com", "joao123") 
    user = user_system.find_user_by_email("joao@mail.com")
    assert user.name == "João Silva"

def test_password_min_length(user_system):
    """CT10: Testa senha no limite mínimo (6 caracteres + número)"""
    user_system.register_user("Carla", "carla@mail.com", "abc123")
    assert user_system.find_user_by_email("carla@mail.com") is not None