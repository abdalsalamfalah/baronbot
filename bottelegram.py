from telegram.ext import Updater, MessageHandler, Filters
updater = Updater(token="1380069836:AAHRT2uobJUW1ckEZn6ghU56JxCMhK2B5lg")
dispatcher = updater.dispatcher
global v


def new_member(bot, update):

    user = update.message.from_user

    update.message.reply_text('اهلا اهلا {} {} '.format(user['first_name'], user['last_name']))


def start(bot, update):
    user = update.message.from_user
    if update.message.text == 'مرحبا':
        v='اهلا وسهلا جميلتنا نورتينا {} اذكري رمز الدخول الي موجود في الرسالة الي دخلتي من خلالها'.format(user['first_name'])
        v = 'اهلا اهلا {} {} '.format(user['first_name'], user['last_name'])

    elif update.message.text == 'اخرس':
        v = 'اهـــا أوكيه'
    elif update.message.text == 'احبك':
        v = 'حبتك زركة'
    elif update.message.text == 'تعال':
        v = 'اصبر وين بأجيك'
    elif update.message.text == 'بوت':
        v = ' مب بوت ياحمار'
    bot.send_message(chat_id=update.message.chat_id,
                     text=v, )

updater.dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, new_member))
start_handler = MessageHandler(Filters.text, start)
dispatcher.add_handler(start_handler)
updater.start_polling()
updater.idle()