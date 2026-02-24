import random

ASSETS_ALL = [
   
]

ASSETS_OTC = [
    "EUR/USD OTC",
    "GBP/USD OTC",
    "USD/JPY OTC",
    "AUD/NZD OTC",
    "AUD/USD OTC",
    "AUD/CAD OTC",
    "AED/CNY OTC",
    "EUR/NZD OTC",
    "EUR/CHF OTC",
    "EUR/JPY OTC",
    "CAD/JPY OTC",
    "CHF/JPY OTC",
    "GBP/AUD OTC",
    "LBP/USD OTC"
]

def generate_signal(settings):
    assets = ASSETS_OTC
    
    accuracy = 0.85, 0.87, 0.88, 0.89, 0.90, 0.92, 0.95, 0.96, 0.97, 0.98, 0.99, 1.00


    asset = random.choice(assets)
    direction = random.choice(["BUY", "SELL"])
    confidence = confidence = random.choice(accuracy)
    if confidence >= 0.85:
    
        return {
        "asset": asset,
        "direction": direction,
        "expiry time": settings["expiry time"],
        "confidence": confidence
    }
   