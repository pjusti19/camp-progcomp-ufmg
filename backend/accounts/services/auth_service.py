from django.contrib.auth import get_user_model
from common.codeforces.client import handle_exists

User = get_user_model()

class SignupError(Exception):
    pass

def register_user(*, name: str, codeforces_handle: str, email: str, password: str):
    email = email.strip()
    name = name.strip().lower()
    codeforces_handle = codeforces_handle.strip()
    password = password.strip()

    if User.objects.filter(email=email).exists():
        raise SignupError("Email já cadastrado.")

    if User.objects.filter(codeforces_handle=codeforces_handle).exists():
        raise SignupError("Handle do Codeforces já cadastrado.")
    
    if not handle_exists(codeforces_handle):
        raise SignupError("Handle do Codeforces não existe.")
    
    User.objects.create_user(
        email = email,
        first_name = name,
        codeforces_handle = codeforces_handle,
        password = password,
    )
   