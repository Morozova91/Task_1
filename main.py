

import data_download as dd
import data_plotting as dplt
import os

"""Является точкой входа в программу.

Запрашивает у пользователя тикер акции и временной период,
загружает данные, обрабатывает их и выводит результаты в виде графика."""

def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
    period = input("Введите период для данных (например, '1mo' для одного месяца): ")

    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, period)

    # Add moving average to the data, RSI, MACD
    stock_data = dd.add_moving_average(stock_data)
    stock_data = dd.calculate_rsi(stock_data)
    stock_data = dd.compute_macd(stock_data)
    print(stock_data)

    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, period)
    dd.calculate_and_display_average_price(stock_data)

    # Notification of strong fluctuations
    if dd.notify_if_strong_fluctuations(stock_data, threshold=20) is not None:
        print(dd.notify_if_strong_fluctuations(stock_data, threshold=20))

    # Export_to_csv
    dplt.export_to_csv(stock_data, f'{ticker}_{period}')



if __name__ == "__main__":
    main()