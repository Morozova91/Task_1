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

    # График RSI
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['RSI'], label='RSI', color='blue')
    plt.axhline(70, linestyle='--', alpha=0.5, color='red')
    plt.axhline(30, linestyle='--', alpha=0.5, color='green')
    plt.title(f"RSI для {ticker}")
    plt.xlabel("Дата")
    plt.ylabel("RSI")
    plt.legend()
    plt.savefig(f"{ticker}_{period}_RSI_chart.png")

    plt.figure(figsize=(14, 7))

    # График цен
    plt.subplot(2, 1, 1)
    plt.plot(data['Close'], label='Close Price', color='blue')
    plt.title(f'{ticker} Price Chart')
    plt.legend()

    # График MACD
    plt.subplot(2, 1, 2)
    plt.plot(data['MACD'], label='MACD', color='green')
    plt.plot(data['Signal'], label='Signal Line', color='red')
    plt.title('MACD Indicator')
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.legend()

    plt.tight_layout()
    plt.show()


    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")

def export_to_csv(data, filename):
    """
        Экспортирует данные в CSV файл.

        :param data: DataFrame, содержащий данные об акциях
        :param filename: str, имя файла для сохранения
        """
    try:
        # Сохраняем DataFrame в CSV файл
        data.to_csv(filename, index=False)
        print(f"Данные успешно экспортированы в файл: {filename}")
    except Exception as e:
        print(f"Произошла ошибка при экспорте данных: {e}")


