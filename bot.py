﻿from telegram.ext import Updater, MessageHandler, Filters
import random

updater = Updater(token="1380069836:AAFVmcmtdpaCnLKGvlbq20gg_VXrZdvNQWM")
dispatcher = updater.dispatcher
global v


def new_member(bot, update):
    user = update.message.from_user

    update.message.reply_text('[اهلا وسهلا نورت/ي قروبنا حياك الله 😍❤️  {} {}  اطلع/ي على الرسالة المثبتة 🌹'.format(user['first_name'], user['last_name']))



def start(bot, update):
    user = update.message.from_user
    if update.message.text == 'مرحبا':
        if(str(user['last_name'])=='None'):
            vv=user['last_name']
            vv=''
            v = 'يا مرحبا فيك 😍 🌹{} {} '.format(user['first_name'],vv)
        else:
            v = 'يا مرحبا فيك 😍 🌹{} {} '.format(user['first_name'],user['last_name'])
    elif update.message.text == 'اهلا':
        v = 'يا اهلا وسهلا فيك 😍 تفضل/ي ؟ 🌹'
    elif update.message.text == 'اخرس':
        v = 'اشكرك'
    elif update.message.text == 'كم الاسعار':
        v = 'اطلع/ي على الرسالة المثبتة فيها كل التفاصيل 😍👆'
    elif update.message.text == 'الاسعار':
        v = 'اطلع/ي على الرسالة المثبتة فيها كل التفاصيل 😍👆'
    elif update.message.text == 'بكم الاسعار':
        v = 'اطلع/ي على الرسالة المثبتة فيها كل التفاصيل 😍👆'
    elif update.message.text == 'كم الأسعار':
        v = 'اطلع/ي على الرسالة المثبتة فيها كل التفاصيل 😍👆'
    elif update.message.text == 'احبك':
        v = 'احبك الله'
    elif update.message.text == 'تعال':
        v = 'اصبر وين بأجيك'
    elif update.message.text == 'بوت':
        v = ' مب بوت يابشر'
    elif update.message.text == 'شلونكم':
        v = 'الحمدلله بألف خير 😍👍 وانت/ي؟'
    elif update.message.text == 'كيف الحال':
        v = 'الحمدلله بألف خير 😍👍 وانت/ي؟'
    elif update.message.text == 'كيف؟':
        v = 'والله عاد ماعرف '
    elif update.message.text == 'تعالي خاص':
        v = 'تنبيه!!!. بعض الاشخاص الذين يتعاملون بغش فتأكد من المعلومات القانونية قبل تعاملك معهم لضمان سلامتك الملاحظة للطرفين.تأكد ايضا ان الذي يكلمك من ادارة المجموعة.الادارة غير مسؤولة عن اي تعامل مع اشخاص اخرين وشكرا'
    elif update.message.text == 'هلو':
        v = 'يا اهلا وسهلا فيك 😍 تفضل/ي ؟'
    elif update.message.text == 'باي':
        v = 'استمتع بوقتك'
    elif update.message.text == 'اروح':
        v = 'تمام ارتاح'
    elif update.message.text == 'تحبني':
        v = 'الله يحبك انا من كي لا احبك'
    elif update.message.text == 'تحبيني':
        v = 'الله يحبك انا من كي لا احبك'
    elif update.message.text == 'الحمدلله':
        v = 'يستاهل الحمد'
    elif update.message.text == 'نرد':
         i=random.randrange(1, 100)
         v =i
         
    elif update.message.text == 'ورقة':
        g=random.randrange(1, 4)  
        if g==1 :
          v = 'حجر'
          if v=='حجر'and update.message.text=='ورقة':
             t=' 😆👌  لقد فزت علي يابشر   '
             v=str(v+' '+t)      
          
        elif g==2:
             t=' 😆👌  لقــد تعادلنــا يابشر  '
             v=str(v+' '+t)
   
        elif g==3:
          v = 'مقص'
          if v=='مقص'and update.message.text=='ورقة':
             t=' 😆👌  انتصـــرت عليك يابشر  '
             v=str(v+' '+t)      
             
    elif update.message.text == 'مقص':
        g=random.randrange(1, 4)  
        if g==1 :
          v = 'حجر'
          if v=='حجر'and update.message.text=='مقص':
             t=' 😆👌  انتصـــرت عليك يابشر  '
             v=str(v+' '+t)      
          
        elif g==2:
          v = 'ورقة'
          if v=='ورقة'and update.message.text=='مقص':
             t=' 😆👌  فزت علي يابشر  '
             v=str(v+' '+t)      
   
        elif g==3:
          v = 'مقص'
          if v==update.message.text:
             t=' 😆👌  لقــد تعادلنــا يابشر  '
             v=str(v+' '+t)
        
             
    elif update.message.text == 'حجر':
        g=random.randrange(1, 4)  
        if g==1 :
          v = 'حجر'
          if v=='حجر'and update.message.text=='حجر':
             t=' 😆👌  لقــد تعادلنــا يابشر  '
             v=str(v+' '+t)      
          
        elif g==2:
          v = 'ورقة'
          if v=='ورقة'and update.message.text=='حجر':
             t= ' 😆👌  انتصـــرت عليك يابشر  ' 
             v=str(v+' '+t)      

        elif g==3:
          v = 'مقص'
          if v=='مقص' and update.message.text=='حجر':
             t= ' 😆👌  فزت علي يابشر  '
             v=str(v+' '+t)
        
    bot.send_message(chat_id=update.message.chat_id,
                     text=v, )


updater.dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, new_member))
start_handler = MessageHandler(Filters.text, start)
dispatcher.add_handler(start_handler)
updater.start_polling()
updater.idle()