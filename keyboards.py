from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📊 Get Signal", callback_data="get_signal")],
        [InlineKeyboardButton("⚙️ Configure Settings", callback_data="settings")],
        [InlineKeyboardButton("💳 Payment / Upgrade", callback_data="payment")]
    ])


def settings_menu():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Accuracy", callback_data="set_accuracy"),
            InlineKeyboardButton("Expiration", callback_data="set_time"),
        ],
        [
            InlineKeyboardButton("Payout", callback_data="set_payout"),
            InlineKeyboardButton("Profit", callback_data="set_profit"),
        ],
        [InlineKeyboardButton("Close", callback_data="close_settings")]
    ])

    
def accuracy_options():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("85%", callback_data="accuracy_85%"),
            InlineKeyboardButton("87%", callback_data="accuracy_87%"),
            InlineKeyboardButton("88%", callback_data="accuracy_88%"),
            InlineKeyboardButton("89%", callback_data="accuracy_89%"),
            InlineKeyboardButton("90%", callback_data="accuracy_90%"),
            InlineKeyboardButton("92%", callback_data="accuracy_92%"),
            InlineKeyboardButton("95%", callback_data="accuracy_95%"),
            InlineKeyboardButton("96%", callback_data="accuracy_96%"),
            InlineKeyboardButton("97%", callback_data="accuracy_9"),
            InlineKeyboardButton("98%", callback_data="accuracy_10"),
            InlineKeyboardButton("99%", callback_data="accuracy_11")
        ]
    ])
    
def time_frame():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("M1", callback_data="time_M1"),
            InlineKeyboardButton("M2", callback_data="time_M2"),
            InlineKeyboardButton("M3", callback_data="time_M3"),
        ]
    ])

def payout():
     return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("85%", callback_data="payout_85%"),
            InlineKeyboardButton("88%", callback_data="payout_88%"),
            InlineKeyboardButton("90%", callback_data="payout_90%"),
            InlineKeyboardButton("89%", callback_data="payout_89%"),
            InlineKeyboardButton("92%", callback_data="payout_92%")
        ]
    ])  

def profit():
       return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("$0.85", callback_data="profit_0.85"),
            InlineKeyboardButton("$0.88", callback_data="profit_0.88"),
            InlineKeyboardButton("$0.90", callback_data="profit_0.90"),
            InlineKeyboardButton("$0.92", callback_data="profit_0.92")
        ]
    ])  
