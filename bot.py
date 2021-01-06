import unicodedata
from telegram.ext import Updater, MessageHandler, Filters
updater = Updater(token="1380069836:AAFVmcmtdpaCnLKGvlbq20gg_VXrZdvNQWM")
dispatcher = updater.dispatcher
global v

def new_user(update, context):
    user = update.message.from_user

    update.message.reply_text(' اهلا وسهلا نورت/ي قروبنا حياك الله ️ {} {} '.format(user['first_name'], user['last_name']))

    update.message.reply_text(' اهلا وسهلا نورت/ي قروبنا حياك الله{} {} '.format(user['first_name'], user['last_name']))
def start(bot, update):
    user = update.message.from_user
    if update.message.text == 'مرحبا':
        v='ياهـــــلا والله'.format(user['first_name'])
       # v = 'اهلا اهلا {} {} '.format(user['first_name'], user['last_name'])


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

updater.dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, new_user))
# updater.dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, new_member))
start_handler = MessageHandler(Filters.text, start)
dispatcher.add_handler(start_handler)
updater.start_polling()
updater.idle()
