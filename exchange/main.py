import requests

def get_exchange_rates():
    url = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
    response = requests.get(url)
    return response.json()


def main():
    print("Доступні валюти: USD, EUR, UAH")

    base_currency = input("Введіть базову валюту (наприклад, USD): ").upper()
    target_currency = input("Введіть валюту обміну (наприклад, EUR): ").upper()
    amount = float(input("Введіть суму для конвертації: "))

    rates = get_exchange_rates()
    print(rates)
    base_rate = 1.0
    target_rate = 1.0
    for rate in rates:
        if rate["ccy"] == base_currency:
            base_rate = float(rate["sale"])
        if rate["ccy"] == target_currency:
            target_rate = float(rate["sale"])

    if base_currency == "UAH":
        base_rate = 1.0
    if target_currency == "UAH":
        target_rate = 1.0

    result = (amount * base_rate) / target_rate
    print(f"{amount} {base_currency} = {round(result, 2)} {target_currency}")


if __name__ == "__main__":
    main()
