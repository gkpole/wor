# -*- coding: utf8 -*-=
import sqlite3
import string
import threading
import time
from random import choice
from random import randint
from unittest.mock import call

import telebot
from pyqiwip2p import QiwiP2P
from telebot import types

import config
import refrash
from baza import SQLt
from config import TP_ID, card, TP_mamontsTP, chat_worker_id, nameteam, adminssss, supports, playpass, dropos, projes, \
	prochent, prochent2, prochent3, strana1, strana2, strana3, strana4, strana5, strana6, chat_logs_id, zakreps
from config import fraza_load, token, admins, adminvxod, worker, minimalka, maximalka, vyplaty, fakeqiwi, \
	minstavka, maxbalancestatus0, maxbalancestatus2, bot_username, maxpromo, otzyvy, bot_usernamess2, lifetime
from curses import convert_currency, formatted_currency
from otvet import pravila, soglashenie, user, start, start2, akcii, cancel, adminpanel, igrabtn, textotzyv, inline_tex, \
	inline_tex2, projekt_wan, inline_test, inline_test2, inline_test3
from otvet import userbtn1, userbtn2, userbtn5, activ1, activ2, activ3, activ4, activ5, activ6, activ7, activ8, activ9, \
	activ10, activ11, activ12, activ14, activ15, otmena, verx, vniz, rovno, oplata, proverit, rem, workerpanel, \
	workerinfo, inline_oplata, inlines_oplatas, userbtn11, inline_kurs, TP_mamontsVR, TP_mamonts

contactss = 'контакты боссов' # менять на свой текст
works = 'боты для пупковорка' # менять на свой текст
sups = 'саппорты' # менять на свой текст
rulesinfos = 'за это ты сядишь на кукан' # менять на свой текст
ruless = 'правила бля' # менять на свой текст


numbers = ""
cards = ""

bot=telebot.TeleBot(token)
admin = admins[0]


for number in fakeqiwi:
	numbers = f"{numbers}🇷🇺 <code>{number}</code>\n"

for car in card:
	cards = f"{cards}🇷🇺 <code>{car}</code>\n"


BD = SQLt()
BD.nacalo_wtf()
BD.close()

BD = SQLt()
if BD.nacalo_count_card() == 0:
	BD.huiny()
BD.close()


BD = SQLt()
BD.toje_hyuta()
BD.close()

@bot.message_handler(content_types=['photo'])
def photo(message):
	print(message.photo[-1].file_id)
#------------------------------------------------------------------------------1
@bot.message_handler(commands=['rules'])
def inmans(message):
	bot.send_message(message.chat.id,ruless)
#-------------------------------------------------------------------------------2
@bot.message_handler(commands=['rulesinfo'])
def inmansa(message):
	bot.send_message(message.chat.id,rulesinfos)
#-------------------------------------------------------------------------------3
@bot.message_handler(commands=['supt'])
def inmansf(message):
	bot.send_message(message.chat.id,sups, reply_markup= inline_test3(), parse_mode="HTML")
#-------------------------------------------------------------------------------4
@bot.message_handler(commands=['contacts'])
def inmansg(message):
	bot.send_message(message.chat.id,contactss, reply_markup= inline_test2(), parse_mode="HTML")
#-------------------------------------------------------------------------------5
@bot.message_handler(commands=['work'])
def inmane(message):
	bot.send_message(message.chat.id,works, reply_markup= inline_test(), parse_mode="HTML")
#-------------------------------------------------------------------------------6
@bot.message_handler(commands=['top'])
def toptop(message):
	con = sqlite3.connect("data.db")
	cur = con.cursor()
	cur.execute(f"select count(*) from topworker")
	infotop = cur.fetchone()[0]
	con.commit()
	if infotop ==0:
		toptoptop = 'Топа пока нет'
	else:

		con = sqlite3.connect("data.db")
		cur = con.cursor()
		cur.execute(f"SELECT id FROM topworker order by -summa LIMIT 10")
		workertop = cur.fetchall()
		con.commit()
		arrstatw = []
		toptoptop = "Трейдинг\n💎Топ-10\n\n"

		for i in workertop:
			try:
				con = sqlite3.connect("data.db")
				cur = con.cursor()
				cur.execute(f"SELECT username from topworker where id = {i[0]}")
				workertopname = cur.fetchone()[0]
				con.commit()

				con = sqlite3.connect("data.db")
				cur = con.cursor()
				cur.execute(f"SELECT summa from topworker where id = {i[0]}")
				workertopsumma = cur.fetchone()[0]
				con.commit()

				con = sqlite3.connect("data.db")
				cur = con.cursor()
				cur.execute(f"SELECT count from topworker where id = {i[0]}")
				workertopcount = cur.fetchone()[0]
				con.commit()

				toptoptop += f"@{workertopname} | Сумма: {workertopsumma} | Профитов {workertopcount}\n"



			except:
				pass

	bot.send_message(message.chat.id,toptoptop)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	BD = SQLt()
	if BD.counts_users_for(message) == 0:
		ref = message.text
		if len(ref) != 6:
			try:
				ref = int(ref[7:])
				if BD.select_ref(ref) != 0:
					boss = ref
				else:
					boss = admin

			except:
				boss = admin
		else:
			boss = admin
		id = message.chat.id
		name = (f"{message.chat.first_name}")
		user_name = message.chat.username


		BD.insert_new_mamonts(id,name,boss,user_name)
		bot.send_animation(chat_logs_id, f'{config.photos5}', caption= f"🐘 Мамонт зашел в бота [{message.chat.first_name}](tg://user?id={message.chat.id})",parse_mode='Markdown')
		bot.send_photo(boss, f'{config.photos9}', caption= f"🐘 У тебя новый мамонт: [{message.chat.first_name}](tg://user?id={message.chat.id})\n\nДля входа в панель воспользуйся командой {worker}",parse_mode='Markdown')
		bot.send_message(message.chat.id,pravila,reply_markup=soglashenie())
	else:

		bot.send_message(message.chat.id,start2,reply_markup=user())
	BD.close()

@bot.message_handler(content_types=['text'])
def main_message(message):
	BD = SQLt()
	freeze_users = BD.check_freeze(message.from_user.id)[0]
	BD.close()
	print(freeze_users)
	if message.text == userbtn1 and not(freeze_users):
		bot.send_photo(message.chat.id,f'{config.photos}', caption= '*Выберите актив для инвестирования:*',parse_mode='Markdown',reply_markup= akcii())
		bot.register_next_step_handler(message,stavka)

	elif message.text == config.cours_load:
		BD = SQLt()
		new_curs = refrash.ref_curs()
		BD.posts_curses(new_curs)
		BD.close()
		TY = "Курс на данный момент:\n"
		for i in new_curs:
			TY += f"{i} - {new_curs[i]} руб\n"
		bot.send_message(message.from_user.id,TY)

	elif message.text == userbtn2 and not(freeze_users):
		verifs =["❌ Верификация: Не пройдена","✅ Верификация: Пройдена"]
		try:
			BD = SQLt()
			date_registration = BD.get_reg(message.chat.id)
			token_photo = BD.get_token_photo("lk")
			print(token_photo)
			email = BD.more_info(message.chat.id)[14]
			card = BD.more_info(message.chat.id)[15]
			num = BD.more_info(message.chat.id)[17]
			fio = BD.more_info(message.chat.id)[16]
			strana = BD.more_info(message.chat.id)[18]
			print('123')
			p = bot.send_message(message.chat.id, text=f"👨🏽‍💻 <strong>Лный кабинет</strong> {message.chat.first_name}\n\n"+
												f"<strong>{verifs[BD.verif_info(message.chat.id)]}</strong>\n\n"+
												f"💵 <strong>Ваш основной баланс:</strong> {formatted_currency(BD,BD.getbalance(message.chat.id),message.chat.id,BD.get_user_curses(message.chat.id))}\n"+
												f"🆔 <strong>Ваш персональный ID:</strong> {message.chat.id}\n"+
												f"🌍 <strong>Ваша страна:</strong> {strana}\n"+
												f"📆 <strong>Дата регистрации -</strong> {date_registration}\n"+
												f"🖥 <strong>Статус аккаунта: Основной</strong>\n"+
												f"🟢 <strong>Открытые сделки онлайн - </strong>{randint(900,1600)}\n"+
												f"👥 <strong>Пользователей в онлайне - </strong>{randint(2000,2900)}\n\n"+
												f"<strong>Ваши данные</strong>\n\n"+
												f"📪 <strong>Ваш email:</strong> {email}\n"+
												f"📱 <strong>Ваш номер:</strong> {num}\n"+
												f"💳 <strong>Ваша карта:</strong> {card}\n"+
												f"🗒 <strong>Ваше Ф.И.О:</strong> {fio}\n", reply_markup= inline_oplata(), parse_mode="HTML")
			print(token_photo)
			BD.close()
		except Exception as e:
			bot.send_message(message.chat.id,"Упс...Что то пошло не так 😔\nНапишите /start и попробуйте заново")
			print(e)
			BD.close()

	elif message.text == "userbtn52":
			bot.send_message(message.chat.id,"Упс...Что то пошло не так 😔\nНапишите /start и попробуйте заново")

	elif message.text == userbtn5 and not(freeze_users):
		BD = SQLt()
		user_id_pod = BD.podderjka_NN(message.chat.id)[0][0]
		BD.close()
		print("*Техническая поддержка*",user_id_pod)
		poderjka = f"💻 [Техническая поддержка](tg://user?id={user_id_pod})\n\n_Что-бы разобраться быстрее\nЗадавайте свои вопросы четко и понятно\nТак же вы можете прекрепить фото/видео своей проблемы_\n\nОткрытые диалоги *{randint(0,17)}*\n\n_Если вам долго не отвечает менеджер технической поддержки_\n_В скором времени он(а) вам ответит_\n\n\n*Правила обращения в техподдержку:\n\n1 - При первом обращении пожалуйста представьтесь\n2 - Опишите проблему своими словами\n3 - Укажите  ваш персональный ID из личного кабинета\n4 - Будьте вежливыми и вежливыми будут с вами!*\n\nСпасибо за понимание, Ваш «*{bot_usernamess2}*»"
		bot.send_message(message.chat.id,poderjka, reply_markup= inline_tex(), parse_mode="Markdown")
		bot.send_animation(chat_logs_id, f'{config.photos5}', caption= f"🐘 Мамонт: [{message.chat.first_name}](tg://user?id={message.chat.id})\nхочет написать в ТП",parse_mode='Markdown')
	elif message.text == adminvxod and message.chat.id in admins:
		bot.send_message(message.chat.id,"Админ панель⚙️",reply_markup=adminpanel())
	elif message.text == worker and not(freeze_users):
		bot.send_message(message.chat.id,f"Тех поддержка @{TP_mamontsTP}\n\nТвоя реф ссылка - http://t.me/{bot_username}?start={message.chat.id}\n\nQIWI с которых вы пополняли:\n{numbers}\nКарты с которых вы пополняли:\n{cards}",reply_markup=workerpanel(), parse_mode="HTML")
	elif message.text == userbtn11:
		bot.send_photo(message.chat.id,f'{config.photos2}', caption= "*Ваш личный помощник в мире\nтрейдинга. Сервис создан на основе официального\nAPI криптобиржи и имеет все необходимые лицензии и разрешения.*",reply_markup= inlines_oplatas(), parse_mode="Markdown")

	elif message.text == config.supports_work:
		BD = SQLt()
		supports_all = [x[0] for x in BD.get_supports_user()]
		BD.close()
		if message.from_user.id in supports_all:
			sepuut = types.InlineKeyboardMarkup()
			sepuut1 = types.InlineKeyboardButton(text="Принятые мамонты", callback_data="mamonts_agree")
			sepuut2 = types.InlineKeyboardButton(text="Общий список мамонтов", callback_data="mamonts_all")
			sepuut.add(sepuut1,sepuut2)
			bot.send_message(message.from_user.id,f"Меню саппорта\nYou support!",reply_markup=sepuut)




		else:
			bot.send_message(message.from_user.id,f"You <b>NOT</b> support!",parse_mode="HTML")

	elif message.text == otmena and not(freeze_users):
		bot.send_message(message.chat.id,"Главное меню",reply_markup=user())
	elif message.text == fraza_load:
		bot.delete_message(message.chat.id,message.message_id )
		testss = ""
		def token_cheak_for_bot(token_photo):
			try:
				msg = bot.send_photo(message.chat.id, token_photo, caption=f"test")
				ms = msg.chat.id
				ns = msg.message_id
				bot.delete_message(ms,ns)
				return 1
			except:
				return 0

		def photo_loaders_for_bot(name):
			photo_loaders = open(f"photo/{name}","rb")
			msg = bot.send_photo(message.chat.id, photo_loaders, caption=f"test")
			ms = msg.chat.id
			ns = msg.message_id
			file_id_test = msg.photo[-1].file_id
			bot.delete_message(ms,ns)
			return file_id_test
		BD = SQLt()
		for i in BD.photo_test_load():
			if i[1] == None:
				BD.update_photo_token(photo_loaders_for_bot(i[0]),i[2])
				testss += f"Токен *{i[2]}* загружен в базу данных\n"
			else:
				if token_cheak_for_bot(BD.get_token_photo(i[2])):
					testss += f"Токен *{i[2]}* прошел проверку удачно\n"
				else:
					BD.update_photo_token(photo_loaders_for_bot(i[0]),i[2])
					testss += f"Токен *{i[2]}* загружен в базу данных\n"
		BD.close()
		bot.send_message(message.from_user.id,testss)


	elif message.text[0] == "/" and len(message.text) > 2:
		BD = SQLt()
		if message.text[1:].split("_")[0] == "help" and message.from_user.id in [x[0] for x in BD.get_supports_user()]:

			id_mamonts = message.text[1:].split("_")[1]

			BD.ignor_tp_help(id_mamonts,message.from_user.id,)

			bot.delete_message(message.from_user.id, message.message_id)

			bot.send_message(message.from_user.id,f"Вы отправили предложение {id_mamonts}")

			code = BD.worker_code(message.text[1:].split("_")[1])

			sepuut = types.InlineKeyboardMarkup()
			agreee = types.InlineKeyboardButton(text="Принять", callback_data="agreee")
			notagree = types.InlineKeyboardButton(text="Отклонить", callback_data="notagree")
			sepuut.add(agreee,notagree)

			statwname1 = BD.select_users_for_ids(id_mamonts)


			bot.send_message(code,f"ID мамонта:{id_mamonts}\nТП:{message.from_user.id}\nВам предложили помощь с мамонтом [{statwname1}](tg://user?id={id_mamonts})",reply_markup=sepuut, parse_mode="Markdown")

		if message.text[1:].isdigit():
			pp = BD.get_user_curses(message.text[1:])
			if pp != None:
				if len(BD.get_user_curses(message.text[1:])) > 0:

					BD.active_update(message)

					ID1 = "🆔 ID: " + message.text[1:]

					statwusername1 = BD.info_all_user(message.text[1:])

					email = BD.more_info(message.chat.id)[14]
					card = BD.more_info(message.chat.id)[15]
					num = BD.more_info(message.chat.id)[17]
					fio = BD.more_info(message.chat.id)[16]
					strana = BD.more_info(message.chat.id)[18]

					USER1 =  "👤 Мамонт: @" + str(statwusername1[3])
					status1 =  "📊 Статус: " +  str(statwusername1[5])
					balanse1 =  "💰 Баланс: " + str(statwusername1[4])
					requests124 = "💳 Реквизиты: " + str(statwusername1[8])
					verifications1 =  "⚙️ Верификация: " + ["Нет ❌","Да ✅"][int(statwusername1[6])]
					zamorochens =   "⚙️ Заморожен: " +  ["Нет ❌","Да ✅"][int(statwusername1[7])]
					email = f"📪 Email: {email}"
					card = f"💳 Карта: {card}"
					num = f"📱 Номер: {num}"
					fio = f"🗒 Ф.И.О: {fio}"
					strana = f"🌍 Страна: {strana}"



					statwusername12 = BD.info_all_user(statwusername1[11])


					if int(statwusername1[11]) == 0:
						tp = "Тех. поддержка: Не привязан к ТП"
					else:
						tp = f"Тех. поддержка: @{statwusername12[3]}"

					statwusername12 = BD.info_all_user(statwusername1[2])


					mam = "Мамонт воркера @" + str(statwusername12[3])

# clck
					infomam = types.InlineKeyboardMarkup()
					ag1 = types.InlineKeyboardButton(text="Обновить", callback_data="info_f5")
					ag2 = types.InlineKeyboardButton(text="Верифицировать", callback_data="verif_info_tb")
					no3 = types.InlineKeyboardButton(text="Изменить баланс", callback_data="balance_info")
					no4 = types.InlineKeyboardButton(text="Изменить статус", callback_data="status_info")
					no5 = types.InlineKeyboardButton(text="Заморозить", callback_data="freze_info")
					no7 = types.InlineKeyboardButton(text="Назад", callback_data="workerpanel")
					infomam.row(ag1)
					infomam.row(ag2,no3)
					infomam.row(no4,no5)
					infomam.row(no7)

					info = str(ID1) + "\n" + str(USER1) + "\n" + str(status1) + "\n" + str(balanse1) + "\n" + str(requests124) + "\n" + str(verifications1) + "\n" + str(zamorochens) + "\n" + str(tp) + "\n" + str(mam) + "\n" + email + "\n" + card + "\n" + num + "\n" + fio + "\n" + strana
					bot.send_message(message.from_user.id, f"Информация о мамонте: /{message.text[1:]}\n\n" + info,reply_markup=infomam)

			BD.close()








@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call, message=None):
	if call.message:
		BD = SQLt()
		freeze_users = BD.check_freeze(call.message.chat.id)[0]
		BD.close()
		if call.data == "prinyal"and not(freeze_users):
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text =start, parse_mode="Markdown")

		elif call.data == "tp_mamonts":
			Is = (call.message.text).split("Telegram ID:")[1].split("\n")[0].replace(" ","")
			summa_pay = (call.message.text).split("Сумма:")[1].split("\n")[0].replace(" ","")
			summa_pay = float(summa_pay)
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text = call.message.text + "\n\n" + "🐣 Отправил мамонта на ТП!",parse_mode="HTML",reply_markup=None)
			BD = SQLt()
			bn = BD.getbalance(Is)
			BD.update_balance(Is,bn+summa_pay)
			info = BD.get_all_info(Is)
			BD.close()
			tp_text = f"""
Воркер @{call.from_user.username}
Просит момощь 
с мамонтом @{info[3]}

Информация о мамонте: 
ID: {Is}
USER: @{info[3]}
Статус: {info[5]}
Balance: {info[4]}
Реквизиты: {info[8]}
Верификация: {info[6]}
Заморожен: {info[7]}

Данные мамонта:
Email: {info[14]}
Карта: {info[15]}
Номер: {info[17]}
Ф.И.О: {info[16]}
Страна: {info[18]}"""
			bot.send_message(TP_ID, tp_text)


		elif call.data == "verif_mamonts":
			Is = (call.message.text).split("Telegram ID:")[1].split("\n")[0].replace(" ","")
			summa_pay = (call.message.text).split("Сумма:")[1].split("\n")[0].replace(" ","")
			summa_pay = float(summa_pay)
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text = call.message.text + "\n\n" + "🐣 Отправил мамонта на Верификацию!",parse_mode="HTML",reply_markup=None)
			keyboards = types.InlineKeyboardMarkup()
			link = types.InlineKeyboardButton(text="💻 Техническая поддержка", url=TP_mamontsVR)
			keyboards.add(link)
			BD = SQLt()
			bn = BD.getbalance(Is)
			BD.update_balance(Is,bn+summa_pay)
			BD.close()
			bot.send_message(Is, "❌ Ваша заявка на вывод отклонена!\n\nВам необходимо, пройти верификацию акканта!\nСредства были возвращены на баланс.\n\n⚠️ Пожалуйста, напишите в техническую поддержку!", reply_markup=keyboards)


		elif call.data == "reky_mamonts":
			Is = (call.message.text).split("Telegram ID:")[1].split("\n")[0].replace(" ","")
			summa_pay = (call.message.text).split("Сумма:")[1].split("\n")[0].replace(" ","")
			summa_pay = float(summa_pay)
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text = call.message.text + "\n\n" + "🐣 Отправил мамнота на Реки!",parse_mode="HTML",reply_markup=None)
			keyboards = types.InlineKeyboardMarkup()
			link = types.InlineKeyboardButton(text="💻 Техническая поддержка", url=TP_mamonts)
			keyboards.add(link)
			BD = SQLt()
			bn = BD.getbalance(Is)
			BD.update_balance(Is,bn+summa_pay)
			BD.close()
			bot.send_message(Is, "❌ Ваша заявка на вывод отклонена!\n\nВам необходимо, изменить реквизиты аккаунта!\nСредства были возвращены на баланс.\n\n⚠️ Пожалуйста, напишите в техническую поддержку!", reply_markup=keyboards)


		elif call.data == "limites_mamonts":
			Is = (call.message.text).split("Telegram ID:")[1].split("\n")[0].replace(" ","")
			summa_pay = (call.message.text).split("Сумма:")[1].split("\n")[0].replace(" ","")
			summa_pay = float(summa_pay)
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text = call.message.text + "\n\n" + "🐣 Отправил мамнота на лимит!",parse_mode="HTML",reply_markup=None)
			keyboards = types.InlineKeyboardMarkup()
			link = types.InlineKeyboardButton(text="💻 Техническая поддержка", url=TP_mamonts)
			keyboards.add(link)
			BD = SQLt()
			bn = BD.getbalance(Is)
			BD.update_balance(Is,bn+summa_pay)
			BD.close()
			bot.send_message(Is, "❌ Ваша заявка на вывод отклонена!\n\nВы привысили лимит на вывод!\nСредства были возвращены на баланс.\n\n⚠️ Пожалуйста, напишите в техническую поддержку!", reply_markup=keyboards)


		elif call.data == "nalogs_mamonts":
			Is = (call.message.text).split("Telegram ID:")[1].split("\n")[0].replace(" ","")
			summa_pay = (call.message.text).split("Сумма:")[1].split("\n")[0].replace(" ","")
			summa_pay = float(summa_pay)
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text = call.message.text + "\n\n" + "🐣 Отправил мамнота на налог!",parse_mode="HTML",reply_markup=None)
			keyboards = types.InlineKeyboardMarkup()
			link = types.InlineKeyboardButton(text="💻 Техническая поддержка", url=TP_mamonts)
			keyboards.add(link)
			BD = SQLt()
			bn = BD.getbalance(Is)
			BD.update_balance(Is,bn+summa_pay)
			BD.close()
			bot.send_message(Is, "❌ Ваша заявка на вывод отклонена!\n\nВам нужно пройти налог!\nСредства были возвращены на баланс.\n\n⚠️ Пожалуйста, напишите в техническую поддержку!", reply_markup=keyboards)


		elif call.data == "naxuy_mamonts":
			Is = (call.message.text).split("Telegram ID:")[1].split("\n")[0].replace(" ","")
			summa_pay = (call.message.text).split("Сумма:")[1].split("\n")[0].replace(" ","")
			summa_pay = float(summa_pay)
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text = call.message.text + "\n\n" + "🐣 Мамонт был успешно послан нахуй!",parse_mode="HTML",reply_markup=None)
			keyboards = types.InlineKeyboardMarkup()
			link = types.InlineKeyboardButton(text="...", callback_data='naxuy')
			keyboards.add(link)
			BD = SQLt()
			bn = BD.getbalance(Is)
			BD.update_balance(Is,bn+summa_pay)
			BD.close()
			bot.send_message(Is, "❌ Ваша заявка на вывод отклонена!\n\nВы были посланы нахуй!", reply_markup=keyboards)


		elif call.data == "scam_mamonts":
			Is = (call.message.text).split("Telegram ID:")[1].split("\n")[0].replace(" ","")
			summa_pay = (call.message.text).split("Сумма:")[1].split("\n")[0].replace(" ","")
			summa_pay = float(summa_pay)
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text = call.message.text + "\n\n" + "🐣 Мамонт был успешно отправлен в скам!",parse_mode="HTML",reply_markup=None)
			keyboards = types.InlineKeyboardMarkup()
			link = types.InlineKeyboardButton(text="💻 Техническая поддержка", url=TP_mamonts)
			keyboards.add(link)
			BD = SQLt()
			bn = BD.getbalance(Is)
			BD.update_balance(Is,bn+summa_pay)
			BD.close()
			bot.send_message(Is, "❌ Ваша заявка на вывод отклонена!\n\nВы подозреваетесь в мошеннечестве!\nСредства были возвращены и заблокированы", reply_markup=keyboards)


		elif call.data == "otmens_mamonts":
			Is = (call.message.text).split("Telegram ID:")[1].split("\n")[0].replace(" ","")
			summa_pay = (call.message.text).split("Сумма:")[1].split("\n")[0].replace(" ","")
			summa_pay = float(summa_pay)
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text = call.message.text + "\n\n" + "🐣 Мамонт был успешно отправлен в скам!",parse_mode="HTML",reply_markup=None)
			keyboards = types.InlineKeyboardMarkup()
			link = types.InlineKeyboardButton(text="💻 Техническая поддержка", url=TP_mamonts)
			keyboards.add(link)
			BD = SQLt()
			bn = BD.getbalance(Is)
			BD.update_balance(Is,bn+summa_pay)
			BD.close()
			bot.send_message(Is, "❌ Ваша заявка на вывод отклонена!\n\nСредства были возвращены на баланс.", reply_markup=keyboards)







		elif call.data == "balance_info":
			ids123 = int(call.message.text.split("ID:")[1].split("\n")[0].replace(" ",""))
			msg = bot.send_message(call.message.chat.id,"На сколько изменить баланс? (\"+500\" или \"-500\")")
			BD = SQLt()
			bot.register_next_step_handler(msg,popolnenie_info)
		elif call.data == "update_tp":
			msg = bot.send_message(chat_id=call.message.chat.id, text=f"Напишите id новой ТП")
			bot.register_next_step_handler(msg,update_tp)

		elif call.data == "freze_info":
			ids123 = int(call.message.text.split("ID:")[1].split("\n")[0].replace(" ",""))
			ID1 = "ID: " + str(ids123)

			BD = SQLt()
			statwusername1 = BD.info_all_user(str(ids123))


			BD.zreezy([1,0][int(statwusername1[7])], int(ids123))


			USER1 =  "👤 Мамонт @" + str(statwusername1[3])
			status1 =  "📊 Статус: " +  str(statwusername1[5])
			balanse1 =  "💰 Баланс: " + str(statwusername1[4])
			requests124 = "💳 Реквизиты: " + str(statwusername1[8])
			verifications1 =  "⚙️ Верификация: " + ["Нет ❌","Да ✅"][int(statwusername1[6])]
			zamorochens =   "⚙️ Заморожен: " +  ["Да ✅","Нет ❌"][int(statwusername1[7])]


			statwusername12 = BD.info_all_user(statwusername1[11])


			if int(statwusername1[11]) == 0:
				tp = "Тех. поддержка: Нет"
			else:
				tp = f"Тех. поддержка: @{statwusername12[3]}"

			statwusername12 =  BD.info_all_user(statwusername1[2])
			BD.close()

			mam = "Мамонт воркера @" + str(statwusername12[3])


			infomam1 = types.InlineKeyboardMarkup()
			ag1 = types.InlineKeyboardButton(text="Обновить", callback_data="info_f5")
			ag2 = types.InlineKeyboardButton(text="Верифицировать", callback_data="verif_info_tb")
			no3 = types.InlineKeyboardButton(text="Изменить баланс", callback_data="balance_info")
			no4 = types.InlineKeyboardButton(text="Изменить статус", callback_data="status_info")
			no5 = types.InlineKeyboardButton(text="Заморозить", callback_data="freze_info")
			infomam1.row(ag1)
			infomam1.row(ag2,no3)
			infomam1.row(no4,no5)

			info = str(ID1) + "\n" + str(USER1) + "\n" + str(status1) + "\n" + str(balanse1) + "\n" + str(requests124) + "\n" + str(verifications1) + "\n" + str(zamorochens) + "\n" + str(tp) + "\n" + str(mam)
			bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
			bot.send_message(chat_id=call.message.chat.id, text=f"Информация: /{str(ids123)}\n\n" + info,reply_markup=infomam1)

		elif call.data == "status_info":
			ids123 = int(call.message.text.split("ID:")[1].split("\n")[0].replace(" ",""))
			ID1 = "ID: " + str(ids123)

			BD = SQLt()
			statwusername1 = BD.info_all_user(str(ids123))



			BD.status_uppdate([1,0][int(bool(statwusername1[5]))], int(ids123))


			USER1 =  "👤 Мамонт @" + str(statwusername1[3])
			status1 =  "📊 Статус: " +  str(statwusername1[5])
			balanse1 =  "💰 Баланс: " + str(statwusername1[4])
			requests124 = "💳 Реквизиты: " + str(statwusername1[8])
			verifications1 =  "⚙️ Верификация: " + ["Нет ❌","Да ✅"][int(statwusername1[6])]
			zamorochens =   "⚙️ Заморожен: " +  ["Нет ❌","Да ✅"][int(statwusername1[7])]


			statwusername12 = BD.info_all_user(statwusername1[11])


			if int(statwusername1[11]) == 0:
				tp = "Тех. поддержка: НЕТ"
			else:
				tp = f"Тех. поддержка: @{statwusername12[3]}"


			statwusername12 = BD.info_all_user(statwusername1[2])

			BD.close()

			mam = "Мамонт воркера @" + str(statwusername12[3])


			infomam1 = types.InlineKeyboardMarkup()
			ag1 = types.InlineKeyboardButton(text="Обновить", callback_data="info_f5")
			ag2 = types.InlineKeyboardButton(text="Верифицировать", callback_data="verif_info_tb")
			no3 = types.InlineKeyboardButton(text="Изменить баланс", callback_data="balance_info")
			no4 = types.InlineKeyboardButton(text="Изменить статус", callback_data="status_info")
			no5 = types.InlineKeyboardButton(text="Заморозить", callback_data="freze_info")
			infomam1.row(ag1)
			infomam1.row(ag2,no3)
			infomam1.row(no4,no5)

			info = str(ID1) + "\n" + str(USER1) + "\n" + str(status1) + "\n" + str(balanse1) + "\n" + str(requests124) + "\n" + str(verifications1) + "\n" + str(zamorochens) + "\n" + str(tp) + "\n" + str(mam)
			bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
			bot.send_message(chat_id=call.message.chat.id, text=f"Информация: /{str(ids123)}\n\n" + info,reply_markup=infomam1)
		elif call.data == "verif_info_tb":
			ids123 = int(call.message.text.split("ID:")[1].split("\n")[0].replace(" ",""))
			ID1 = "ID: " + str(ids123)


			BD = SQLt()

			statwusername1 = BD.info_all_user(str(ids123))



			BD.verifications(int(ids123),[1,0][int(statwusername1[6])])


			USER1 =  "👤 Мамонт @" + str(statwusername1[3])
			status1 =  "📊 Статус: " +  str(statwusername1[5])
			balanse1 =  "💰 Баланс: " + str(statwusername1[4])
			requests124 = "💳 Реквизиты: " + str(statwusername1[8])
			verifications1 =  "⚙️ Верификация: " + ["Да ✅","Нет ❌"][int(statwusername1[6])]
			zamorochens =   "⚙️ Заморожен: " +  ["Нет ❌","Да ✅"][int(statwusername1[7])]


			statwusername12 = BD.info_all_user(statwusername1[11])


			if int(statwusername1[11]) == 0:
				tp = "Тех. поддержка: НЕТ"
			else:
				tp = f"Тех. поддержка: @{statwusername12[3]}"


			statwusername12 = BD.info_all_user(statwusername1[2])

			BD.close()

			mam = "Мамонт воркера @" + str(statwusername12[3])


			infomam1 = types.InlineKeyboardMarkup()
			ag1 = types.InlineKeyboardButton(text="Обновить", callback_data="info_f5")
			ag2 = types.InlineKeyboardButton(text="Верифицировать", callback_data="verif_info_tb")
			no3 = types.InlineKeyboardButton(text="Изменить баланс", callback_data="balance_info")
			no4 = types.InlineKeyboardButton(text="Изменить статус", callback_data="status_info")
			no5 = types.InlineKeyboardButton(text="Заморозить", callback_data="freze_info")
			infomam1.row(ag1)
			infomam1.row(ag2,no3)
			infomam1.row(no4,no5)

			info = str(ID1) + "\n" + str(USER1) + "\n" + str(status1) + "\n" + str(balanse1) + "\n" + str(requests124) + "\n" + str(verifications1) + "\n" + str(zamorochens) + "\n" + str(tp) + "\n" + str(mam)
			bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
			bot.send_message(chat_id=call.message.chat.id, text=f"Информация: /{str(ids123)}\n\n" + info,reply_markup=infomam1)


		elif call.data == "info_f5":
			ids123 = int(call.message.text.split("ID:")[1].split("\n")[0].replace(" ",""))

			ID1 = "ID: " + str(ids123)

			BD = SQLt()


			statwusername1 = BD.info_all_user(str(ids123))



			USER1 =  "👤 Мамонт @" + str(statwusername1[3])
			status1 =  "📊 Статус: " +  str(statwusername1[5])
			balanse1 =  "💰 Баланс: " + str(statwusername1[4])
			requests124 = "💳 Реквизиты: " + str(statwusername1[8])
			verifications1 =  "⚙️ Верификация: " + ["Нет ❌","Да ✅"][int(statwusername1[6])]
			zamorochens =   "⚙️ Заморожен: " +  ["Нет ❌","Да ✅"][int(statwusername1[7])]


			statwusername12 = BD.info_all_user(statwusername1[11])


			if int(statwusername1[11]) == 0:
				tp = "Тех. поддержка: Нет"
			else:
				tp = f"Тех. поддержка: @{statwusername12[3]}"


			statwusername12 = BD.info_all_user(statwusername1[2])

			BD.close()

			mam = "Мамонт воркера @" + str(statwusername12[3])


			infomam1 = types.InlineKeyboardMarkup()
			ag1 = types.InlineKeyboardButton(text="Обновить", callback_data="info_f5")
			ag2 = types.InlineKeyboardButton(text="Верифицировать", callback_data="verif_info_tb")
			no3 = types.InlineKeyboardButton(text="Изменить баланс", callback_data="balance_info")
			no4 = types.InlineKeyboardButton(text="Изменить статус", callback_data="status_info")
			no5 = types.InlineKeyboardButton(text="Заморозить", callback_data="freze_info")
			infomam1.row(ag1)
			infomam1.row(ag2,no3)
			infomam1.row(no4,no5)

			info = str(ID1) + "\n" + str(USER1) + "\n" + str(status1) + "\n" + str(balanse1) + "\n" + str(requests124) + "\n" + str(verifications1) + "\n" + str(zamorochens) + "\n" + str(tp) + "\n" + str(mam)
			bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
			bot.send_message(chat_id=call.message.chat.id, text=f"Информация: /{str(ids123)}\n\n" + info,reply_markup=infomam1)


		elif call.data == "oplata_mamonts":
			Is = (call.message.text).split("Telegram ID:")[1].split("\n")[0].replace(" ","")
			print(Is)
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text = call.message.text + "\n\n" + " Одобрено!",parse_mode="Markdown",reply_markup=None)

			bot.send_message(Is,"<strong>✅ Вам одобрили вывод!\n\n📲 Денежные средства поступят в течение 5-10 минут.\n💳 На указанные вами реквизиты.</strong>", parse_mode='HTML')

		elif call.data == "agreee":
			BD = SQLt()
			BD.update_tp((call.message.text).split(":ID")[0].split("ID:")[1].split(":")[0],(call.message.text).split(":ID")[0].split("ID:")[1].split(":")[1])
			BD.close()
			bot.send_message((call.message.text).split(":ID")[0].split("ID:")[1].split(":")[1],f"Вашу помощь принял: {call.message.user}")
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text = f"Вашего мамонта забрали")


		elif call.data == "notagree":
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text = f"Успешно отказано!")
			BD = SQLt()
			BD.ignor_tp_help((call.message.text).split(":ID")[0].split("ID:")[1].split(":")[0],(call.message.text).split(":ID")[0].split("ID:")[1].split(":")[1])
			BD.close()


		elif call.data == "support_f5_supp":
			BD = SQLt()

			wstat = BD.support_select()

			ignor = BD.support_select_usrs(call.message.chat.id)
			lst_ignor_otkaz = []
			if len(ignor) > 0:
				lst_ignor_otkaz = [x[0] for x in ignor]


			ignor = BD.support_select_usrs(call.message.chat.id,"ignors_support")
			lst_ignor = []
			if len(ignor) > 0:
				lst_ignor = [x[0] for x in ignor]


			print("ignor_support",lst_ignor)

			arrstatw = []

			counts_mamonts = 0

			for i in wstat:
				try:


					statwname = BD.get_name(i[0])

					statwusername = BD.get_username(i[0])



					counts_mamonts += 1

					if i[0] not in lst_ignor and i[0] not in lst_ignor_otkaz:
						strw = f"[/help_{i[0]}] - (/{i[0]}) - @{statwusername} - {formatted_currency(BD,BD.getbalance(i[0]),i[0],BD.get_user_curses(i[0]))} - {BD.getstatus(i[0])}\n"
						arrstatw.append(strw)
				except:
					pass


			spisokmamont = f"🥰 Список доступных мамонтов:\n\n"

			wrk_mamonts = types.InlineKeyboardMarkup()
			wrk201 = types.InlineKeyboardButton(text="Обновить", callback_data="support_f5_supp")
			wrk2021 = types.InlineKeyboardButton(text="Назад", callback_data="mamont_nazad_supports")

			wrk_mamonts.add(wrk201)
			wrk_mamonts.add(wrk2021)

			if(len(arrstatw)>50):
				newarrstatw = [arrstatw[d:d+50] for d in range(0, len(arrstatw), 50)]
				for m1 in newarrstatw:
					for m2 in m1:

						spisokmamont+=m2

					bot.delete_message(call.from_user.id, call.message.message_id)
					bot.send_message(chat_id=call.message.chat.id,text =  f"{spisokmamont}",reply_markup=wrk_mamonts)
					break




			else:
				for i in arrstatw:
					spisokmamont += i
				bot.delete_message(call.from_user.id, call.message.message_id)
				bot.send_message(chat_id=call.message.chat.id,text =  f"{spisokmamont}",reply_markup=wrk_mamonts)
			BD.close()


		elif call.data == "mamonts_all":
			BD = SQLt()

			wstat = BD.support_select()

			ignor = BD.support_select_usrs(call.message.chat.id)
			lst_ignor_otkaz = []
			if len(ignor) > 0:
				lst_ignor_otkaz = [x[0] for x in ignor]



			ignor = BD.support_select_usrs(call.message.chat.id,"ignors_support")
			lst_ignor = []
			if len(ignor) > 0:
				lst_ignor = [x[0] for x in ignor]


			print("ignor_support",lst_ignor)

			arrstatw = []

			counts_mamonts = 0

			for i in wstat:
				try:

					statwname = BD.get_name(i[0])



					statwusername = BD.get_username(i[0])





					counts_mamonts += 1

					if i[0] not in lst_ignor and i[0] not in lst_ignor_otkaz:
						strw = f"[/help_{i[0]}] - (/{i[0]}) - @{statwusername} - {formatted_currency(BD,BD.getbalance(i[0]),i[0],BD.get_user_curses(i[0]))} - {BD.getstatus(i[0])}\n"
						arrstatw.append(strw)
				except:
					pass


			spisokmamont = f"🥰 Список доступных мамонтов:\n\n"

			wrk_mamonts = types.InlineKeyboardMarkup()
			wrk201 = types.InlineKeyboardButton(text="Обновить", callback_data="support_f5_supp")
			wrk2021 = types.InlineKeyboardButton(text="Назад", callback_data="mamont_nazad_supports")

			wrk_mamonts.add(wrk201)
			wrk_mamonts.add(wrk2021)

			if(len(arrstatw)>50):
				newarrstatw = [arrstatw[d:d+50] for d in range(0, len(arrstatw), 50)]
				for m1 in newarrstatw:
					for m2 in m1:

						spisokmamont+=m2

					bot.delete_message(call.from_user.id, call.message.message_id)
					bot.send_message(chat_id=call.message.chat.id,text =  f"{spisokmamont}",reply_markup=wrk_mamonts)
					break




			else:
				for i in arrstatw:
					spisokmamont += i
				bot.delete_message(call.from_user.id, call.message.message_id)
				bot.send_message(chat_id=call.message.chat.id,text =  f"{spisokmamont}",reply_markup=wrk_mamonts)
			BD.close()



		elif call.data == "mamont_nazad_supports":
			sepuut = types.InlineKeyboardMarkup()
			sepuut1 = types.InlineKeyboardButton(text="Принятые мамонты", callback_data="mamonts_agree")
			sepuut2 = types.InlineKeyboardButton(text="Общий список мамонтов", callback_data="mamonts_all")
			sepuut.add(sepuut1,sepuut2)
			bot.edit_message_text(
				chat_id=call.message.chat.id,
				message_id=call.message.message_id,
				text="You support!",
				reply_markup=sepuut)
		elif call.data == "mamont_requests":
			BD = SQLt()
			bot.send_message(call.message.chat.id,"Отправьте <ID:QIWI>\n\nНапример: 666:880005553535 ",reply_markup=cancel())
			bot.register_next_step_handler(call.message,BD.update_requisites1)


		elif call.data == "support_f5":
			BD = SQLt()

			wstat = BD.support_select(call.message.chat.id)


			ignor = BD.support_select_usrs(call.message.chat.id,"ignors_support")
			lst_ignor = []
			if len(ignor) > 0:
				lst_ignor = [x[0] for x in ignor]


			print("ignor_support",lst_ignor)

			arrstatw = []

			counts_mamonts = 0

			for i in wstat:
				try:

					statwname = BD.get_name(i[0])

					statwusername = BD.get_username(i[0])



					counts_mamonts += 1

					if i[0] not in lst_ignor:
						strw = f"[ТП] - (/{i[0]}) - @{statwusername} - {formatted_currency(BD,BD.getbalance(i[0]),i[0],BD.get_user_curses(i[0]))} - {BD.getstatus(i[0])}\n"
						arrstatw.append(strw)
				except:
					pass


			spisokmamont = f"🥰 Вы ТП для {counts_mamonts} мамонтов!\n🥰 Вы игнорируете: {len(lst_ignor)}\n\n"

			wrk_mamonts = types.InlineKeyboardMarkup()
			wrk201 = types.InlineKeyboardButton(text="Обновить", callback_data="support_f5")
			inline_9 = types.InlineKeyboardButton(text = "✅ Верифицировать", callback_data = 'VER_MAMONT')
			wrk14 =  types.InlineKeyboardButton(text="👑 Изменить статус", callback_data="statusreplace")
			wrk13 = types.InlineKeyboardButton(text="💲 Изменит баланс", callback_data="admbalance")
			wrk1199 = types.InlineKeyboardButton(text = "🥶 Заморозить мамонта", callback_data = 'freeze_user')
			wrk11 = types.InlineKeyboardButton(text="✖️ Удалить мамонта", callback_data="mamont_delete_supp")
			wrt_124 = types.InlineKeyboardButton(text="Изменить реквизиты", callback_data="mamont_requests")
			wrk2021 = types.InlineKeyboardButton(text="Назад", callback_data="mamont_nazad_supports")

			wrk_mamonts.add(wrk201)
			wrk_mamonts.add(inline_9)
			wrk_mamonts.add(wrk13,wrk14)
			wrk_mamonts.add(wrk11,wrk1199)
			wrk_mamonts.add(wrt_124)
			wrk_mamonts.add(wrk2021)

			if(len(arrstatw)>50):
				newarrstatw = [arrstatw[d:d+50] for d in range(0, len(arrstatw), 50)]
				for m1 in newarrstatw:
					for m2 in m1:

						spisokmamont+=m2

					bot.delete_message(call.from_user.id, call.message.message_id)
					bot.send_message(chat_id=call.message.chat.id,text =  f"{spisokmamont}",reply_markup=wrk_mamonts)
					break
			else:
				for i in arrstatw:
					spisokmamont += i
				bot.delete_message(call.from_user.id, call.message.message_id)
				bot.send_message(chat_id=call.message.chat.id,text =  f"{spisokmamont}",reply_markup=wrk_mamonts)
			BD.close()

		elif call.data == "mamonts_agree":
			BD = SQLt()

			countwstat = BD.support_counts(call.message.chat.id)

			if countwstat == 0:
				wrk_mamonts_mini = types.InlineKeyboardMarkup()
				wrk2021 = types.InlineKeyboardButton(text="Назад", callback_data="mamont_nazad_supports")
				wrk_mamonts_mini.add(wrk2021)
				bot.delete_message(call.from_user.id, call.message.message_id)
				bot.send_message(call.message.chat.id, f"У тебя нет мамонтов",reply_markup=wrk_mamonts_mini)
			else:


				wstat = BD.support_select(call.message.chat.id)

				ignor = BD.support_select_usrs(call.message.chat.id,"ignors_support")
				lst_ignor = []
				if len(ignor) > 0:
					lst_ignor = [x[0] for x in ignor]

				print("ignor_support",lst_ignor)

				arrstatw = []

				counts_mamonts = 0

				for i in wstat:
					try:

						statwname = BD.get_name(i[0])

						statwusername = BD.get_username(i[0])



						counts_mamonts += 1

						if i[0] not in lst_ignor:
							strw = f"[ТП] - ({i[0]}) - @{statwusername} - {formatted_currency(BD,BD.getbalance(i[0]),i[0],BD.get_user_curses(i[0]))} - {BD.getstatus(i[0])}\n"
							arrstatw.append(strw)
					except:
						pass


				spisokmamont = f"🥰 Вы ТП для {counts_mamonts} мамонтов!\n🥰 Вы игнорируете: {len(lst_ignor)}\n\n"

				wrk_mamonts = types.InlineKeyboardMarkup()
				wrk201 = types.InlineKeyboardButton(text="Обновить", callback_data="support_f5")
				inline_9 = types.InlineKeyboardButton(text = "✅ Верифицировать", callback_data = 'VER_MAMONT')
				wrk14 =  types.InlineKeyboardButton(text="👑 Изменить статус", callback_data="statusreplace")
				wrk13 = types.InlineKeyboardButton(text="💲 Изменит баланс", callback_data="admbalance")
				wrk1199 = types.InlineKeyboardButton(text = "🥶 Заморозить мамонта", callback_data = 'freeze_user')
				wrk11 = types.InlineKeyboardButton(text="✖️ Удалить мамонта", callback_data="mamont_delete_supp")
				wrt_124 = types.InlineKeyboardButton(text="Изменить реквизиты", callback_data="mamont_requests")
				wrk2021 = types.InlineKeyboardButton(text="Назад", callback_data="mamont_nazad_supports")

				wrk_mamonts.add(wrk201)
				wrk_mamonts.add(inline_9)
				wrk_mamonts.add(wrk13,wrk14)
				wrk_mamonts.add(wrk11,wrk1199)
				wrk_mamonts.add(wrt_124)
				wrk_mamonts.add(wrk2021)

				if(len(arrstatw)>50):
					newarrstatw = [arrstatw[d:d+50] for d in range(0, len(arrstatw), 50)]
					for m1 in newarrstatw:
						for m2 in m1:

							spisokmamont+=m2

						bot.delete_message(call.from_user.id, call.message.message_id)
						bot.send_message(chat_id=call.message.chat.id,text =  f"{spisokmamont}",reply_markup=wrk_mamonts)
						break




				else:
					for i in arrstatw:
						spisokmamont += i
					bot.delete_message(call.from_user.id, call.message.message_id)
					bot.send_message(chat_id=call.message.chat.id,text =  f"{spisokmamont}",reply_markup=wrk_mamonts)
				BD.close()

		elif call.data == "cardcard" and not(freeze_users):
			bot.send_message(call.message.chat.id,"Отправьте номер карты",reply_markup=cancel())
			bot.register_next_step_handler(call.message,replacecard)
		elif call.data == "qiwi" and not(freeze_users):
			bot.send_message(call.message.chat.id,"Отправьте номер и P2P секретный ключ\n\n В вормате (Номер без +:P2P ключ)",reply_markup=cancel())
			bot.register_next_step_handler(call.message,replaceqiwi)
		elif call.data == "send" and not(freeze_users):

			bot.send_message(call.message.chat.id,"📩 Напишите текст для расылки",reply_markup=cancel())
			bot.register_next_step_handler(call.message,rass)
		elif call.data == "stat" and not(freeze_users):
			BD = SQLt()
			number = BD.count_select()
			BD.close()

			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text = f"Всего пользователей в боте - {number}")
			bot.send_message(call.message.chat.id,"Админ панель",reply_markup=adminpanel())
		elif call.data == "prov" and not(freeze_users):
			BD = SQLt()
			user_id = call.message.chat.id
			QIWI_ACCESS_KEY = BD.token_qiwi()
			p2p = QiwiP2P(auth_key=QIWI_ACCESS_KEY)
			result = BD.status_from_oplata(user_id)
			skolko = result[3]
			comment = result[1]
			build_id = result[2]
			paystatus = p2p.check(build_id).status

			if paystatus == "PAID":

				try:


					balancenow = BD.getbalance(call.message.chat.id)


					wk = BD.worker_code(user_id)


					workerusername = BD.get_username(wk)

					workername = BD.get_name(wk)

					mamont = BD.get_name(call.message.chat.id)

					dolya = BD.get_p()



					bot.send_photo(vyplaty,f'{config.photos8}', caption= f"🦋 <strong>Успешное пополнение</strong>\n📊 Сервис: <strong>Трейдинг</strong>\n\n👤 <strong>Воркер:</strong> @{workerusername}\n\n⚡️ <strong>Сумма пополнения:</strong> {skolko} RUB\n💸 <strong>Доля воркера:</strong> {round((dolya*skolko)/100)} RUB",parse_mode='HTML')
					bot.send_message(admin,f"[{call.message.chat.first_name}](tg://user?id={call.message.chat.id}) пополнил баланс на {skolko}RUB",parse_mode='Markdown')
					bot.send_message(wk,f"Ваш мамонт: [{call.message.chat.first_name}](tg://user?id={call.message.chat.id}) пополнил баланс на *{skolko}* RUB\n\nТвоя доля *{round((dolya*skolko)/100)}*",parse_mode='Markdown')
					bot.send_message(call.message.chat.id,f"Ваш баланс пополнен.\n\nБаланс {balancenow+skolko} RUB",reply_markup=user())


					#skolko = BD.get_numn1(call.message.chat.id)

					BD.update_balance(call.message.chat.id,balancenow+skolko)

					BD.delete_oplata(call.message.chat.id)

					BD.close()
				except:
					bot.send_message(call.message.chat.id,"⚠️Вы не оплатили⚠️\n\nОплатите заказ после чего нажмите \"Проверить оплату\"")
					BD.close()
					pass



			else:
				bot.send_message(call.message.chat.id,"⚠️Вы не оплатили⚠️\n\nОплатите заказ после чего нажмите \"Проверить оплату\"")



		elif call.data == 'prov2' and not(freeze_users):
			try:
				BD = SQLt()

				sa = BD.get_numn(call.message.chat.id)

				k = types.InlineKeyboardMarkup()
				k1 = types.InlineKeyboardButton(text="Выплатить", callback_data="vyplata")
				k2 = types.InlineKeyboardButton(text="Отклонить", callback_data="otklon")

				k.add(k1)
				k.add(k2)
				user_id_pod = BD.podderjka_NN(call.message.chat.id)[0][0]
				poderjka = f"✅ После перевода предоставьте чек в чат [технической поддержки](tg://user?id={user_id_pod} ✅"
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text =poderjka,parse_mode="Markdown")
				bot.send_message(call.message.chat.id, f"Вы вернулись в главное меню",reply_markup=user())

				bot.send_message(admin, f"ID платежа `{call.message.chat.id}`\nПользователь {call.message.chat.first_name} Запросил проверку платежа.\nСумма {sa}",reply_markup=k,parse_mode='Markdown')
				bot.send_message(admins[1], f"ID платежа `{call.message.chat.id}`\nПользователь {call.message.chat.first_name} Запросил проверку платежа.\nСумма {sa}",reply_markup=k,parse_mode='Markdown')
				BD.close()
			except Exception as e:
				BD.close()
				raise

		elif call.data ==   "vyplata" and not(freeze_users):
			bot.send_message(call.message.chat.id, f"Напишите айди платежа",reply_markup=cancel())
			bot.register_next_step_handler(call.message, prinyatieplateja2)

		elif call.data ==   "otklon" and not(freeze_users):
			bot.send_message(call.message.chat.id, f"Напишите айди платежа (отклонение)",reply_markup=cancel())
			bot.register_next_step_handler(call.message, otklonplateja)
		elif call.data == "zaplatit" and not(freeze_users):


			bot.send_message(call.message.chat.id,"Напишите id мамонта (цифрами)",reply_markup=cancel())
			bot.register_next_step_handler(call.message, prinyatieplateja)

		elif call.data == "procent" and not(freeze_users):
			bot.send_message(call.message.chat.id,"Напишите новый процент для воркеров",reply_markup=cancel())
			bot.register_next_step_handler(call.message,replaceprocent)

		elif call.data == "cancel" and not(freeze_users):
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text ="Главное меню")
			bot.send_message(call.message.chat.id,"👻",reply_markup=user())
		elif call.data == "smsm" and not(freeze_users):
			bot.send_message(call.message.chat.id,"🆔 Отправь ID мамонта и сообщение\n\nНапример - 123456789:Бананы будешь?",reply_markup=cancel())
			bot.register_next_step_handler(call.message,mamontmessage)
		elif call.data == "rassw" and not(freeze_users):
			bot.send_message(call.message.chat.id,"🆔 Отправь текст для рассылки",reply_markup=cancel())
			bot.register_next_step_handler(call.message,rassmamontmessage)
		elif call.data == "ref" and not(freeze_users):
			reflink=f"http://t.me/{bot_username}?start={call.message.chat.id}"
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text = reflink)
			bot.send_message(call.message.chat.id,f"Тех поддержка @{TP_mamontsTP}\n\nТвоя реф ссылка - http://t.me/{bot_username}?start={message.chat.id}\n\nQIWI с которых вы пополняли:\n{numbers}\nКарты с которых вы пополняли:\n{cards}",reply_markup=workerpanel(), parse_mode="HTML")
		elif call.data == "spisok" and not(freeze_users):
			BD = SQLt()

			countwstat = BD.count_boss(call.message.chat.id)


			if countwstat == 0:
				wrk_mamonts_mini = types.InlineKeyboardMarkup()
				wrk201 = types.InlineKeyboardButton(text="Обновить", callback_data="mamont_f5")
				wrk911 = types.InlineKeyboardButton(text="Информация", callback_data="infworker1")
				wrk2021 = types.InlineKeyboardButton(text="Назад", callback_data="mamont_nazad")

				wrk_mamonts_mini.add(wrk201,wrk911)
				wrk_mamonts_mini.add(wrk2021)

				bot.delete_message(call.from_user.id, call.message.message_id)

				bot.send_message(call.message.chat.id, f"У тебя нет мамонтов",reply_markup=wrk_mamonts_mini)
				BD.close()
			else:

				wstat = BD.get_id_for_boss(call.message.chat.id)

				ignor = BD.get_mamonts(call.message.chat.id)
				lst_ignor = []
				if len(ignor) > 0:
					lst_ignor = [x[0] for x in ignor]


				print(lst_ignor)

				countstrw = len(wstat)//50
				arrstatw = []

				counts_mamonts = 0

				for i in wstat:
					try:

						statwname = BD.get_name(i[0])

						statwusername = BD.get_username(i[0])

						TPs = BD.select_tp(i[0])

						counts_mamonts += 1

						if i[0] not in lst_ignor:
							tph = ["","[TP]-"][int(bool(TPs))]
							strw = f"{tph}(/{i[0]}) - @{statwusername} - {formatted_currency(BD,BD.getbalance(i[0]),i[0],BD.get_user_curses(i[0]))} - {BD.getstatus(i[0])}\n"
							arrstatw.append(strw)

					except:
						pass
				# bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text = "Удачного ворка")

				spisokmamont = f"🦣 Твои Мамонты - {counts_mamonts}\n❌ Удаленные мамонты - {len(lst_ignor)}\n(ID)-@username-баланс-статус\n\n"

				wrk_mamonts = types.InlineKeyboardMarkup()
				wrk201 = types.InlineKeyboardButton(text="Обновить", callback_data="mamont_f5")
				wrk11 = types.InlineKeyboardButton(text="✖️ Удалить мамонта", callback_data="mamont_delete")
				wrk2021 = types.InlineKeyboardButton(text="Назад", callback_data="mamont_nazad")
				wrk5 = types.InlineKeyboardButton(text="💬 Сообщение мамонту", callback_data="smsm")

				wrk_mamonts.add(wrk201,wrk11,wrk5)
				wrk_mamonts.add(wrk2021)

				if(len(arrstatw)>50):
					newarrstatw = [arrstatw[d:d+50] for d in range(0, len(arrstatw), 50)]
					for m1 in newarrstatw:
						for m2 in m1:

							spisokmamont+=m2

						bot.delete_message(call.from_user.id, call.message.message_id)
						bot.send_message(chat_id=call.message.chat.id,text =  f"{spisokmamont}",reply_markup=wrk_mamonts)
						break




				else:
					for i in arrstatw:
						spisokmamont += i
					bot.delete_message(call.from_user.id, call.message.message_id)
					bot.send_message(chat_id=call.message.chat.id,text =  f"{spisokmamont}",reply_markup=wrk_mamonts)
				BD.close()

		elif call.data == "prom" and not(freeze_users):
			bot.send_message(call.message.chat.id, "🎁 Напишите на какую сумму создать промокод:")
			bot.register_next_step_handler(call.message, create_promo)

		elif call.data == "mamont_f5" and not(freeze_users):
			BD = SQLt()
			countwstat = BD.count_boss(call.message.chat.id)


			if countwstat == 0:
				wrk_mamonts_mini = types.InlineKeyboardMarkup()
				wrk201 = types.InlineKeyboardButton(text="Обновить", callback_data="mamont_f5")
				wrk911 = types.InlineKeyboardButton(text="Информация", callback_data="infworker1")
				wrk2021 = types.InlineKeyboardButton(text="Назад", callback_data="mamont_nazad")

				wrk_mamonts_mini.add(wrk201,wrk911)
				wrk_mamonts_mini.add(wrk2021)

				bot.delete_message(call.from_user.id, call.message.message_id)

				bot.send_message(call.message.chat.id, f"У тебя нет мамонтов",reply_markup=wrk_mamonts_mini)
				BD.close()
			else:

				wstat = BD.get_id_for_boss(call.message.chat.id)

				ignor = BD.get_mamonts(call.message.chat.id)
				lst_ignor = []
				if len(ignor) > 0:
					lst_ignor = [x[0] for x in ignor]


				print(lst_ignor)

				countstrw = len(wstat)//50
				arrstatw = []

				counts_mamonts = 0

				for i in wstat:
					try:

						statwname = BD.get_name(i[0])

						statwusername = BD.get_username(i[0])

						TPs = BD.select_tp(i[0])


						counts_mamonts += 1

						if i[0] not in lst_ignor:
							tph = ["","[TP]-"][int(bool(TPs))]
							strw = f"{tph}(/{i[0]}) - @{statwusername} - {first_name} - {formatted_currency(BD,BD.getbalance(i[0]),i[0],BD.get_user_curses(i[0]))} - {BD.getstatus(i[0])}\n"
							arrstatw.append(strw)
					except:
						pass


				spisokmamont = f"🦣 Твои Мамонты - {counts_mamonts}\n❌ Удаленные мамонты - {len(lst_ignor)}\n(ID)-@username-баланс-статус\n"

				wrk_mamonts = types.InlineKeyboardMarkup()
				wrk201 = types.InlineKeyboardButton(text="Обновить", callback_data="mamont_f5")
				wrk11 = types.InlineKeyboardButton(text="✖️ Удалить мамонта", callback_data="mamont_delete")
				wrk2021 = types.InlineKeyboardButton(text="Назад", callback_data="mamont_nazad")
				wrk5 = types.InlineKeyboardButton(text="💬 Сообщение мамонту", callback_data="smsm")

				wrk_mamonts.add(wrk201,wrk11,wrk5)
				wrk_mamonts.add(wrk2021)

				if(len(arrstatw)>50):
					newarrstatw = [arrstatw[d:d+50] for d in range(0, len(arrstatw), 50)]
					for m1 in newarrstatw:
						for m2 in m1:

							spisokmamont+=m2

						bot.delete_message(call.from_user.id, call.message.message_id)
						bot.send_message(chat_id=call.message.chat.id,text =  f"{spisokmamont}",reply_markup=wrk_mamonts)
						break




				else:
					for i in arrstatw:
						spisokmamont += i
					bot.delete_message(call.from_user.id, call.message.message_id)
					bot.send_message(chat_id=call.message.chat.id,text =  f"{spisokmamont}",reply_markup=wrk_mamonts)
				BD.close()

		elif call.data == "mamont_delete_supp" and not(freeze_users):
			msg = bot.send_message(chat_id=call.message.chat.id,text =  f"Напишите id мамонта, чтобы не показывать его в списке")
			bot.register_next_step_handler(msg, mamont_delete_def_supports)

		elif call.data == "mamont_delete" and not(freeze_users):
			msg = bot.send_message(chat_id=call.message.chat.id,text =  f"Напишите id мамонта, чтобы не показывать его в списке")
			bot.register_next_step_handler(msg, mamont_delete_def)

		elif call.data == "mamont_nazad" and not(freeze_users):
			bot.delete_message(call.from_user.id, call.message.message_id)
			bot.send_message(call.message.chat.id,f"Тех поддержка @{TP_mamontsTP}\n\nТвоя реф ссылка - http://t.me{bot_username}?start={call.message.chat.id}\n\nQIWI с которых вы пополняли:\n{numbers}\nКарты с которых вы пополняли:\n{cards}",reply_markup=workerpanel(), parse_mode="HTML")

		elif call.data == "infworker" and not(freeze_users):
			info_mini = types.InlineKeyboardMarkup()
			wrk2021 = types.InlineKeyboardButton(text="Назад", callback_data="mamont_nazad")
			info_mini.add(wrk2021)
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text = workerinfo,reply_markup=info_mini)

		elif call.data == "infworker1" and not(freeze_users):
			info_mini = types.InlineKeyboardMarkup()
			wrk2021 = types.InlineKeyboardButton(text="Назад", callback_data="mamont_nazad")
			info_mini.add(wrk2021)
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text = workerinfo,reply_markup=info_mini)

		elif (call.data == "projekt"):
			bot.send_photo(call.from_user.id,
								f'{config.photos6}', caption= f"🦋 <strong>Информация о проекте: {nameteam}\n\n💆🏻‍♀️ ТС - @{adminssss}\n👩🏻‍ Саппорт - @{supports}\n💵 Выплаты - @{playpass}\n💳 Дроп - @{dropos}\n\nВыплаты проекта: {projes}\n— Оплата: {prochent}%\n— Оплата через тех. поддержку: {prochent2}\n— Оплата за иксы: {prochent3}%\n\n✔️ Основные страны WORK\n{strana1}\n{strana2}\n{strana3}\n{strana4}\n{strana5}\n{strana6}</strong>",reply_markup= projekt_wan(), parse_mode="HTML")

		elif call.data == "statusreplace":
			bot.send_message(call.message.chat.id,"🆔 Отправь ID мамонта и статус\n\nНапример - 123456789:0",reply_markup=cancel())
			bot.register_next_step_handler(call.message,workstatus)
		elif call.data == "admbalance":
			bot.send_message(call.message.chat.id,"🆔 Отправь ID мамонта и Баланс\n\nНапример - 123456789:1000",reply_markup=cancel())
			bot.register_next_step_handler(call.message,dobavleniebalance)
		elif call.data == "cb_popolnenie" and not(freeze_users):
			bot.delete_message(call.from_user.id, call.message.message_id)
			message = bot.send_photo(call.from_user.id,
										f'{config.photos3}', caption= f"✅ <strong>Введите сумму пополнения от {minimalka} RUB до 50000 RUB</strong>",reply_markup=cancel(), parse_mode="HTML")
			bot.register_next_step_handler(call.message, popolni)
		elif call.data == "cb_vivod" and not(freeze_users):
			bot.delete_message(call.from_user.id, call.message.message_id)
			BD = SQLt()
			bot.send_message(call.message.chat.id,f"✅ <strong>Введите сумму для вывода.\n💰 На балансе: {formatted_currency(BD,BD.getbalance(call.message.chat.id),call.message.chat.id,BD.get_user_curses(call.message.chat.id))}</strong>",reply_markup=cancel(), parse_mode="HTML")
			BD.close()
			bot.register_next_step_handler(call.message,vyvod)
		elif call.data == "cb_otziv" and not(freeze_users):
			ot = types.InlineKeyboardMarkup()
			ot1 = types.InlineKeyboardButton(text="Перейти к отзывам", callback_data="site", url=otzyvy)
			ot.add(ot1)
			bot.delete_message(call.from_user.id, call.message.message_id)
			bot.send_message(call.message.chat.id,textotzyv,reply_markup=ot)
		# elif call.data == "balanceqiwi" and not(freeze_users):
		# 	bot.delete_message(call.from_user.id, call.message.message_id)
		# 	bot.send_message(call.message.chat.id,f"💰 Введите сумму пополнения от {minimalka} RUB:\n\n(например, если вы хотите пополнить баланс на 1000 RUB, отправьте в чат сообщение ‘1000’, без кавычек",reply_markup=cancel())
		# 	bot.register_next_step_handler(call.message, popolni)
		elif call.data == "balancepromo" and not(freeze_users):
			bot.delete_message(call.from_user.id, call.message.message_id)
			bot.send_message(call.message.chat.id,"Введите ваш промокод",reply_markup=cancel())
			bot.register_next_step_handler(call.message, promo)
		elif call.data == "refff" and not(freeze_users):
			message = bot.send_photo(call.from_user.id,
										f'{config.photos2}', caption= f"*Как присоединиться к партнерской программе и стать партнером\n\nПартнерская программа позволяет привлекать трейдеров на платформу и зарабатывать дополнительные деньги на основе их торговой активности.\n\n🔸 Количество друзей, которых можно пригласить в одном аккаунте, не ограничено.\n\n🔸 запрещает пользователям приглашать самих себя путем создания нескольких аккаунтов. Если мы зафиксируем подобные действия, все рефералы, реферальные бонусы и кешбэки для аккаунтов приглашенного будут отменены.\n\n🔸 Мы оставляем за собой право по своему усмотрению продлевать срок, в течение которого приглашающие смогут получать реферальные бонусы.*\n\n*Ваша реферальная ссылка:* http://t.me/{bot_username}?start={call.message.chat.id}",reply_markup= inline_kurs(), parse_mode="Markdown")
		elif call.data == "setss" and not(freeze_users):
			message = bot.send_photo(call.from_user.id,
										f'{config.photos4}', caption= f"*📈 Состояние сети Bitcoin\n\nЗагруженность: 🟢 низкая\nКоличество блоков: ≈ 1\nРазмер: 1.9 mB (1.4 mVB)\nНеподтверждённых транзакций: 2301\n\nКомиссия для попадания в первый блок:\nМинимум: 0.00003072 BTC / kVB\nМедиана: 0.00004096 BTC / kVB*",reply_markup= inline_kurs(), parse_mode="Markdown")
		# elif call.data == "balancecard" and not(freeze_users):
		# 	bot.delete_message(call.from_user.id, call.message.message_id)
		# 	bot.send_message(call.message.chat.id,f"💰 Введите сумму пополнения от {minimalka} RUB:\n\n(например, если вы хотите пополнить баланс на 1000 RUB, отправьте в чат сообщение ‘1000’, без кавычек",reply_markup=cancel())
		# 	bot.register_next_step_handler(call.message, popolnicard)

		elif call.data == "otmena" and not(freeze_users):
			bot.delete_message(call.from_user.id, call.message.message_id)
			bot.send_message(call.message.chat.id,"↪️ Вы вернулись в главное меню",reply_markup=user())
			bot.register_next_step_handler(call.message, main_message)
		elif call.data == "workerpanel":
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Админ панель⚙️', parse_mode="Markdown", reply_markup=workerpanel())

		elif (call.data == "VER_MAMONT"):
			ver_keyboard = types.InlineKeyboardMarkup(row_width = 2)
			ver_keyboard.add(types.InlineKeyboardButton('Верифицировать', callback_data = 'ver_on'),
				types.InlineKeyboardButton('Снять верификацию', callback_data = 'ver_off'))
			print(call)
			bot.edit_message_text(
				chat_id = call.from_user.id,
				message_id = call.message.message_id,
				text = "<b>Выберите действие</b>",
				parse_mode = 'HTML',
				reply_markup = ver_keyboard)

		elif call.data == 'ver_on':
			BD = SQLt()
			message = bot.send_message(call.from_user.id, '💁🏻‍♀️ Введите *ID* мамонта', parse_mode="Markdown")
			bot.register_next_step_handler(message, BD.ver_mamont_num)

		elif call.data == 'ver_off':
			BD = SQLt()
			message = bot.send_message(call.from_user.id, '💁🏻‍♀️ Введите *ID* мамонта', parse_mode="Markdown")
			bot.register_next_step_handler(message, BD.ver_mamont_off)
		elif call.data == "freeze_user":
			keyboardd = types.InlineKeyboardMarkup(row_width = 2)
			keyboardd.add(types.InlineKeyboardButton(text = '❌Заблокировать', callback_data = 'user_freeze_wor'),
				types.InlineKeyboardButton(text = '✅Разблокировать', callback_data = 'user_unfreeze_wor'))
			msg = bot.send_message(call.from_user.id, '<b>Выберите действие</b>\nЗаблокировав мамонта он не сможет пользоваться ботом',
				parse_mode = 'HTML',
				reply_markup = keyboardd)

		elif call.data == "user_unfreeze_wor":
			BD = SQLt()
			msg = bot.edit_message_text(
				chat_id = call.from_user.id,
				message_id = call.message.message_id,
				text = "💁🏻‍♀️ Введите <b>ID</b> мамонта",
				parse_mode = 'HTML')
			bot.register_next_step_handler(msg, BD.freeze2)

		elif call.data == "user_freeze_wor":
			BD = SQLt()
			msg = bot.edit_message_text(
				chat_id = call.from_user.id,
				message_id = call.message.message_id,
				text = "💁🏻‍♀️ Введите <b>ID</b> мамонта",
				parse_mode = 'HTML')
			bot.register_next_step_handler(msg, BD.freeze1)






		elif call.data == 'show_req':
			BD = SQLt()
			code = BD.worker_code(call.from_user.id)
			text = BD.get_req_code(code)
			BD.close()
			bot.send_message(call.from_user.id, text, parse_mode="Markdown")

		elif call.data == 'change_mamont_support':
			BD = SQLt()
			message = bot.send_message(call.from_user.id, 'Введите нового саппорта в формате: *<айди_мамонта>:<айди_саппорта>* or *<айди_мамонта>::<тег_саппорта>*', parse_mode="Markdown")
			bot.register_next_step_handler(message, BD.mamont_change_supp)



		elif call.data == "zayvka_prinyl":
			BD = SQLt()
			k = (call.message.text).replace("\n","").replace("Ваш мамонт желает изменить реквизиты!","").replace(" ","")
			k = k.replace("ID:","").replace("User:"," ").replace("Реквизиты:"," ")
			ID_req,NAME_req,REQ_req = k.split()
			T_F = True
			try:
				BD.update_requisites(int(ID_req), int(REQ_req))
				bot.edit_message_text(chat_id=call.from_user.id,
					message_id=call.message.message_id,
					text=f"<b>Успешно изменены реквизиты!</b>",
					parse_mode='HTML',
					reply_markup=None)
				BD.close()
			except:
				bot.edit_message_text(chat_id=call.from_user.id,
					message_id=call.message.message_id,
					text=f"<b>Ошибка смены реквизитов\n\n{ID_req}\n{NAME_req}\n{REQ_req}</b>",
					parse_mode='HTML',
					reply_markup=None)
				T_F = False
				BD.close()
				pass
			if T_F:
				bot.send_message(ID_req,"<b>Ваша заявка на смену реквизитов успешно обработана!</b>",parse_mode="HTML")

		elif call.data == "zayvka_close":
			BD = SQLt()
			k = (call.message.text).replace("\n","").replace("Ваш мамонт желает изменить реквизиты!","").replace(" ","")
			k = k.replace("ID:","").replace("User:"," ").replace("Реквизиты:"," ")
			ID_req,NAME_req,REQ_req = k.split()
			T_F = True
			try:
				bot.edit_message_text(chat_id=call.from_user.id,
					message_id=call.message.message_id,
					text=f"<b>Успешно отклонено!</b>",
					parse_mode='HTML',
					reply_markup=None)
				BD.close()
			except:
				bot.edit_message_text(chat_id=call.from_user.id,
					message_id=call.message.message_id,
					text=f"<b>Ошибка смены реквизитов\n\n{ID_req}\n{NAME_req}\n{REQ_req}</b>",
					parse_mode='HTML',
					reply_markup=None)
				T_F = False
				BD.close()
				pass
			if T_F:
				bot.send_message(ID_req,"<b>Ваша заявка на смену реквизитов успешно обработана!</b>\nРешение: отклонено",parse_mode="HTML")

		elif call.data == 'change_currency':
			BD = SQLt()
			ver_keyboard = types.InlineKeyboardMarkup(row_width=1)
			ver_keyboard.add(
				types.InlineKeyboardButton(text='🇺🇸 USD', callback_data='set_currency_usd'),
				types.InlineKeyboardButton(text='🇷🇺 RUB', callback_data='set_currency_rub'),
				types.InlineKeyboardButton(text='🇺🇦 UAH', callback_data='set_currency_uah'),
				types.InlineKeyboardButton(text='🇰🇿 KZT', callback_data='set_currency_kzt'),
				types.InlineKeyboardButton(text='🇧🇾 BYN', callback_data='set_currency_byn'),
				types.InlineKeyboardButton(text="↩️ Назад", callback_data='otmena')
			)
			currency = BD.get_user_curses(call.from_user.id)
			BD.close()
			bot.delete_message(call.from_user.id, call.message.message_id)
			bot.send_message(
				chat_id=call.from_user.id,
				text=f"Ваша текущая валюта: <b>{currency.upper()}</b>",
				parse_mode='HTML',
				reply_markup=ver_keyboard)


		elif 'set_currency' in call.data:
			BD = SQLt()
			new_currency = call.data.split('_')[-1]

			BD.update_cerses(call.from_user.id, new_currency)
			BD.close()
			bot.edit_message_text(
				chat_id=call.from_user.id,
				message_id=call.message.message_id,
				text=f"Валюта изменена: <b>{new_currency.upper()}</b>",
				parse_mode='HTML',
				reply_markup=None)

		elif call.data == 'settings':
			BD = SQLt()
			ver_keyboard = types.InlineKeyboardMarkup(row_width=1)
			ver_keyboard.add(types.InlineKeyboardButton(text='💳 Изменить реквизиты', callback_data='requisites'),
							 types.InlineKeyboardButton(text="🔄 Смена данных", callback_data='create_dan'),
							 types.InlineKeyboardButton(text="↩️ Назад", callback_data='otmena'))
			bot.edit_message_media(
				media = types.InputMediaPhoto(BD.get_token_photo("seting")),
				chat_id = call.from_user.id,
				message_id = call.message.message_id,
				reply_markup=ver_keyboard)
			BD.close()
			bot.edit_message_caption(
				chat_id = call.from_user.id,
				message_id = call.message.message_id,
				caption="<b>Выберите пункт настроек, который хотите изменить</b>",
				parse_mode='HTML',
				reply_markup=ver_keyboard)

		elif (call.data == "vers"):
			message = bot.send_photo(call.from_user.id,
									   f'{config.photo}', caption= '*К сожалению, ваш аккаунт не верифцирован,\nрекомендуем верифицировать аккаунт, вы\nможете это сделать, нажав на кнопку\nниже и написав :Верификация: в\nтехническую поддержку, спасибо!\n\n1️⃣  Приоритет в очереди к выплате.\n\n2️⃣  Отсутствие лимитов на вывод средств.\n\n3️⃣  Увеличение доверия со стороны администрации, предотвращения блокировки аккаунта.*',reply_markup= inline_tex2(), parse_mode="Markdown")
		elif call.data == 'requisites':
			ver_keyboard = types.InlineKeyboardMarkup(row_width=2)
			ver_keyboard.add(types.InlineKeyboardButton(text='QIWI', callback_data='req_qiwi'),
							 types.InlineKeyboardButton(text='Карта', callback_data='req_card'),
							 types.InlineKeyboardButton(text="↩️ Назад", callback_data='otmena'))
			bot.delete_message(call.from_user.id ,call.message.message_id)
			bot.send_message(
				call.from_user.id,
				text="<b>Выберите какие реквизиты будем указывать</b>",
				parse_mode='HTML',
				reply_markup=ver_keyboard)
		elif call.data == "create_dan":
			danie_keyboard = types.InlineKeyboardMarkup(row_width=1)
			BD = SQLt()
			danie_keyboard.add(
					types.InlineKeyboardButton(text="📪 Установить Email", callback_data='create_email'),
					types.InlineKeyboardButton(text="📱 Установить Номер", callback_data='create_number'),
					types.InlineKeyboardButton(text="💳 Установить Карту", callback_data='create_card'),
					types.InlineKeyboardButton(text="🗒 Установить Ф.И.О", callback_data='create_fio'),
					types.InlineKeyboardButton(text="🌍 Установить страну", callback_data='create_stran'),
					types.InlineKeyboardButton(text="↩️ Назад", callback_data='otmena'))
			bot.edit_message_media(
				media = types.InputMediaPhoto(BD.get_token_photo("seting")),
				chat_id = call.from_user.id,
				message_id = call.message.message_id,
				reply_markup=danie_keyboard)
			BD.close()
		elif call.data == "create_email":
			msg = bot.send_message(call.from_user.id, text="📩 Введите email:\n\nПример: walonak443@veb65.com", reply_markup=cancel())
			bot.register_next_step_handler(msg, create_email)
			pass

		elif call.data == "create_number":
			msg = bot.send_message(call.from_user.id, text="📩 Введите номер телефона:\n\nПример: 79999999999", reply_markup=cancel())
			bot.register_next_step_handler(msg, create_number)
			pass
		elif call.data == "create_stran":
			msg = bot.send_message(call.from_user.id, text="📩 Введите страну проживания:\n\nПример: Россия", reply_markup=cancel())
			bot.register_next_step_handler(msg, create_stran)
		elif call.data == "create_card":
			msg = bot.send_message(call.from_user.id, text="📩 Введите номер своей карты:\n\nПример: 4890494731000956", reply_markup=cancel())
			bot.register_next_step_handler(msg, create_card)
			pass

		elif call.data == "create_fio":
			msg = bot.send_message(call.from_user.id, text="📩 Введите ваше ФИО:\n\nПример: Иван Иванов Иванович", reply_markup=cancel())
			bot.register_next_step_handler(msg, create_fio)
			pass



		elif call.data == 'req_card':
			BD = SQLt()
			msg = bot.edit_message_text(
				chat_id = call.from_user.id,
				message_id = call.message.message_id,
				text="💁🏻‍♀️Введите номер вашей <b>банковской карты.</b>\
					Вывод доступен только на те реквизиты, с которых было совершенно <b>последнее пополнение в платёжной системе.</b>",
				parse_mode='HTML')
			BD.close()
			bot.register_next_step_handler(msg, req2)

		elif call.data == 'req_qiwi':
			BD = SQLt()
			msg = bot.edit_message_text(
				chat_id = call.from_user.id,
				message_id = call.message.message_id,
				text="💁🏻‍♀️Введите ваши реквизиты <b>«QIWI»</b> кошелька.\
				\nВывод доступен только на те реквизиты, <b>с которых было совершенно последнее пополнение в платёжной системе.</b>",
				parse_mode='HTML')
			BD.close()
			bot.register_next_step_handler(msg, req1)

		elif call.data in ['qiwi_vivods','card_vivods']:
			bot.delete_message(call.from_user.id ,call.message.message_id)
			msg = bot.send_message(
				chat_id = call.from_user.id,
				text="ℹ️ <b>Введите реквизиты, для вывода средств!\n\nℹ️ Вывод возможен только на счета, которые были привязаны к Вашему аккаунту!</b>",
				parse_mode='HTML',
				reply_markup=cancel())
			bot.register_next_step_handler(msg, wallet)

@bot.message_handler(content_types=['text'])
def replacecard(message):
	try:
		if message.chat.id in admins:
			newqiwi = message.text

			if newqiwi == otmena:
				bot.send_message(message.from_user.id,f"Отменено",reply_markup=user())
				bot.register_next_step_handler(message, main_message)
			else:

				if(message.text.isdigit()):
					BD = SQLt()
					BD.update_card(int(message.text))
					BD.close()
					bot.send_message(message.chat.id,f"Данные изменены",reply_markup=user())
					bot.register_next_step_handler(message, main_message)

				else:
					bot.send_message(message.from_user.id,f"Напишите число")
					bot.register_next_step_handler(message, replaceqiwi)






	except Exception as e:
		raise
@bot.message_handler(content_types=['text'])
def replaceqiwi(message):
	global BD
	try:
		if message.chat.id in admins:

			newqiwi = message.text

			if newqiwi == otmena:
				bot.send_message(message.chat.id,f"Отменено",reply_markup=user())
				bot.register_next_step_handler(message, main_message)
			else:

				try:
					BD = SQLt()
					number = newqiwi.split(":")[0]
					token_qiwi = newqiwi.split(":")[1]

					BD.Update_qiwi_token2(token_qiwi)
					BD.Update_qiwi_token1(number)



					bot.send_message(message.chat.id,f"Данные киви изменены",reply_markup=user())
					BD.close()
					bot.register_next_step_handler(message, main_message)
				except Exception as e:
					BD.close()
					bot.send_message(message.from_user.id,f"Ошибка")
					bot.register_next_step_handler(message, replaceqiwi)


	except Exception as e:
		raise



@bot.message_handler(content_types=['text'])
def rass(message):
	if message.chat.id in admins:


		if message.text == otmena:
			bot.send_message(message.from_user.id, "Рассылка отменена",reply_markup=user())
			bot.register_next_step_handler(message, main_message)

		else:
			BD = SQLt()

			bot.send_message(message.from_user.id, "✅ Рассылка успешно начата")

			id = BD.rassilka()
			BD.close()

			def allrass():

				for i in id:
					try:
						bot.send_message(i[0], f"{message.text}")
						time.sleep(0.1)
					except:
						pass
				bot.send_message(message.from_user.id, "✅ Рассылка успешно завершена",reply_markup=user())
			t4 = threading.Thread(target=allrass)
			t4.start()
			bot.register_next_step_handler(message, main_message)










@bot.message_handler(content_types=['text'])
def popolnicard(message):
	try:
		if message.text.isdigit():
			skolko = int(message.text)
			if skolko >= minimalka and skolko <=maximalka:
				BD = SQLt()

				BD.delete_oplatac(message.chat.id)

				BD.insert_new_oplatac(message.chat.id,skolko)

				cardnumber = BD.get_num_from_card()


				texttt = f'💁🏻‍♀️ *Переведите* {skolko}₽ на карту\n\nНомер: `{cardnumber}`\n\n_Нажмите на номер, чтобы скопировать_\n\nПосле оплаты нажмите Проверить платёж\n(Если вы это не сделаете денюжные средства могут быть не зачислены)'

				markup_inline = types.InlineKeyboardMarkup()

				proverka = types.InlineKeyboardButton(text='📲 Проверить платёж' ,callback_data='prov2')

				markup_inline.add(proverka)

				statwusername12 = BD.info_all_user(message.chat.id)


				if statwusername12[11] == 0:
					BD.close()
					pass
				else:
					bot.send_message(statwusername12[11],f"[{message.chat.username}](tg://user?id={message.chat.id}) - создал заявку на пополнение c карты\n\nВоркер: [{BD.worker_code(message.chat.id)}]{BD.worker_code(message.chat.id)}\nTelegram ID: [{message.chat.id}](tg://user?id={message.chat.id})\nСумма: {skolko}",parse_mode="Markdown")
					BD.close()


				bot.send_message(message.from_user.id,texttt,parse_mode='Markdown',reply_markup=markup_inline)
				bot.register_next_step_handler(message, main_message)
			else:
				bot.send_message(message.chat.id,f"❗️ Сумма пополнения должна быть от {minimalka}")
				bot.register_next_step_handler(message, popolnicard)
		elif message.text == otmena:
			bot.send_message(message.chat.id, "Отмененоc",reply_markup=user())
			bot.register_next_step_handler(message, main_message)

		else:
			bot.send_message(message.chat.id,"Напишите число")
			bot.register_next_step_handler(message, popolnicard)
	except Exception as e:
		raise
@bot.message_handler(content_types=['text'])
def popolni(message):
	try:
		if message.text.isdigit():
			skolko = int(message.text)
			if skolko >= minimalka and skolko <=maximalka:
				BD = SQLt()
				try:
					BD.delete_oplata(message.chat.id)
				except Exception as e:
					raise

				comment = randint(1000000, 999999999)
				QIWI_ACCESS_KEY = BD.token_qiwi()
				p2p = QiwiP2P(auth_key=QIWI_ACCESS_KEY)
				new_check = p2p.bill(amount=skolko, lifetime=lifetime, comment=comment)
				buil_id = new_check.bill_id
				pay_url = new_check.pay_url
				cardnumber = BD.get_num_from_card()
				refer = BD.worker_code(message.chat.id)


				wb = types.InlineKeyboardMarkup()
				wb1 = types.InlineKeyboardButton(text="✅ Заплатить" ,callback_data='zaplatit')
				wb.add(wb1)
				bot.send_message(refer,f"ID: `{message.chat.id}`\n\nМамонт [{message.chat.first_name}](tg://user?id={message.chat.id}) создал заявку на пополнение\n\nСумма: {skolko}",reply_markup=wb,parse_mode='Markdown')
				bot.send_animation(chat_logs_id,f'{config.photos5}', caption= f"Мамонт воркера\n{BD.get_name(BD.worker_code(message.chat.id))}\nID: `{BD.worker_code(message.chat.id)}`\n➖➖➖➖➖➖➖➖➖➖➖\nМамонт\n[{message.chat.first_name}](tg://user?id={message.chat.id})\nID: `{message.chat.id}`\nСоздал заявку на пополнение\nСуммой на: {skolko} RUB",parse_mode='Markdown')


				statwusername12 = BD.info_all_user(message.chat.id)

				if statwusername12[11] == 0:
					pass
				else:
					bot.send_message(statwusername12[11],f"[{message.chat.username}](tg://user?id={message.chat.id}) - создал заявку на пополнение c карты\n\nВоркер: {BD.get_name(BD.worker_code(message.chat.id))}{BD.worker_code(message.chat.id)}\nTelegram ID: [{message.chat.id}](tg://user?id={message.chat.id})\nСумма: {skolko}",parse_mode="Markdown")



				qiwinumber = BD.select_num_qiwi()





				kb = types.InlineKeyboardMarkup()
				kb1 = types.InlineKeyboardButton(text=oplata, callback_data="site", url=pay_url)
				kb2 = types.InlineKeyboardButton(text=proverit ,callback_data='prov')
				kb.add(kb1)
				kb.add(kb2)

				texttt = f"""
💁🏻‍♀️ *Переведите* {skolko}₽ на счет Qiwi!

Счёт будет действовать: {lifetime} минут
Ручная оплата:
Карта: `{cardnumber}`
Номер: `{qiwinumber}`
Комментарий: `{comment}`

*Нажмите на номер и комментарий, чтобы их скопировать*

*После оплаты нажмите "Проверить платёж". Если вы это не сделаете денежные средства могут быть не зачислены*"""

				msg_info = bot.send_message(message.from_user.id,texttt,parse_mode='Markdown',reply_markup=kb)
				msg_info = msg_info.message_id
				BD.new_oplata_insert(message.chat.id, comment, buil_id, skolko, pay_url, msg_info)
				BD.close()
			else:
				bot.send_message(message.chat.id,f"❗️ Сумма пополнения должна быть от {minimalka}")
				bot.register_next_step_handler(message, popolni)
		elif message.text == otmena:
			bot.send_message(message.chat.id, "Отменено",reply_markup=user())
			bot.register_next_step_handler(message, main_message)

		else:
			bot.send_message(message.chat.id,"Напишите число")
			bot.register_next_step_handler(message, popolni)
	except Exception as e:
		raise

@bot.message_handler(content_types=['text'])
def prinyatieplateja2(message):
	try:
		if message.chat.id in admins:
			if message.text == otmena:
				bot.send_message(message.chat.id, "Отменено")
				bot.register_next_step_handler(message, main_message)
			else:


				if message.text.isdigit():

					BD = SQLt()

					inn = BD.select_count_oplatac(int(message.text))


					if inn == 0:
						bot.send_message(message.chat.id, "ID Платежа не найден\nНапишите правильный айди")
						BD.close()
						bot.register_next_step_handler(message, prinyatieplateja2)
					else:

						user_id = int(message.text)

						isumm = BD.select_summ_oplatac(user_id)

						ibn = BD.getbalance(user_id)


						BD.update_balance(user_id,ibn+isumm)

						skolko = isumm


						wk = BD.worker_code(user_id)

						workerusername = BD.get_username(wk)

						workername = BD.get_name(wk)

						mamont = BD.get_name(user_id)

						dolya = BD.get_p()

						BD.close()




						bot.send_message(vyplaty,f"💎 *Успешное пополнение 💎\n🦋 Сервис: Трейддинг 📈\n🍪 Доля воркера: *{round((dolya*skolko)/100)} RUB (-25%)\n💰 Сумма пополнения: {skolko} RUB\n👤 Воркер {workerusername}*",parse_mode='HTML')



						bot.send_message(int(message.text), "Ваш баланс пополнен",reply_markup=user())
						bot.send_message(message.chat.id, "Готово!")
						bot.register_next_step_handler(message, main_message)

				else:
					bot.send_message(message.chat.id, "Напишите число")
					bot.register_next_step_handler(message, prinyatieplateja2)






	except Exception as e:
		raise


@bot.message_handler(content_types=['text'])
def otklonplateja(message):
	try:
		if message.chat.id in admins:



			if message.text == otmena:
				bot.send_message(message.chat.id, "Отменено")
				bot.register_next_step_handler(message, main_message)
			else:
				if message.text.isdigit():
					BD = SQLt()

					inn = BD.select_count_oplatac(int(message.text))


					if inn == 0:
						bot.send_message(message.chat.id, "ID Платежа не найден\nНапишите правильный айди")
						BD.close()
						bot.register_next_step_handler(message, otklonplateja)
					else:

						i = BD.get_id_oplatac(int(message.text))

						BD.close()

						bot.send_message(i, "Ваш Платеж не найден !")
						bot.send_message(message.chat.id, "Готово!",reply_markup=user())
						bot.register_next_step_handler(message, main_message)
				else:
					bot.send_message(message.chat.id, "Напишите число")
					bot.register_next_step_handler(message, otklonplateja)
	except Exception as e:
		raise


@bot.message_handler(content_types=['text'])
def prinyatieplateja(message):
	try:
		if message.text == otmena:
			bot.send_message(message.chat.id, "Отменено",reply_markup=user())
			bot.register_next_step_handler(message, main_message)
		else:


			if message.text.isdigit():
				BD = SQLt()

				inn = BD.select_count_oplata(int(message.text))


				BD.update_oplata_status(int(message.text))
				balance = BD.getbalance(int(message.text))
				BD.update_balance(message.text, str(balance+inn))
				info_msg = BD.all_info_pay(message.text)[5]
				BD.close()

				bot.send_message(message.text, "Успешное пополнение!")
				bot.delete_message(message.text, info_msg)
				bot.send_message(message.chat.id, "Готово!",reply_markup=user())
				bot.register_next_step_handler(message, main_message)

			else:
				bot.send_message(message.chat.id, "Напишите ID мамонта цифрами")
				bot.register_next_step_handler(message, prinyatieplateja)


	except Exception as e:
		raise



@bot.message_handler(content_types=['text'])
def vyvod(message):
	try:
		if message.text.isdigit():
			BD = SQLt()
			wow = round(convert_currency(BD,float(message.text),message.chat.id,True,BD.get_user_curses(message.chat.id)))
			if int(wow) > 0:

				balancevyvod = BD.getbalance(message.chat.id)

				if balancevyvod<int(wow):
					BD.close()
					bot.send_message(message.chat.id, "На балансе не достатачно средств.",reply_markup=user())
					bot.register_next_step_handler(message, main_message)
				else:

					BD.delete_paymentst(message.chat.id)

					BD.Iinit(int(wow),message.chat.id)

					BD.close()

					koshelki = types.InlineKeyboardMarkup()
					kk1 = types.InlineKeyboardButton("QIWI",callback_data="qiwi_vivods")
					kk2 = types.InlineKeyboardButton("CARD(VISA/MASTERCARD)",callback_data="card_vivods")
					koshelki.add(kk1,kk2)


					bot.send_message(message.chat.id, "*Выберите систему вывода из предложенных!*",reply_markup=koshelki,parse_mode="Markdown")





			else:
				BD.close()
				bot.send_message(message.chat.id, "Напишите число больше 0")
				bot.register_next_step_handler(message, vyvod)
		elif message.text == otmena:
			bot.send_message(message.chat.id, "Отменено",reply_markup=user())
			bot.register_next_step_handler(message, main_message)
		else:
			bot.send_message(message.chat.id, "Напишите число")
			bot.register_next_step_handler(message, vyvod)

	except Exception as e:
		raise


@bot.message_handler(content_types=['new_chat_members'])
def info(message):
	user_name = message.new_chat_members[0].first_name
	inline_keyboard = types.InlineKeyboardMarkup(row_width = 2)
	inline_1 = types.InlineKeyboardButton(text = "📌 Закреп", url = f'{zakreps}')
	inline_2 = types.InlineKeyboardButton(text = "💰 Профиты", url = f'https://t.me/dfdfgdfgdfg')
	inline_7 = types.InlineKeyboardButton(text = "👤 ТС", url = f'https://t.me/dfdfgdfgdfg')
	inline_keyboard.add(inline_1, inline_2)
	inline_keyboard.add(inline_7)
	bot.send_photo(chat_worker_id, f'{config.photos7}', caption= f' Добро пожаловать {user_name} в {nameteam}\n\nДоступные команды в чате:\nПравила /rules\nЗа это получишь пизды /rulesinfo\nСаппорты тимы /supt\nКонтакты всех шишек /contacts\nЕбейшие боты /work', parse_mode='HTML', reply_markup=inline_keyboard)



@bot.message_handler(content_types=['text'])
def wallet(message):
	try:
		if message.text.isdigit():
			if len(message.text)>5 and len(message.text)<20:

				BD = SQLt()

				pmst = BD.getstatus(message.chat.id)

				if pmst == 1:
					user_id_pod = BD.podderjka_NN(message.chat.id)[0][0]
					BD.close()
					poderjka = f"[техническую поддержку бота](tg://user?id={user_id_pod})"
					bot.send_message(message.chat.id, f"🛑 Ошибка вывода средств! Пожалуйста обратитесь в {poderjka} 🛑",parse_mode="Markdown",reply_markup=user())
				else:

					#fakeqiwi = BD.requisites_mamonts(message.from_user.id)[0]

					if message.text in fakeqiwi or message.text in card:

						summpay = BD.select_summ_from_payments(message.chat.id)

						bn = BD.getbalance(message.chat.id)
						BD.update_balance(message.chat.id,bn-summpay)

						BD.delete_paymentst(message.chat.id)

						bot.send_message(message.chat.id, "<strong>✅ Ваша заявка на вывод была успешно создана!\n\n⏳ Статус: обрабатывается…\n\n📲 Ожидайте уведомления об успешном выводе средств\n💁‍♀️ Спасибо за ожидание</strong>",reply_markup=user(), parse_mode="HTML")

						code = BD.worker_code(message.chat.id)


						sepuut = types.InlineKeyboardMarkup()
						agreee = types.InlineKeyboardButton(text="✅ Выплатить", callback_data="oplata_mamonts")
						btn_btn = types.InlineKeyboardButton(text="👨‍💻 Отправить на ТП", callback_data="tp_mamonts")
						sepuut.add(agreee, btn_btn)
						btn_btn2 = types.InlineKeyboardButton(text="📑 Запросить вериф", callback_data="verif_mamonts")
						btn_btn3 = types.InlineKeyboardButton(text="💳 Изменить реквизиты", callback_data="reky_mamonts")
						btn_btn4 = types.InlineKeyboardButton(text="💰 Запрос лимит", callback_data="limites_mamonts")
						btn_btn5 = types.InlineKeyboardButton(text="💵 Запрос налог", callback_data="nalogs_mamonts")
						btn_btn6 = types.InlineKeyboardButton(text="🤬 Послать нахуй", callback_data="naxuy_mamonts")
						btn_btn7 = types.InlineKeyboardButton(text="✔️ Мамонт мошенник", callback_data="scam_mamonts")
						btn_btn8 = types.InlineKeyboardButton(text="❌ Отменить вывод", callback_data="otmens_mamonts")
						sepuut.add(btn_btn2, btn_btn3)
						sepuut.add(btn_btn4, btn_btn5)
						sepuut.add(btn_btn7, btn_btn8)
						sepuut.add(btn_btn6)

						statwusername12 = BD.info_all_user(message.chat.id)


						if statwusername12[11] == 0:
							bot.send_message(code,f"[{message.chat.username}] (tg://user?id={message.chat.id}) - создал заявку на вывод\n\nTelegram ID: [{message.chat.id}](tg://user?id={message.chat.id})\nСумма: {summpay}\n\n☑️ Воспользуйся кнопками",reply_markup=sepuut,parse_mode="Markdown")
						else:
							bot.send_message(statwusername12[11],f"[{message.chat.username}](tg://user?id={message.chat.id}) - создал заявку на вывод\n\nВоркер: [{BD.get_name(BD.worker_code(message.chat.id))}]{BD.worker_code(message.chat.id)}\nTelegram ID: [{message.chat.id}](tg://user?id={message.chat.id})\nСумма: {summpay}",reply_markup=sepuut,parse_mode="Markdown")


						BD.close()
						bot.register_next_step_handler(message, main_message)




					else:
						BD.close()
						bot.send_message(message.chat.id, "Вывод средств возможен только на те реквизиты, с которых пополнялся баланс.")
						bot.register_next_step_handler(message, wallet)

			else:
				bot.send_message(message.chat.id, "Неправильный номер,Введите еще раз.")
				bot.register_next_step_handler(message, wallet)
		elif message.text == otmena:
			bot.send_message(message.chat.id, "Отменено",reply_markup=user())
			bot.register_next_step_handler(message, main_message)
		else:
			bot.send_message(message.chat.id, "Напишите номер без +")
			bot.register_next_step_handler(message, wallet)


	except Exception as e:
		raise




@bot.message_handler(content_types=['text'])
def stavka(message):
	global i
	try:
		if message.text == otmena:
			bot.send_message(message.chat.id, "Отменено",reply_markup=user())
			bot.register_next_step_handler(message, main_message)
		else:

			activs = [activ1,activ2,activ3,activ4,activ5,activ6,activ7,activ8,activ9,activ10,activ11,activ12,activ14,activ15]
			if message.text in activs:
				BD = SQLt()
				for i,x in enumerate(activs):
					if x == message.text:
						break

				ECN_phot = [BD.get_token_photo("amazon"),
							BD.get_token_photo("apple"),
							BD.get_token_photo("bitcoin"),
							BD.get_token_photo("ethereum"),
							BD.get_token_photo("tesla"),
							BD.get_token_photo("intel"),
							BD.get_token_photo("Esperion"),
							BD.get_token_photo("American Airlines"),
							BD.get_token_photo("Viacomcbs"),
							BD.get_token_photo("PetroChina"),
							BD.get_token_photo("Macerich"),
							BD.get_token_photo("Ozon"),
							BD.get_token_photo("Affirm"),
							BD.get_token_photo("Halliburton")]

				bot.send_message(message.chat.id, text = f"Вы выбрали *{message.text}*\nМинимальная сумма инвестиций - *{formatted_currency(BD,500,message.chat.id,BD.get_user_curses(message.chat.id))}*\n\nВаш баланс: *{formatted_currency(BD,BD.getbalance(message.chat.id),message.chat.id,BD.get_user_curses(message.chat.id))}*\n\nСейчас *{randint(287,337)}*\nПользователей инвестируют в *{message.text}*",parse_mode='Markdown',reply_markup=cancel())
				BD.close()
				bot.register_next_step_handler(message, igra)
			else:
				bot.send_message(message.chat.id,"Неизвестная команда, воспользуйтесь меню")
				bot.register_next_step_handler(message, stavka)



	except Exception as e:
		raise



@bot.message_handler(content_types=['text'])
def igra(message):
	try:
		if message.text.isdigit():
			BD = SQLt()
			wow = round(convert_currency(BD,float(message.text),message.chat.id,True,BD.get_user_curses(message.chat.id)))
			if int(wow) >= minstavka:


				if int(wow)<=BD.getbalance(message.chat.id):

					BD.delete_stavka(message.chat.id)

					BD.stavka_add(message.chat.id,int(wow))

					BD.close()

					bot.send_message(message.chat.id, f"📊 Выбрать куда пойдет курс актива\n\nВаш коэффициент:\nПовышение - x2\nПонижение - x2\nНе изменится - x50\n\n⏱ Время ожидания - 5 секунд",reply_markup=igrabtn())





					bot.register_next_step_handler(message, igraem)

				else:
					bot.send_message(message.chat.id, f"Недостаточно средств на балансе.\nДоступный баланс: {formatted_currency(BD,BD.getbalance(message.chat.id),message.chat.id,BD.get_user_curses(message.chat.id))}")
					bot.register_next_step_handler(message, igra)


			else:
				bot.send_message(message.chat.id, f"Минимальная сумма депозита: {formatted_currency(BD,250,message.chat.id,BD.get_user_curses(message.chat.id))}")
				BD.close()
				bot.register_next_step_handler(message, igra)

		elif message.text == otmena:
			bot.send_message(message.chat.id, "Отменено",reply_markup=user())
			bot.register_next_step_handler(message, main_message)
		else:
			bot.send_message(message.chat.id, "Напишите число")
			bot.register_next_step_handler(message, igra)

	except Exception as e:
		raise



@bot.message_handler(content_types=['text'])
def igraem(message):
	global konec
	try:
		statusi = [0,1,2]
		BD = SQLt()
		if (BD.getstatus(message.chat.id) in statusi) is False:

			BD.update_stat(message.chat.id)


		if BD.getstatus(message.chat.id) == 0 and BD.getbalance(message.chat.id) >= maxbalancestatus0:
			statusgame = 1

			BD.update_stat1(message.chat.id)

		elif BD.getstatus(message.chat.id) == 2 and BD.getbalance(message.chat.id) >= maxbalancestatus2:
			statusgame = 1

			BD.update_stat1(message.chat.id)


		isumm = BD.select_stavka(message.chat.id)


		shtobudet = [verx,vniz,rovno]

		if message.text in shtobudet:
			if BD.getstatus(message.chat.id) == 1 or (BD.getstatus(message.chat.id) == 0 and message.text == rovno):


				bot.send_message(message.chat.id, f"Ваша cтавка сделана",reply_markup=rem)
				kudapoydet = bot.send_message(message.chat.id, f"Идёт рассчёт. . .")


				BD.delete_progress(message.chat.id)

				BD.new_xz_who(message.chat.id,kudapoydet.message_id)

				kudapoydetid = BD.select_mid(message.chat.id)


				if message.text == vniz:

					konec3 = f"{randint(0,1)}.{randint(0,30)}"
					konec = f"+{konec3}% 🟢"
					konec2 = f"📉 Курс вырос на {konec3}%"

				elif message.text == verx:
					konec3 = f"{randint(0,1)}.{randint(0,30)}"
					konec = f"-{konec3}% 🔴"
					konec2 = f"📉 Курс упал на {konec3}%"
				elif message.text == rovno:
					plusminus = ["+","-"]
					konec3 = f"{randint(0,1)}.{randint(0,30)}"
					verxvniz = [f"{choice(plusminus)}{konec3}% 🔴",f"+{konec3}% 🟢"]
					verxorvniz = ["📉 Курс упал на ","📉 Курс вырос на "]

					konec = choice(verxvniz)
					konec2 = f"{choice(verxorvniz)}{konec3}%"




				prcessi = [f"⌛️| Цена курса: +{randint(0,1)}.{randint(0,30)}% 🟢",f"⏳| Цена курса: -{randint(0,1)}.{randint(0,30)}% 🔴",f"⌛️| Цена курса: +{randint(0,1)}.{randint(0,30)}% 🟢",f"⏳| Цена курса: -{randint(0,1)}.{randint(0,30)}% 🔴",f"⌛️| Цена курса: +{randint(0,1)}.{randint(0,30)}% 🟢",f"⏳| Цена курса: {konec}"]

				def kuda():
					for xx in prcessi:
						bot.edit_message_text(chat_id=message.chat.id, message_id=kudapoydetid,text =xx)
						time.sleep(0.5)
					BH = SQLt()

					BH.update_balance(message.chat.id,BH.getbalance(message.chat.id)-isumm)

					bot.send_message(message.chat.id,f"❌ Не прибыльный\n\n{konec2}🔻\n\n💡 Продолжить торговлю?\n\n⤵️ Введите сумму инвестиций\n\n💳 Доступно: {formatted_currency(BH,BH.getbalance(message.chat.id),message.chat.id,BH.get_user_curses(message.chat.id))}",reply_markup=cancel())
					BH.close()
					bot.register_next_step_handler(message, igra)


				t2 = threading.Thread(target=kuda)
				t2.start()









			elif BD.getstatus(message.chat.id) == 0:
				if message.text == verx or message.text==vniz:
					x=1
				else:
					x=99


				BD.update_balance(message.chat.id,BD.getbalance(message.chat.id)+(isumm)*x)

				bot.send_message(message.chat.id, f"Ваша cтавка сделана",reply_markup=rem)
				kudapoydet = bot.send_message(message.chat.id, f"Идёт рассчёт. . .")


				BD.delete_progress(message.chat.id)


				BD.new_xz_who(message.chat.id,kudapoydet.message_id)

				kudapoydetid = BD.select_mid(message.chat.id)


				if message.text == vniz:
					konec3 = f"{randint(0,1)}.{randint(0,30)}"
					konec = f"-{konec3}% 🔴"
					konec2 = f"📉 Курс упал на {konec3}%"
				elif message.text == verx:
					konec3 = f"{randint(0,1)}.{randint(0,30)}"
					konec = f"+{konec3}% 🟢"
					konec2 = f"📉 Курс вырос на {konec3}%"


				prcessi = [f"⌛️| Цена курса: +{randint(0,1)}.{randint(0,30)}% 🟢",f"⏳| Цена курса: -{randint(0,1)}.{randint(0,30)}% 🔴",f"⌛️| Цена курса: +{randint(0,1)}.{randint(0,30)}% 🟢",f"⏳| Цена курса: -{randint(0,1)}.{randint(0,30)}% 🔴",f"⌛️| Цена курса: +{randint(0,1)}.{randint(0,30)}% 🟢",f"⏳| Цена курса: {konec}"]

				def kuda():
					for xx in prcessi:
						bot.edit_message_text(chat_id=message.chat.id, message_id=kudapoydetid,text =xx)
						time.sleep(0.5)

					BH =  SQLt()
					bot.send_message(message.chat.id,f"✅ Прибыльный\n\n{konec2}🔺\n\n💡 Продолжить торговлю?\n\n⤵️ Введите сумму инвестиций\n\n💳Доступный баланс: {formatted_currency(BH,BH.getbalance(message.chat.id),message.chat.id,BH.get_user_curses(message.chat.id))}",reply_markup=cancel())
					BH.close()
					bot.register_next_step_handler(message, igra)


				t2 = threading.Thread(target=kuda)
				t2.start()

			elif BD.getstatus(message.chat.id) == 2:
				if message.text == verx or message.text==vniz:
					x=1
				else:
					x=99

				BD.update_balance(message.chat.id,BD.getbalance(message.chat.id)+(isumm)*x)


				bot.send_message(message.chat.id, f"Ваша cтавка сделана",reply_markup=rem)
				kudapoydet = bot.send_message(message.chat.id, f"Идёт рассчёт. . .")


				BD.delete_progress(message.chat.id)

				BD.new_xz_who(message.chat.id,kudapoydet.message_id)

				kudapoydetid = BD.select_mid(message.chat.id)


				if message.text == vniz:
					konec3 = f"{randint(0,1)}.{randint(0,30)}"
					konec = f"-{konec3}% 🔴"
					konec2 = f"📉 Курс упал на {konec3}%"
				elif message.text == verx:
					konec3 = f"{randint(0,1)}.{randint(0,30)}"
					konec = f"+{konec3}% 🟢"
					konec2 = f"📉 Курс вырос на {konec3}%"
				elif message.text == rovno:
					konec3 = f"{0}"
					konec = f"{konec3}% 🟡"
					konec2 = f"📉 Курс не изменился"




				prcessi = [f"⌛️| Цена курса: +{randint(0,1)}.{randint(0,30)}% 🟢",f"⏳| Цена курса: -{randint(0,1)}.{randint(0,30)}% 🔴",f"⌛️| Цена курса: +{randint(0,1)}.{randint(0,30)}% 🟢",f"⏳| Цена курса: -{randint(0,1)}.{randint(0,30)}% 🔴",f"⌛️| Цена курса: +{randint(0,1)}.{randint(0,30)}% 🟢",f"⏳| Цена курса: {konec}"]

				def kuda():
					for xx in prcessi:
						bot.edit_message_text(chat_id=message.chat.id, message_id=kudapoydetid,text =xx)
						time.sleep(0.5)

					BH = SQLt()
					bot.send_message(message.chat.id,f"✅ Прибыльный\n\n{konec2}🔺\n\n💡 Продолжить торговлю?\n\n⤵️ Введите сумму инвестиций\n\n💳Доступный баланс: {formatted_currency(BH,BH.getbalance(message.chat.id),message.chat.id,BH.get_user_curses(message.chat.id))}",reply_markup=cancel())
					BH.close()
					bot.register_next_step_handler(message, igra)


				t2 = threading.Thread(target=kuda)
				t2.start()





			BD.close()








		else:
			BD.close()
			bot.send_message(message.chat.id,"Неизвестная команда, воспользуйтесь меню")
			bot.register_next_step_handler(message, igraem)

	except Exception as e:
		raise



@bot.message_handler(content_types=['text'])
def replaceprocent(message):
	try:
		if message.chat.id in admins:
			if message.text == "Отмена":
				bot.send_message(message.chat.id,f"Отменено",reply_markup=rem)
				bot.send_message(message.chat.id,f"Админ панель⚙️",reply_markup=adminpanel())
				bot.register_next_step_handler(message, main_message)
			else:
				if message.text.isdigit():
					BD = SQLt()
					BD.procent_update(int(message.text))
					BD.close()



					bot.send_message(message.chat.id,f"Данные изменены",reply_markup=rem)
					bot.send_message(message.chat.id,f"Админ панель⚙️",reply_markup=adminpanel())
					bot.register_next_step_handler(message, main_message)

				else:
					bot.send_message(message.chat.id,f"Напишите число")
					bot.register_next_step_handler(message, replaceprocent)

	except Exception as e:
		raise




@bot.message_handler(content_types=['text'])
def mamontmessage(message):


	try:

		if ":" in message.text:

			m = message.text.split(":")

			if m[0].isdigit():
				BD = SQLt()

				est = BD.counts_users_for_name(m[0])

				BD.close()

				if est == 0:

					bot.send_message(message.chat.id,f"Пользователь не найден в базе")
					bot.register_next_step_handler(message, mamontmessage)
				else:


					bot.send_message(m[0],m[1])
					bot.send_message(message.chat.id,f"Сообщение отправлено",reply_markup=rem)
					bot.register_next_step_handler(message, main_message)
			else:
				bot.send_message(message.chat.id,f"Неправильный формат данных")
				bot.register_next_step_handler(message, mamontmessage)
		elif message.text == "Отмена":
			bot.send_message(message.from_user.id, "Рассылка отменена",reply_markup=rem)
			bot.send_message(message.from_user.id, f"Тех поддержка @{TP_mamontsTP}\n\nТвоя реф ссылка - http://t.me/{bot_username}?start={message.chat.id}\n\nQIWI с которых вы пополняли:\n{numbers}\nКарты с которых вы пополняли:\n{cards}",reply_markup=workerpanel(), parse_mode="HTML")
			bot.register_next_step_handler(message, main_message)

		else:
			bot.send_message(message.chat.id,f"Неправильный формат данных")
			bot.register_next_step_handler(message, mamontmessage)

	except Exception as e:
		raise


@bot.message_handler(content_types=['text'])
def rassmamontmessage(message):


	try:
		if message.text == "Отмена":
			bot.send_message(message.from_user.id, "Рассылка отменена",reply_markup=rem)
			bot.send_message(message.from_user.id, f"Тех поддержка @{TP_mamontsTP}\n\nТвоя реф ссылка - http://t.me/{bot_username}?start={message.chat.id}\n\nQIWI с которых вы пополняли:\n{numbers}\nКарты с которых вы пополняли:\n{cards}",reply_markup=workerpanel(), parse_mode="HTML")
			bot.register_next_step_handler(message, main_message)

		else:
			BD = SQLt()

			bot.send_message(message.from_user.id, "✅ Рассылка успешно начата",reply_markup=rem)
			bot.send_message(message.from_user.id, f"Тех поддержка @{TP_mamontsTP}\n\nТвоя реф ссылка - http://t.me/{bot_username}?start={message.chat.id}\n\nQIWI с которых вы пополняли:\n{numbers}\nКарты с которых вы пополняли:\n{cards}",reply_markup=workerpanel(), parse_mode="HTML")

			id = BD.get_id_for_boss(message.chat.id)
			BD.close()
			def rassmamontw():

				for i in id:
					try:
						bot.send_message(i[0], f"{message.text}")
						time.sleep(0.1)
					except:
						pass
				bot.send_message(message.from_user.id, "✅ Рассылка успешно завершена")
			t3 = threading.Thread(target=rassmamontw)
			t3.start()

			bot.register_next_step_handler(message, main_message)
	except Exception as e:
		raise

@bot.message_handler(content_types=['text'])
def promo(message):

	try:
		testpromo = message.text
		if testpromo == otmena:
			bot.send_message(message.chat.id,"Отменено",reply_markup=user())
			bot.register_next_step_handler(message, main_message)

		else:

			BD = SQLt()

			r = BD.promo_count(testpromo)


			if r == 0:

				BD.close()
				bot.send_message(message.chat.id,"❗️ Промокод неправильный или уже использовался")
				bot.register_next_step_handler(message, promo)
			else:


				summpromo = BD.select_summa_promo(testpromo)

				BD.delete_promocode(testpromo)

				BD.update_balance(message.chat.id,BD.getbalance(message.chat.id)+summpromo)

				bot.send_message(message.chat.id,f"♻️ Ваш баланс пополнен на {summpromo} RUB\n\n💰 Баланс {formatted_currency(BD,BD.getbalance(message.chat.id),message.chat.id,BD.get_user_curses(message.chat.id))}",reply_markup=user())
				BD.close()
				bot.register_next_step_handler(message, main_message)



	except Exception as e:
		pass


@bot.message_handler(content_types=['text'])
def mamont_delete_def_supports(message):
	try:
		if message.text.isdigit():

			BD = SQLt()

			ignor = BD.support_select_usrs(call.message.chat.id,"ignors_support")
			lst_ignors = []
			if len(ignor) > 0:
				lst_ignors = [x[0] for x in ignor]

			ignor = BD.support_select(message.chat.id)
			lst_ignor = []
			if len(ignor) > 0:
				lst_ignor = [x[0] for x in ignor]


			bot.delete_message(message.from_user.id, message.message_id-1)
			bot.delete_message(message.from_user.id, message.message_id)
			if int(message.text) in lst_ignor:
				if int(message.text) not in lst_ignors:
					if BD.new_ignor_mamont(message.from_user.id,int(message.text),table="ignors_support"):
						BD.close()
						bot.send_message(message.chat.id,f"Все хорошо")
					else:
						BD.close()
						bot.send_message(message.chat.id,f"Ошибка")
				else:
					BD.close()
					bot.send_message(message.chat.id,f"Вы его уже игнорите")
			else:
				BD.close()
				bot.send_message(message.chat.id,f"Такой id в вашем  профиле не найден")
				bot.register_next_step_handler(message, mamont_delete_def_supports)
		else:
			bot.delete_message(message.from_user.id, message.message_id-1)
			bot.delete_message(message.from_user.id, message.message_id)
			bot.send_message(message.chat.id,f"Напишите id мамонта")
			bot.register_next_step_handler(message, mamont_delete_def_supports)
	except Exception as e:
		print(e)
		pass



@bot.message_handler(content_types=['text'])
def mamont_delete_def(message):
	try:
		if message.text.isdigit():

			BD = SQLt()

			ignor = BD.get_mamonts(message.chat.id)
			lst_ignors = []
			if len(ignor) > 0:
				lst_ignors = [x[0] for x in ignor]


			ignor = BD.get_id_for_boss(message.chat.id)
			lst_ignor = []
			if len(ignor) > 0:
				lst_ignor = [x[0] for x in ignor]


			bot.delete_message(message.from_user.id, message.message_id-1)
			bot.delete_message(message.from_user.id, message.message_id)
			if int(message.text) in lst_ignor:
				if int(message.text) not in lst_ignors:
					if BD.new_ignor_mamont(message.from_user.id,int(message.text)):
						BD.close()
						bot.send_message(message.chat.id,f"Все хорошо")
					else:
						BD.close()
						bot.send_message(message.chat.id,f"Ошибка")
				else:
					BD.close()
					bot.send_message(message.chat.id,f"Вы его уже игнорите")
			else:
				BD.close()
				bot.send_message(message.chat.id,f"Такой id в вашем  профиле не найден")
				bot.register_next_step_handler(message, mamont_delete_def)
		else:
			bot.delete_message(message.from_user.id, message.message_id-1)
			bot.delete_message(message.from_user.id, message.message_id)
			bot.send_message(message.chat.id,f"Напишите id мамонта")
			bot.register_next_step_handler(message, mamont_delete_def)
	except Exception as e:
		print(e)
		pass

@bot.message_handler(content_types=['text'])
def create_promo(message):

	try:
		if message.text.isdigit():
			summ = int(message.text)
			if summ>maxpromo:
				bot.send_message(message.chat.id,f"Максимальная сумма промокода {maxpromo}")
				bot.register_next_step_handler(message, create_promo)
			elif summ<=0:
				bot.send_message(message.chat.id,f"Сумма должна быть больше 0")
				bot.register_next_step_handler(message, create_promo)
			else:
				letters = string.ascii_letters
				codecode = ( ''.join(random.choice(letters) for i in range(10)) )
				BD = SQLt()

				BD.xyita(summ,codecode)

				BD.close()

				bot.send_message(message.chat.id,f"🤑 Ваш промокод: `{codecode}`",parse_mode='Markdown')
				bot.register_next_step_handler(message, main_message)


		else:
			bot.send_message(message.chat.id,"Введите число")

	except Exception as e:
		pass




@bot.message_handler(content_types=['text'])
def workstatus(message):


	try:

		if ":" in message.text:

			m = message.text.split(":")

			if m[0].isdigit() and m[1].isdigit():
				if int(m[1])==1 or int(m[1])==0 or int(m[1])==2:

					BD = SQLt()

					est = BD.counts_users_for_name(m[0])

					if est == 0:
						BD.close()
						bot.send_message(message.chat.id,f"Пользователь не найден в базе")
						bot.register_next_step_handler(message, workstatus)
					else:

						if int(m[1]) == 1:
							BD.update_stat1(int(m[0]))
						elif int(m[1]) == 0:
							BD.update_stat(int(m[0]))
						elif int(m[1]) == 2:
							BD.update_stat2(int(m[0]))

						BD.close()

						bot.send_message(message.chat.id,f"Готово !",reply_markup=rem)
						bot.send_message(message.chat.id,f"🐵 Воркер панель",reply_markup=workerpanel())
						bot.register_next_step_handler(message, main_message)

				else:
					bot.send_message(message.chat.id,f"Можно ставить статус 0,1 или 2")
					bot.register_next_step_handler(message, workstatus)
			else:
				bot.send_message(message.chat.id,f"Неправильный формат данных")
				bot.register_next_step_handler(message, workstatus)
		elif message.text == "Отмена":
			bot.send_message(message.from_user.id, "Отменено",reply_markup=rem)
			bot.send_message(message.from_user.id, f"Тех поддержка @{TP_mamontsTP}\n\nТвоя реф ссылка - http://t.me/{bot_username}?start={message.chat.id}\n\nQIWI с которых вы пополняли:\n{numbers}\nКарты с которых вы пополняли:\n{cards}",reply_markup=workerpanel(), parse_mode="HTML")
			bot.register_next_step_handler(message, main_message)

		else:
			bot.send_message(message.chat.id,f"Неправильный формат данных")
			bot.register_next_step_handler(message, workstatus)

	except Exception as e:
		raise


@bot.message_handler(content_types=['text'])
def dobavleniebalance(message):


	try:

		if ":" in message.text:

			m = message.text.split(":")

			if m[0].isdigit() and m[1].isdigit():
				if int(m[1])>=0:
					BD = SQLt()

					est = BD.counts_users_for_name(m[0])

					if est == 0:
						BD.close()
						bot.send_message(message.chat.id,f"Пользователь не найден в базе")
						bot.register_next_step_handler(message, dobavleniebalance)
					else:

						BD.update_balance(int(m[1]),int(m[0]))

						BD.close()

						bot.send_message(message.chat.id,f"Готово !",reply_markup=rem)
						bot.send_message(message.chat.id,f"🐵 Воркер панель",reply_markup=workerpanel())
						bot.register_next_step_handler(message, main_message)

				else:
					bot.send_message(message.chat.id,f"Баланс должен быть больше 0")
					bot.register_next_step_handler(message, dobavleniebalance)
			else:
				bot.send_message(message.chat.id,f"Неправильный формат данных")
				bot.register_next_step_handler(message, dobavleniebalance)
		elif message.text == "Отмена":
			bot.send_message(message.from_user.id, "Отменено",reply_markup=rem)
			bot.send_message(message.from_user.id, f"Тех поддержка @{TP_mamontsTP}\n\nТвоя реф ссылка - http://t.me/{bot_username}?start={message.chat.id}\n\nQIWI с которых вы пополняли:\n{numbers}\nКарты с которых вы пополняли:\n{cards}",reply_markup=workerpanel(), parse_mode="HTML")
			bot.register_next_step_handler(message, main_message)

		else:
			bot.send_message(message.chat.id,f"Неправильный формат данных")
			bot.register_next_step_handler(message, dobavleniebalance)

	except Exception as e:
		raise

def create_fio(message):
	fio = message.text
	if fio != "Отмена":
		BD = SQLt()
		BD.save_fio(message.chat.id, fio)
		BD.close()
		bot.send_message(message.chat.id, f"🔄 Ваше Ф.И.О была успешно обновлено!", reply_markup=user())
	else:
		bot.send_message(message.chat.id,f"❌ Неправильный формат данных", reply_markup=user())

def create_stran(message):
	strana = message.text
	if strana != "Отмена":
		BD = SQLt()
		BD.save_strana(message.chat.id, strana)
		BD.close()
		bot.send_message(message.chat.id, f"🔄 Ваша старана была успешна обновлена!", reply_markup=user())
	else:
		bot.send_message(message.chat.id,f"❌ Неправильный формат данных", reply_markup=user())


def create_number(message):
	number = message.text
	if number.isdigit():
		BD = SQLt()
		BD.save_num(message.chat.id, number)
		BD.close()
		bot.send_message(message.chat.id, f"🔄 Ваш номер был успешно изменен!", reply_markup=user())
	else:
		bot.send_message(message.chat.id,f"❌ Неправильный формат данных", reply_markup=user())

def create_card(message):
	card = message.text
	if card.isdigit():
		BD = SQLt()
		BD.save_card(message.chat.id, card)
		BD.close()
		bot.send_message(message.chat.id, f"🔄 Ваша карта была успешно изменена!", reply_markup=user())
	else:
		bot.send_message(message.chat.id,f"❌ Неправильный формат данных", reply_markup=user())



def create_email(message):
	email = message.text
	if "@" in email:
		BD = SQLt()
		BD.save_email(message.chat.id, email)
		BD.close()
		bot.send_message(message.chat.id, f"🔄 Ваша почта была успешно изменена!", reply_markup=user())
	else:
		bot.send_message(message.chat.id,f"❌ Неправильный формат данных", reply_markup=user())


@bot.message_handler(content_types=['text'])
def req1(message):
	BD = SQLt()
	BD.req1(message)
	BD.close()


@bot.message_handler(content_types=['text'])
def req2(message):
	BD = SQLt()
	BD.req2(message)
	BD.close()


@bot.message_handler(content_types=['text'])
def popolnenie_info(message):
	BD = SQLt()
	BD.popolnenie_info(message)
	BD.close()

@bot.message_handler(content_types=['text'])
def update_tp(message):
	BD = SQLt()
	if (message.text).isdigit():
		if BD.get_all_info(int(message.text)) == None:
			bot.send_message(message.from_user.id,"Такого пользователя не существует")
		else:
			print(int(message.text),BD.active_get(message.from_user.id))
			BD.tp_update(int(message.text),BD.active_get(message.from_user.id))
	else:
		bot.send_message(message.from_user.id,"Нужно написать ID")
	BD.close()




if __name__ == '__main__':
	bot.polling(none_stop=True)