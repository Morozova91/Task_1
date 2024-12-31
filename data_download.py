import yfinance as yf

"""
 data_download.py
 Отвечает за загрузку данных об акциях.
Содержит функции для извлечения данных об акциях из интернета и расчёта скользящего среднего."""
# Получает исторические данные об акциях для указанного тикера и временного периода.
# Возвращает DataFrame с данными.
def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data

# Добавляет в DataFrame колонку со скользящим средним, рассчитанным на основе цен закрытия.
def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data
# вычисляет и выводит среднюю цену закрытия акций за заданный период.
def calculate_and_display_average_price(data):
    print(data['Close'].mean(axis=0))