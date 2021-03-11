from binance.client import Client
from binance.websockets import BinanceSocketManager
import constants
import talib, numpy

client = Client(constants.BINANCE_API_KEY, constants.BINANCE_API_SECRET)

def get_all():
    msg = ""
    msg += get_info("BTCUSDT") + "\n"
    msg += get_info("ETHUSDT") + "\n"
    msg += get_info("BNBUSDT") + "\n"
    msg += get_info("ADAUSDT") + "\n"
    msg += get_info("DOTUSDT") + "\n"
    msg += get_info("XRPUSDT") + "\n"
    msg += get_info("UNIUSDT") + "\n"
    msg += get_info("LTCUSDT") + "\n"
    msg += get_info("LINKUSDT") + "\n"
    msg += get_info("BCHUSDT") + "\n"
    msg += get_info("XLMUSDT") + "\n"
    msg += get_info("DOGEUSDT") + "\n"
    msg += get_info("XEMUSDT") + "\n"
    msg += get_info("AAVEUSDT") + "\n"
    msg += get_info("LUNAUSDT") + "\n"
    msg += get_info("ATOMUSDT") + "\n"
    msg += get_info("VETUSDT") + "\n"
    msg += get_info("EOSUSDT") + "\n"
    msg += get_info("TRXUSDT") + "\n"

    return msg

def get_info(symbol, str_interval = "8 Hour ago UTC", end_interval=None):
    closes = []

    latest_price = client.get_aggregate_trades(symbol=symbol)[-1]["p"]

    for candle in client.get_historical_klines(symbol, Client.KLINE_INTERVAL_15MINUTE, str_interval,end_interval):
        k_close = float(candle[4])
        closes.append(k_close)

        if len(closes) > 20:
            np_closes = numpy.array(closes)
            rsi = calc_indicators(np_closes)
            return f"{symbol:<8} | RSI: {round(rsi[-1],2)} | ${latest_price}"

def calc_indicators(np_closes):
    return get_rsi(14,np_closes)

def get_rsi(period,candles):
        return talib.RSI(candles, period)