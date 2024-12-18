# Опис
# Розробіть Python-додаток на основі Flask, який реалізує сервер для магазину 3D друку. Сервер має обробляти запити на обчислення вартості друку завантаженої 3D моделі.
# Ціна залежить від ваги моделі та регіону користувача, який визначається з HTTP-заголовків. Сервер повинен приймати файл у форматі STL, аналізувати його, визначати вагу моделі та обчислювати ціну залежно
# від регіону користувача.
#
# Вимоги
# Flask сервер:
# - Використайте бібліотеку Flask для створення сервера.
# - Реалізуйте ендпоінт POST /calculate-price, який приймає файл STL та повертає розраховану ціну.
#
# Розрахунок ваги моделі:
# - Використайте бібліотеку numpy-stl для читання файлу STL та визначення об'єму моделі.
# Обчисліть вагу моделі, враховуючи матеріал з щільністю:
# - PLA: 1.25 г/см³
# - ABS: 1.05 г/см³
# - PETG: 1.38 г/см³
#
# Розрахунок ціни:
# Ціна залежить від ваги моделі та регіону користувача:
# - EU (Європа): $0.05 за грам
# - US (США): $0.07 за грам
# - UA (Україна): $0.03 за грам
#
# - Якщо регіон не визначений, використовуйте ціну за замовчуванням: $0.06 за грам.
# - Визначайте регіон користувача з HTTP-заголовка X-Region.
#
# Обробка помилок:
# - Якщо файл не завантажено або має некоректний формат, поверніть помилку 400 Bad Request.
# - Якщо заголовок X-Region відсутній або має некоректне значення, поверніть помилку 400 Bad Request з повідомленням "Invalid region header."
# - Якщо файл STL пошкоджений або не може бути прочитаний, поверніть помилку 500 Internal Server Error.

from flask import Flask, request, jsonify
from stl import mesh
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

DENSITIES = {
    "PLA": 1.25,
    "ABS": 1.05,
    "PETG": 1.38
}

REGION_PRICES = {
    "EU": 0.05,
    "US": 0.07,
    "UA": 0.03,
    "DEFAULT": 0.06
}


def calculate_model_weight(volume, material_density):
    return volume * material_density # об'єм * щільність


def calculate_price(weight, region):
    price_per_gram = REGION_PRICES.get(region, REGION_PRICES["DEFAULT"])
    return weight * price_per_gram  # вага * вартість друку


@app.route('/calculate-price', methods=['POST'])
def calculate_price_endpoint():
    if 'file' not in request.files:
        return jsonify({"error": "no file provided"}), 400

    stl_file = request.files['file']
    region = request.headers.get('X-Region')
    material = request.form.get('material')
    if region not in REGION_PRICES and region != "DEFAULT":
        return jsonify({"error": "invalid region"}), 400

    try:
        temp_dir = './temp'  # Вказує шлях до тимчасової папки.
        os.makedirs(temp_dir, exist_ok=True)  # Створює папку, якщо вона не існує.
        filename = secure_filename(stl_file.filename)  # Робить ім'я файлу безпечним.
        filepath = os.path.join(temp_dir, filename)  # Формує повний шлях до файлу.
        stl_file.save(filepath)  # Зберігає файл STL за цим шляхом.

        stl_mesh = mesh.Mesh.from_file(filepath)  # Завантажує STL файл у mesh-об'єкт.
        volume = stl_mesh.get_mass_properties()[0]  # Обчислює об'єм моделі (см³).

        os.remove(filepath)  # Видаляє тимчасовий файл.

        material_density = DENSITIES[material]  # Отримує щільність вибраного матеріалу.
        weight = calculate_model_weight(volume, material_density)  # Обчислює вагу моделі.
        price = calculate_price(weight, region)  # Обчислює ціну друку моделі.

        return jsonify({"weight": round(weight, 2), "price": round(price, 2)}), 200
    except Exception as e:
        print(f"error: {e}")
        return jsonify({"error": "fail"}), 500


if __name__ == '__main__':
    app.run(debug=True)
