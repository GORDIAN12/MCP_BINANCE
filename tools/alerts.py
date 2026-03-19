def check_alert(change, threshold=0.5):
    if abs(change) >= threshold:
        return "ALERTA: movimiento fuerte"
    return None