from os import system 
try:
	import os,sys,time,requests
	import random, telebot, os
	from time import sleep
	from telebot import types
except ImportError:
	os.system('pip install requests')
	os.system('pip install telebot')
	os.system('pip install pyTelegramBotAPI==3.7.7')
	os.system('pip install pyTelegramBotAPI==3.6.7')
	os.system('pip install random')
	os.system('pip install time')
	
bot = telebot.TeleBot("6347021500:AAH1GsJqP9kslq65PM2WU3xWj8jEiPj-sLgا")
own_id = "5927744467"
SaiF = types.InlineKeyboardButton(text = "- CaRLoS?", url = 'https://t.me/q_3_i')
a1  = types.InlineKeyboardButton(text = "تشغيل البوت", callback_data = 's1')
a2  = types.InlineKeyboardButton(text = "ايقاف البوت", callback_data = 's2')
a3  = types.InlineKeyboardButton(text = "اضافه يوزرات", callback_data = 's3')
a4  = types.InlineKeyboardButton(text = "مسح جميع اليوزرات", callback_data = 's4')
a5  = types.InlineKeyboardButton(text = "عرض جميع اليوزرات", callback_data = 's5')
@bot.message_handler(commands=['start'])
def start(message):
    global id
    id = message.from_user.id
    print(id)
    o = types.InlineKeyboardMarkup()
    o.add(a1,a2)
    o.add(a3,a4)
    o.add(a5)
    o.add(SaiF)
    ph = "https://d.top4top.io/p_25994rf5g1.jpg"
    if str(id) == own_id:
    	bot.send_photo(message.chat.id,ph,caption=f"""* - اهلا بك عزيزي؟ الرجاء اختيار الزر المناسب من الاسفل*""",parse_mode="markdown",reply_markup=o)
    if str(id) != own_id:
    	bot.reply_to(message,text='*لك بابه روح فعل من تاج راسك وتعال شهل لزكه؟ بشر مال اهانه*',parse_mode="markdown")
@bot.callback_query_handler(func=lambda call: True)
def oh(call):
    if call.data =="s1":
        runbot(call.message)
    if call.data =="s2":
         stopbot(call.message)
    if call.data =="s3":
         adduser(call.message)
    if call.data =="s4":
         deleteuser(call.message)
    if call.data =="s5":
         alluser(call.message)
def alluser(message):
 	try:
 		i = ('user.txt')
 		r = open(i,'r').read()
 		bot.send_message(message.chat.id, text=f"{r}\nBy : @JaJJJJ")
 	except:
 		bot.send_message(message.chat.id, text="لايوجد ملف لليوزرات .")         
def deleteuser(message):
 	try:
 		os.remove("user.txt")
 		bot.send_message(message.chat.id, text="تم مسح اليوزرات")
 	except:
 		bot.send_message(message.chat.id, text="لايوجد ملف لليوزرات .")
def adduser(message):
 	bot.send_message(message.chat.id, text=" ارسل اليوزرات دون @ .")
 	@bot.message_handler(func=lambda m:True)
 	def textbot(message):
 		acc = message.text
 		if str(id) == own_id:
 			try:
 				with open('user.txt', 'a') as the_combo:
 					the_combo.write(str(acc)+'\n')
 				bot.send_message(message.chat.id, text="تم اضافه اليوزرات")
 			except:
 				bot.send_message(message.chat.id, text="حدث خطأ الرجاء المحاوله مره اخرى .")
def runbot(message):
	try:
		os.remove("info.txt")
		with open('info.txt', 'a') as the_combo:
 				the_combo.write(str("run"))
		bot.send_message(message.chat.id, text="تم التشغيل")
		system("screen -dmS bot python3 base.py")
	except:
		pass 			
def stopbot(message):
	try:
		os.remove("info.txt")
		with open('info.txt', 'a') as the_combo:
 				the_combo.write(str("stop"))
		bot.send_message(message.chat.id, text="تم ايقاف التشغيل")
		system("screen -S bot -X kill")
	except:
		pass 		
bot.polling(none_stop=True)