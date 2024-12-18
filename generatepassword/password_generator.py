import random
import string
import pytest
# assert <умова>, <повідомлення> перевіряє умови, кидає помилки
# raise використовується для генерації помилок вручну
# ValueError помилка при неправильному значенні аргументу
def generate_password(length):
    if length <= 0:
        raise ValueError("довжина пароля має бути додатнім цілим числом.")
    if length < 4:
        raise ValueError("довжина пароля має бути не меншою за 4.")

    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    password = random.choices(letters + digits + symbols, k=length)

    return ''.join(password)  # об'єднує елементи списку в один рядок


# тест на довжину пароля
def test_length():
    password = generate_password(8)
    assert len(password) == 8  # перевіряємо, чи має пароль довжину 8


# тест на наявність букв, цифр і спеціальних символів
def test_contains_characters():
    password = generate_password(8)
    assert any(c.isalpha() for c in password)  # перевіряємо, чи є буква
    assert any(c.isdigit() for c in password)  # перевіряємо, чи є цифра
    assert any(c in string.punctuation for c in password)  # перевіряємо, чи є спеціальний символ


# тест на обробку некоректних значень довжини
def test_invalid_length():
    with pytest.raises(ValueError):  # перевіряємо, чи піднімається ValueError
        generate_password(0)  # генеруємо пароль довжиною 0
    with pytest.raises(ValueError):
        generate_password(-5)  # генеруємо пароль довжиною -5