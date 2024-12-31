import yfinance as yf


"""
 data_download.py
 Отвечает за загрузку данных об акциях.
Содержит функции для извлечения данных об акциях из интернета и расчёта скользящего среднего.
Получает исторические данные об акциях для указанного тикера и временного периода.
Возвращает DataFrame с данными."""
def fetch_stock_data(ticker, period):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data

"""Добавляет в DataFrame колонку со скользящим средним, рассчитанным на основе цен закрытия."""
def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data

"""вычисляет и выводит среднюю цену закрытия акций за заданный период."""
def calculate_and_display_average_price(data):
    print(data['Close'].mean(axis=0))

"""анализирует данные и уведомляет пользователя, 
если цена акций колебалась более чем на заданный процент за период.
Функция будет вычислять максимальное и минимальное значения цены закрытия и сравнивать разницу с заданным порогом. 
Если разница превышает порог, пользователь получает уведомление."""
def notify_if_strong_fluctuations(data, threshold=20):

    min_price = data['Close'].min()
    max_price = data['Close'].max()
    price_change = ((max_price - min_price) / min_price) * 100

    # Уведомляем пользователя, если колебания превышают порог
    if price_change > threshold:
        print(f"Уведомление: Колебания цены акций составили {price_change:.2f}%, что превышает порог в {threshold}%.")
    else:
        print(f"Колебания цены акций составили {price_change:.2f}%, что не превышает порог в {threshold}%.")

"""Вычисление MACD
    MACD (Moving Average Convergence Divergence) — это технический индикатор, позволяющий оценивать силу тренда и построенный 
    с учетом усредненного изменения цены.
    Вычисляет индикатор MACD и сигнальную линию на основе цен закрытия.

    Параметры:
    data (DataFrame): Данные о ценах акций, должен содержать колонку 'Close'.
    short_window (int): Период для короткой экспоненциальной скользящей средней (по умолчанию 12).
    long_window (int): Период для длинной экспоненциальной скользящей средней (по умолчанию 26).
    signal_window (int): Период для сигнальной линии (по умолчанию 9)."""

def compute_macd(data, short_window=12, long_window=26, signal_window=9):
    # Вычисляем короткую и длинную экспоненциальные скользящие средние
    data['EMA_sw'] = data['Close'].ewm(span=short_window, adjust=False).mean()
    data['EMA_lw'] = data['Close'].ewm(span=long_window, adjust=False).mean()

    # MACD
    data['MACD'] = data['EMA_sw'] - data['EMA_lw']
    # Сигнальная линия
    data['Signal'] = data['MACD'].ewm(span=signal_window, adjust=False).mean()

    return data
"""Вычисление RSI
    RSI ((Relative Strength Index, RSI)- индекс технического анализа, определяющий силу тренда и вероятность его смены.
        Рассчитывает индекс относительной силы (RSI) на основе цен закрытия.

    Параметры:
    data (DataFrame): Данные о ценах акций, должен содержать колонку 'Close'.
    period (int): Период для расчета RSI (по умолчанию 14)."""
def calculate_rsi(data, period=14):
    # Рассчитываем изменения цен
    delta = data['Close'].diff()

    # Отделяем прибыли и убытки
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()

    # Рассчитываем относительную силу (RS)
    rs = gain / loss

    # Рассчитываем RSI
    data['RSI'] = 100 - (100 / (1 + rs))

    return data






