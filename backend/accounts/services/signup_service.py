from django.contrib.auth import get_user_model

User = get_user_model()

class SignupError(Exception):
    pass

def register_user(*, name: str, codeforces_handle: str, email: str, password: str):
    email = email.strip()
    name = name.strip().lower()
    codeforces_handle = codeforces_handle.strip()
    password = password.strip()
    
    if not email or not name or not codeforces_handle or not password:
        raise SignupError("Preencha todos os campos.")
    
    if User.objects.filter(email=email).exists():
        raise SignupError("Email já cadastrado.")
    
    if not validateHandle(codeforces_handle):
        raise SignupError("Handle do Codeforces inválido.")
    
    return User.objects.create_user(
        email = email,
        first_name = name,
        codeforces_handle = codeforces_handle,
        password = password,
    )