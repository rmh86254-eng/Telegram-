from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8698568099:AAGmDSagyfkk3NR9cQiGFRgJXLcG_eyQDjk"
CHANNEL = "@WE_ARE_CYBER_FORCE_BD"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📢 Join Channel", url="https://t.me/WE_ARE_CYBER_FORCE_BD")],
        [InlineKeyboardButton("✅ I Joined", callback_data="check")]
    ]

    await update.message.reply_text(
        "ফাইল পাওয়ার আগে আমাদের চ্যানেলে Join করুন।",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id

    try:
        member = await context.bot.get_chat_member(CHANNEL, user_id)

        if member.status in ["member", "administrator", "creator"]:
            await query.message.reply_document(document=open("file1.zip", "rb"))
            await query.message.reply_document(document=open("file2.pdf", "rb"))
            await query.message.reply_text("✅ সব ফাইল পাঠানো হয়েছে।")
        else:
            await query.message.reply_text("❌ আগে চ্যানেলে Join করুন।")

    except:
        await query.message.reply_text("❌ আগে চ্যানেলে Join করুন।")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(check))

app.run_polling()