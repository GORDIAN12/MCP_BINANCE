def detect_trend(prices):
    if len(prices) < 5:
        return "neutral"

    last = prices[-5:]

    if all(x < y for x, y in zip(last, last[1:])):
        return "uptrend"
    elif all(x > y for x, y in zip(last, last[1:])):
        return "downtrend"
    
    return "sideways"