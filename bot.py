import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler

# إعداد السجلات لمتابعة عمل البوت
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# توكن البوت الخاص بك
TOKEN = "8714224392:AAGPh3n20TappdVNilKqvSV_WsEietYa57c"

# دالة رسالة البدء /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    welcome_text = (
        f"أهلاً بك يا {user_name} في بوت الاختبارات التجريبية (كلية الشريعة والقانون)!\n\n"
        "اختر القسم أو المادة التي تريد اختبار نفسك فيها:"
    )
    
    keyboard = [
        [InlineKeyboardButton("📚 اختبار مادة الفقه", callback_data="quiz_fiqh")],
        [InlineKeyboardButton("⚖️ اختبار مادة القانون", callback_data="quiz_law")],
        [InlineKeyboardButton("ℹ️ معلومات عن البوت", callback_data="info")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

# دالة التعامل مع الأزرار والأسئلة
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "quiz_fiqh":
        await query.edit_message_text(
            text="سؤال (1): ما حكم الصلاة خلف المبتدع؟\n\nأ) جائزة مع الكراهة\nب) باطلة\nج) غير صحيحة",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("أ) جائزة مع الكراهة", callback_data="correct")],
                [InlineKeyboardButton("ب) باطلة", callback_data="wrong")],
                [InlineKeyboardButton("ج) غير صحيحة", callback_data="wrong")]
            ])
        )
    elif query.data == "quiz_law":
        await query.edit_message_text(
            text="سؤال (1): ما هو الأساس في العقوبات التعزيرية؟\n\nأ) التوقيف الشرعي\nب) اجتهاد ولي الأمر والقاضي\nج) النص القطعي",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("أ) التوقيف الشرعي", callback_data="wrong")],
                [InlineKeyboardButton("ب) اجتهاد ولي الأمر والقاضي", callback_data="correct")],
                [InlineKeyboardButton("ج) النص القطعي", callback_data="wrong")]
            ])
        )
    elif query.data == "correct":
        await query.edit_message_text(text="✅ إجابتك صحيحة أحسنت! /start للعودة للقائمة الرئيسية.")
    elif query.data == "wrong":
        await query.edit_message_text(text="❌ إجابة خاطئة. حاول مرة أخرى عبر إرسال /start.")
    elif query.data == "info":
        await query.edit_message_text(text="هذا بوت تجريبي لخدمة طلاب كلية الشريعة والقانون. /start للعودة.")

def main():
    # بناء وتشغيل تطبيق البوت
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))

    print("البوت يعمل الان...")
    application.run_polling()

if __name__ == '__main__':
    main()

