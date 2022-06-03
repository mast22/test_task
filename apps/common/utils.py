import random
import string


def random_string(n=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))


def random_email():
    return f"{random_string()}@{random_string()}.com"
