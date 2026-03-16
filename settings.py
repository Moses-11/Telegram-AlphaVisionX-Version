DEFAULT_SETTINGS = {
    "assets": "OTC ONLY",
    "accuracy": 0.85,
    "expiry time": "M1",
    "payout": 85,
    "profit": 0.85
}


user_settings = {}

def get_settings(user_id):
    if user_id not in user_settings:
        user_settings[user_id] = DEFAULT_SETTINGS.copy()
    return user_settings[user_id]
    
    

def update_setting(user_id, key, value):
    settings = get_settings(user_id)
    settings[key] = value
    
