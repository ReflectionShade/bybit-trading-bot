# bot.py

import time
import requests
from bybit import Client
from config import API_KEY, API_SECRET

# Инициализация клиента Bybit
client = Client(API_KEY, API_SECRET)

# Функция для получения баланса
def get_balance():
    try:
        balance = client.get_wallet_balance()
        print(f"Баланс: {balance}")
        return balance
    except Exception as e:
        print(f"Ошибка при получении баланса: {e}")
        return None

# Функция для получения данных о рынке
def get_market_data(symbol):
    try:
        market_data = client.get_symbol_info(symbol)
        print(f"Данные о рынке: {market_data}")
        return market_data
    except Exception as e:
        print(f"Ошибка при получении данных о рынке: {e}")
        return None

# Пример функции для выполнения ордера
def place_order(symbol, qty, side, order_type="Market"):
    try:
        order = client.place_active_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            qty=qty,
            time_in_force="GoodTillCancel"
        )
        print(f"Ордер размещен: {order}")
    except Exception as e:
        print(f"Ошибка при размещении ордера: {e}")

# Пример торговой стратегии (Smart Money)
def smart_money_strategy(symbol):
    # Получаем данные о рынке
    market_data = get_market_data(symbol)
    if market_data is None:
        return

    # Пример принятия торгового решения (условия стратегии Smart Money)
    if market_data['last_price'] < 50000:
        print("Цена ниже 50000, открываем ордер на покупку")
        place_order(symbol, 1, "Buy")
    elif market_data['last_price'] > 60000:
        print("Цена выше 60000, открываем ордер на продажу")
        place_order(symbol, 1, "Sell")

# Главный цикл бота
def main():
    symbol = "BTCUSDT"  # Торговая пара
    while True:
        print("Запуск стратегии Smart Money...")
        smart_money_strategy(symbol)
        time.sleep(10)  # Пауза в 10 секунд между выполнениями стратегии

if __name__ == "__main__":
    main()
