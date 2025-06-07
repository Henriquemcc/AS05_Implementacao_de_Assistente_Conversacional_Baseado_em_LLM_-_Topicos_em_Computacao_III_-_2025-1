import random
import string

def gerar_random_string(length = 10) -> str:
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))