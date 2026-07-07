import requests

BASE_URL = f"https://codeforces.com/api"
DEFAULT_TIMEOUT = 10

USER_INFO = "user.info"

class CodeforcesAPIError:
    pass

def _call(method: str, params: dict | None = None):
    url = f"{BASE_URL}/{method}"
    response = requests.get(url, params = params or {}, timeout = DEFAULT_TIMEOUT)
    response.raise_for_status() 
    
    data = response.json()
    
    if data.get("status") != "OK":
        raise CodeforcesAPIError(data.get("comment", "Erro na API do Codeforces"))
    
    return data["result"]

def get_user_info(handle: str) -> dict:
    return _call(USER_INFO, {"handles": handle})

def handle_exists(handle: str) -> bool:
    try:
        users = get_user_info(handle)
        return len(users) > 0
    except CodeforcesAPIError:
        return False