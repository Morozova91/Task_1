import matplotlib.pyplot as plt
import pandas as pd

"""
data_plotting.py
Отвечает за визуализацию данных.
Содержит функции для создания и сохранения графиков цен закрытия и скользящих средних."""
"""
    Создание и сохранение графика цен акций с скользящей средней.
    Параметры:
    - data: DataFrame, содержащий данные о ценах акций с колонками 'Close' и 'Moving_Average'.
    - ticker: Тикер акции для заголовка.
    - period: Период времени для графика (используется в имени файла).
    - filename: Необязательный; если указан, график будет сохранен с этим именем.
    """
def create_and_save_plot(data, ticker, period, filename=None):
    plt.figure(figsize=(10, 6))

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')

    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()

    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")