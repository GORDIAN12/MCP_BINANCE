from tools.price import get_price
from tools.trend import detect_trend
from tools.alerts import check_alert

class CryptoAgent:

    def __init__(self):
        self.history = []

    def run(self):
        price = get_price()

        if self.history:
            prev = self.history[-1]
            change = ((price - prev) / prev) * 100
        else:
            change = 0

        self.history.append(price)

        trend = detect_trend(self.history)
        alert = check_alert(change)

        return {
            "price": price,
            "change": change,
            "trend": trend,
            "alert": alert
        }