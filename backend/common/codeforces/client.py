import requests
import logging

logger = logging.getLogger(__name__)

BASE_URL = f"https://codeforces.com/api"
DEFAULT_TIMEOUT = 10

USER_INFO = "user.info"

class CodeforcesAPIError(Exception):
    pass

class HandleNotFoundError(Exception):
    pass

def _call(method: str, params: dict | None = None):
    url = f"{BASE_URL}/{method}"
    try:
        response = requests.get(url, params=params or {}, timeout=DEFAULT_TIMEOUT)
    except requests.RequestException as e:
        raise CodeforcesAPIError(f"Falha ao conectar na API do Codeforces: {e}") from e
    
    data = response.json()
    
    if data.get("status") != "OK":
        comment = data.get("comment", "Erro na API do Codeforces")
        if "not found" in comment.lower():
            raise HandleNotFoundError(comment)
        raise CodeforcesAPIError(comment)
    
    return data["result"]

def handle_exists(handle: str) -> bool:
    try:
        users = _call(USER_INFO, {"handles": handle})
        return len(users) > 0
    except HandleNotFoundError as e:
        logger.warning("%s", e)
        return False