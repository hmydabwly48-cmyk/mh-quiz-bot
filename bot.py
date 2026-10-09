import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# إعداد السجلات لمتابعة عمل البوت
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# توكن البوت الخاص بك
TOKEN = "8714224392:AAGPh3n20TappdVNilKqvSV_WsEietYa57c"

def start(update: Update, context: CallbackContext) -> None:
    """إرسال رسالة الترحيب عند بدء استخدام البوت."""
    user = update.effective_user
    welcome_text = (
        f"مرحباً بك يا {user.first_name} في بوت الاختبارات والمسابقات الذكي! 📚\n\n"
        "اختر أحد الخيارات في الأسفل للبدء:"
    )
    
    keyboard = [
        [InlineKeyboardButton("📝 بدء الاختبار", callback_data='start_quiz')],
        [InlineKeyboardButton("ℹ️ حول البوت", callback_data='about')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    update.message.reply_text(welcome_text, reply_markup=reply_markup)

def button_handler(update: Update, context: CallbackContext) -> None:
    """التعامل مع الضغط على الأزرار."""
    query = update.callback_query
    query.answer()
    
    if query.data == 'start_quiz':
        query.edit_message_text(text="جاري تجهيز الأسئلة... قريباً تبدأ المسابقة! 🚀")
    elif query.data == 'about':
        query.edit_message_text(text="هذا البوت مخصص لتقديم اختبارات وتدريبات مساعدة للطلاب. الإصدار التجريبي.")

def main() -> None:
    """تشغيل البوت."""
    updater = Updater(TOKEN)

    # جلب مدير التوزيع لإضافة الأوامر
    dispatcher = updater.dispatcher

    # أوامر البوت
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button_handler))

    # بدء تشغيل البوت
    updater.start_polling()
    print("تم تشغيل البوت بنجاح...")
    
    # البقاء في وضع الاستماع حتى يتم إيقافه يدويياً
    updater.idle()

if __name__ == '__main__':
    main()


