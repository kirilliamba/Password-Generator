import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))

    return password

# Пример использования
password = generate_password(22)  # в скобках указываем длину пароля
# print(f"Сгенерированный пароль: {password}")
