from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler,
    CallbackQueryHandler, ContextTypes, CallbackContext
    )

from settings import get_settings, update_setting, user_settings
from signal_engine import generate_signal
from payment import can_get_signal, record_signal, remaining_signals
from keyboards import main_menu, settings_menu, accuracy_options, time_frame, payout, profit
from datetime import datetime, timedelta
import logging
import random
import string

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger()

BOT_TOKEN = "8543415296:AAGRyPJG-B7XislNs_RrDwtTdtP_ilWMKxc"

access_keys = {
    "AVX-9F3K-Q2LM-30D": {
        "days": 30,
        "used": False
    }
}

users = {
    6727753819: {
        "free_used": 20,
        "is_subscribed": True,
        "expires_at": "2026-02-25"
    }
}

def generate_key(days: int):
    part1 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    part2 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return f"AVX-{part1}-{part2}-{days}D"

async def genkey(update, context):
    ADMIN_IDS = [6727753819]  # your Telegram ID
    
    days = 30
 
    key = generate_key(days)

    access_keys[key] = {
        "days": days,
        "used": False
    }

    await update.message.reply_text(
        f"✅ Access Key Generated:\n\n"
        f"{key}\n\n"
        f"Activation link:\n"
        f"/activate {key}",
        parse_mode="Markdown"
    )
    

    user_id = update.effective_user.id

    if user_id != ADMIN_IDS:
        await update.message.reply_text("⛔ You are not authorized.")
        return

    elif user_id == ADMIN_IDS:
        await update.message.reply_text("Usage: /genkey <days>")
        return

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("genkey", genkey))
    
async def activate(update, context):
    ADMIN_IDS = [6727753819]
    user_id = update.effective_user.id
    
    users[user_id] = {
        "free_used": users.get(user_id, {}).get("free_used", 0),
        "is_subscribed": True,
        "expires_at": expiry
    }

    key_data["used"] = True

    if user_id != ADMIN_IDS:
        await update.message.reply_text("❌ Usage: /activate <ACCESS_KEY>")
        return

    key = context.args[0]
    key_data = access_keys.get(key)

    if key != key_data:
        await update.message.reply_text("❌ Invalid access key.")
        return
    else:
        await update.message.reply_text(
        f"✅ Subscription activated!\n"
        f"📅 Expires on: {expiry.date()}"
    )
    if key_data["used"]:
        await update.message.reply_text("❌ This key has already been used.")
        return

    expiry = datetime.now() + timedelta(days=key_data["days"])

    
async def has_access(user_id):
    user = users.get(user_id)

    if not user:
        return True  # new users get free access

    if user.get("is_subscribed"):
        if datetime.now() < user["expires_at"]:
            return True
        else:
            user["is_subscribed"] = False  # auto-expire

    return user.get("free_used", 0) < 20





async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    settings = get_settings(user_id)

    text = (
        "📈 Welcome to AlphaVisionX™️\n" 
        "🏦AlphaVisionX is a Pocket Option-Broker Signal Bot! The Best OTC Market Analysis Tool\n\n"
        "🈚Enjoy 10 FREE Testing signals!\n"
        "⏫Upgrade to access UNLIMITED Signals!\n\n"
        "⚙️Your current settings:\n\n"
        f"Asset Type: {settings['assets']}\n"
        f"Minimum Accuracy: {settings['accuracy']}\n"
        f"Expiration: {settings['expiry time']}\n"
        f"Payout: {settings['payout']}\n"
        f"Profit: ${settings['profit']}\n\n"
    )

    await update.message.reply_text(
        text,
        parse_mode="Markdown",
        reply_markup=main_menu()
    )

async def my_settings(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start(update, context)

async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🛑 Bot stopped.")


async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    data = query.data
    
    if user_id not in user_settings:
        user_settings[user_id] = {}
        
    
    if data == "get_signal":
        if not can_get_signal(user_id):
            await query.message.reply_text("❌ Free signals exhausted. Upgrade required.")
            return

        signal = generate_signal(get_settings(user_id))
        record_signal(user_id)

        await query.message.reply_text(
            f"📊 AlphaVisionX Signal\n\n"
            f"Currency Pair: {signal['asset']}\n"
            f"Direction: {signal['direction']}\n"
            f"Expiry: {signal['expiry time']}\n"
            f"Confidence/Accuracy: {signal['confidence']}\n\n"
            f"🟠Free signals left: {remaining_signals(user_id)}",
            parse_mode="Markdown",
            reply_markup=main_menu()
        )
        
    elif data == "payment":
        await query.message.reply_text(
            "UPGRADE TO ACCESS UNLIMITED SIGNALS!!\n"
            "🔶1 Month / $8\n"
            "🔶3 Months / $15\n"
            "🔶1 Year / $60\n\n"
            "💳 Pay using any of the options below: \n\n"
            "💰CRYPTO DEPOSITS ONLY!🪙\n"
            "USDT(Tether TRC-20): TNCx1T85prqHHTcPDgqm8tBMdLjjvGfGSf\n\n"
            "Binance Smart Chain (BEP-20): 0xb63c0270b7c9b657413009a7859f31abcfca5f15\n\n"
            "Bitcoin: 12teRe5nKjfK3wfySScrwasKuBAxESrvAc\n\n"
            "After you pay, contact me through Telegram with payment screenshot for the access key, my username is @trader11",
            reply_markup=main_menu()
        )

    elif data == "settings":
        await query.message.reply_text(
            "⚙️ Configure the Signal bot settings:",
            reply_markup=settings_menu()
        )

        
    elif data == "set_accuracy":
        await query.message.reply_text(
            "accuracy",
            reply_markup=accuracy_options()
        )
        
    elif data == "set_time":
        await query.message.reply_text(
            "expiration",
            reply_markup=time_frame()
        )
    
    elif data == "set_payout":
        await query.message.reply_text(
            "payout",
            reply_markup=payout()
        )
        
    elif data == "set_profit":
        await query.message.reply_text(
            "profit",
            reply_markup=profit()
        )
        
        
    elif data.startswith("profit_"):
        value = float(data.split("_")[1])
        update_setting(user_id, "profit", value)
        await query.message.reply_text(
            f"✅ For each $1 trade opened, you will make ${value}",
            reply_markup=settings_menu()
        )
        
    elif data.startswith("payout_"):
        value = str(data.split("_")[1])
        update_setting(user_id, "payout", value)
        await query.message.reply_text(
            f"✅ Payout set to {value}",
            reply_markup=settings_menu()
        )
        
    elif data.startswith("time_"):
        value = str(data.split("_")[1])
        update_setting(user_id, "expiry time", value)
        await query.message.reply_text(
            f"✅ Expiry time set to {value}",
            reply_markup=settings_menu()
        )
        
    elif data.startswith("accuracy_"):
        value = str(data.split("_")[1])
        update_setting(user_id, "accuracy", value)
        await query.message.reply_text(
            f"✅ Accuracy set to {value}",
            reply_markup=settings_menu()
        )
            
            
    elif data == "close_settings":
        await query.message.reply_text(
            "Settings closed.",
            reply_markup=main_menu()
        )
        

def main():
    print("🚀 AlphaVisionX Bot started...")
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("stop", stop))
    app.add_handler(CommandHandler("my_settings", my_settings))
    app.add_handler(CallbackQueryHandler(handle_buttons))

    app.run_polling()
main()
 
