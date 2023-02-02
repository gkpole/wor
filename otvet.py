# -*- coding: utf8 -*-
import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import json
from config import maxbalancestatus0,maxbalancestatus2,fakeqiwi,card
from config import TP_mamonts,TP_mamontsVR,linkssssa,livskanal,links2,links3,links4,chatss,manus,profit

pravila = "Политика и условия пользования данным ботом.\n\
1. Перед принятием инвестиционного решения Инвестору необходимо самостоятельно оценить экономические риски и выгоды, налоговые, юридические, бухгалтерские последствия заключения сделки, свою готовность и возможность принять такие риски. Клиент также несет расходы на оплату брокерских и депозитарных услуг\n\
2. Принимая правила, Вы подтверждаете своё согласие со всеми вышеперечисленными правилами!\n\
3. Ваш аккаунт может быть заблокирован в подозрении на мошенничество/обман нашей системы! Каждому пользователю необходима верификация для вывода крупной суммы средств.\n\
4. Мультиаккаунты запрещены!\n\
5. Скрипты, схемы, тактики использовать запрещено!\n\
6. Если будут выявлены вышеперчисленные случаи, Ваш аккаунт будет заморожен до выяснения обстоятельств!\n\
7. В случае необходимости администрация имеет право запросить у Вас документы, подтверждающие Вашу личность и Ваше совершеннолетие.\n\
Вы играете на виртуальные монеты, покупая их за настоящие деньги. Любое пополнение бота является пожертвованием! Вывод денежных средств осуществляется только при достижении баланса, в 5 раз превышающего с сумму Вашего пополнения!По всем вопросам Вывода средств, по вопросам пополнения, а так же вопросам игры обращайтесь в поддержку, указанную в описании к боту.\n\
Пишите сразу по делу, а не «Здравствуйте! Тут?»\n\
Старайтесь изложить свои мысли четко и ясно.\n\n\
Спасибо за понимание, Ваш «Binance Trade»"


workerinfo = f"➖➖➖➖➖➖➖➖➖➖➖➖\nСтатус 1 - всегда проигрыш\n➖➖➖➖➖➖➖➖➖➖➖➖\nСтатус 0 - мамонт будет выигрывать пока у него баланс меньше {maxbalancestatus0},после того как баланс увелечится статус автоматичкесий изменится на 1 - всегда проигрыш\nНа этом статусе ставка на ровно будет проигрыш.\n\
➖➖➖➖➖➖➖➖➖➖➖➖\nСтатус 2 Любая cтавка будет выигрыш пока у него баланс меньше {maxbalancestatus2},после того как баланс увелечится статус автоматичкесий изменится на 1 - всегда проигрыш\n\
➖➖➖➖➖➖➖➖➖➖➖➖\nДефолтом стоит статус - 0\n\nБот для отрисовке чеков @HelperScamBot"
prinyat = "✅ Принять правила"

start = "Добро пожаловать\n\n_«Fast Invest»_\n\n*Надежная и безопасная биржа биткоинов и криптовалют.\nНачните с самой простой и безопасной\nплатформы для заработка криптовалют.\nСтаньте владельцем криптовалюты за считанные минуты*"
start2 = "Мы рады видеть вас снова!"
select = "Выберите криптовалюту для инвестирования:"
qiwiorpromo = "Выберите вариант пополнения баланса"
textotzyv = "Оставить свой отзыв, и прочитать отзывы других пользователей можете тут.\n\nОставьте свой отзыв и получите +5% на следующее пополнение."

naxuy = "Вы можете пойти еще раз нахуй"

userbtn1 = "💹 ECN счёт"
userbtn2 = "👨🏽‍💻 Личный кабинет"
userbtn3 = "💰 Пополнить"
userbtn4 = "💸 Вывести"
userbtn6 = "💬 Отзывы"
userbtn5 = "💻 Техническая Поддержка"
userbtn11 = "ℹ️ Информация"
userbtn52 = "📊 Курс акций"
userbtn53 = "🛒 Купить акцию"

activ1 = "Amazon"
activ2 = "Apple"
activ3 = "Bitcoin"
activ4 = "Etherium"
activ5 = "Tesla"
activ6 = "Intel"
activ7 = "Esperion"
activ8 = "American Airlines"
activ9 = "Viacomcbs"
activ10 = "PetroChina"
activ11 = "Macerich"
activ12 = "Ozon"
activ14 = "Affirm"
activ15= "Halliburton"

otmena = "Отмена"

verx = "Вверх"
vniz = "Вниз"
rovno = "Не изменится"


balanceqiwi= "💳 QIWI"
balancecard = "💳 Банковская карта (RU)"
balancepromo = "💳 Промокод"

oplata = "💳 Оплатить"
proverit = "📲 Проверить платёж"


def inline_kurs():
	k3 = InlineKeyboardMarkup()
	pop3 = types.InlineKeyboardButton(otmena, callback_data = "otmena")
	k3.add(pop3)
	return k3
#oplata
def inline_ofdgdfg():
	k2 = InlineKeyboardMarkup()
	k2_btn1 = InlineKeyboardButton(userbtn3, callback_data="cb_popolnenie")
	pop3 = types.InlineKeyboardButton(otmena, callback_data = "otmena")
	k2.add(k2_btn1)
	k2.add(pop3)
	return k2
#tex
def inline_tex():
	pop = InlineKeyboardMarkup()
	pop334s = types.InlineKeyboardButton(text = "💻 Техническая поддержка", url = f'{TP_mamontsVR}')
	pop3 = types.InlineKeyboardButton(otmena, callback_data = "otmena")
	pop.add(pop334s)
	pop.add(pop3)
	return pop

def projekt_wan():
	infos = InlineKeyboardMarkup()
	inl = types.InlineKeyboardButton(text = "💬 Чат воркеров", url = f'{chatss}')
	inn2 = types.InlineKeyboardButton(text = "📚 Материалы", url = f'{manus}')
	inline_23 = types.InlineKeyboardButton(text = "💰 Профиты", url = f'{profit}')
	infos.add(inl, inn2)
	infos.add(inline_23)
	return infos

def inline_tex2():
	pops = InlineKeyboardMarkup()
	pop33s = types.InlineKeyboardButton(text = "✅ Пройти верификацию", url = f'{TP_mamontsVR}')
	pop31 = types.InlineKeyboardButton(otmena, callback_data = "otmena")
	pops.add(pop33s)
	pops.add(pop31)
	return pops
#menu LK	
def inline_oplata():
	k2 = InlineKeyboardMarkup()
	k2_btn1 = InlineKeyboardButton(userbtn3, callback_data="cb_popolnenie")
	k2_btn2 = InlineKeyboardButton(userbtn4, callback_data="cb_vivod")
	k2_btn3 = InlineKeyboardButton(balancepromo, callback_data = "balancepromo")
	k2_btn6 = InlineKeyboardButton(text="👍 Партнерская программа", callback_data = "refff")
	k2_btn7 = InlineKeyboardButton(text="✅ Верификация", callback_data='vers')
	k2_btn8 = InlineKeyboardButton(text="💱 Сменить валюту", callback_data='change_currency')
	k2_btn4 = InlineKeyboardButton(text='⚙️ Настройки', callback_data='settings')
	k2.add(k2_btn1,k2_btn2)
	k2.add(k2_btn3,k2_btn6)
	k2.add(k2_btn7,k2_btn8)
	k2.add(k2_btn4)
	return k2
	
def inlines_oplatas():
	k7 = InlineKeyboardMarkup()
	k7_btns1 = InlineKeyboardButton(text = "📋 Лицензия", url = f'{linkssssa}')
	k7_btns2 = InlineKeyboardButton(text = "📕 Политика и условия", url = f'{links2}')
	k7_btns3 = InlineKeyboardButton(text = "🤝 Соглашения на обработку данных", url = f'{links3}')
	k7_btns4 = InlineKeyboardButton(text = "ℹ️ О нас", url = f'{links4}')
	k7_btns5 = types.InlineKeyboardButton(otmena, callback_data = "otmena")
	k7_btns6 = InlineKeyboardButton(text="📈 Состояние сети", callback_data = "setss")
	k7.add(k7_btns1,k7_btns2)
	k7.add(k7_btns3,k7_btns4)
	k7.add(k7_btns6)
	k7.add(k7_btns5)
	return k7
	
#game
def igrabtn():
	gamebtn = types.ReplyKeyboardMarkup(True)
	gb1 = types.KeyboardButton(verx)
	gb2 = types.KeyboardButton(vniz)
	gb3 = types.KeyboardButton(rovno)

	gamebtn.add(gb1,gb2)
	gamebtn.add(gb3)

	return gamebtn
#------------ кнопки чата
def inline_test():
	ks3 = InlineKeyboardMarkup()
	ks3_btn1 = InlineKeyboardButton(text = "Бот  для теста", url = 'https://t.me/GogIntimsBot')
	ks3_btn2 = InlineKeyboardButton(text = "Бот  для теста", url = 'https://t.me/GogIntimsBot')
	ks3_btn3 = InlineKeyboardButton(text = "Бот  для теста", url = 'https://t.me/GogIntimsBot')
	ks3_btn4 = InlineKeyboardButton(text = "Бот  для теста", url = 'https://t.me/GogIntimsBot')
	ks3.add(ks3_btn1)
	ks3.add(ks3_btn2)
	ks3.add(ks3_btn3)
	ks3.add(ks3_btn4)
	return ks3

def inline_test2():
	ks4 = InlineKeyboardMarkup()
	ks4_btn1 = InlineKeyboardButton(text = "Контакт тест", url = 'https://t.me/GogIntimsBot')
	ks4_btn2 = InlineKeyboardButton(text = "Контакт тест", url = 'https://t.me/GogIntimsBot')
	ks4_btn3 = InlineKeyboardButton(text = "Контакт тест", url = 'https://t.me/GogIntimsBot')
	ks4_btn4 = InlineKeyboardButton(text = "Контакт тест", url = 'https://t.me/GogIntimsBot')
	ks4.add(ks4_btn1)
	ks4.add(ks4_btn2)
	ks4.add(ks4_btn3)
	ks4.add(ks4_btn4)
	return ks4
	
def inline_test3():
	ks5 = InlineKeyboardMarkup()
	ks5_btn1 = InlineKeyboardButton(text = "саппорт тест", url = 'https://t.me/GogIntimsBot')
	ks5_btn2 = InlineKeyboardButton(text = "саппорт тест", url = 'https://t.me/GogIntimsBot')
	ks5_btn3 = InlineKeyboardButton(text = "саппорт тест", url = 'https://t.me/GogIntimsBot')
	ks5_btn4 = InlineKeyboardButton(text = "саппорт тест", url = 'https://t.me/GogIntimsBot')
	ks5.add(ks5_btn1)
	ks5.add(ks5_btn2)
	ks5.add(ks5_btn3)
	ks5.add(ks5_btn4)
	return ks5
#------------ кнопки чата 
#menu osnova
def user():
	k1 = types.ReplyKeyboardMarkup(True)
	k1_btn1 = types.KeyboardButton(userbtn1) #userbtn1 = "📍 ECN счёт"
	k1_btn2 = types.KeyboardButton(userbtn2) #userbtn2 = "👨🏽‍💻 Личный кабинет"
	k1_btn5 = types.KeyboardButton(userbtn5) #userbtn5 = "🛠 Тех Поддержка"
	k1_btn11 = types.KeyboardButton(userbtn11) #userbtn11 = "⁉️ Вопросы/Ответы"

	k1.add(k1_btn1)	
	k1.add(k1_btn2)
	k1.add(k1_btn11,k1_btn5)
	

	return k1

def akcii():
	act = types.ReplyKeyboardMarkup(True)
	activ_btn1 = types.KeyboardButton(activ1)
	activ_btn2 = types.KeyboardButton(activ2)
	activ_btn3 = types.KeyboardButton(activ3)
	activ_btn4 = types.KeyboardButton(activ4)
	activ_btn5 = types.KeyboardButton(activ5)
	activ_btn6 = types.KeyboardButton(activ6)
	activ_btn8 = types.KeyboardButton(activ7)
	activ_btn9 = types.KeyboardButton(activ8)
	activ_btn10 = types.KeyboardButton(activ9)
	activ_btn11 = types.KeyboardButton(activ10)
	activ_btn12 = types.KeyboardButton(activ11)
	activ_btn13 = types.KeyboardButton(activ12)
	activ_btn15 = types.KeyboardButton(activ14)
	activ_btn16 = types.KeyboardButton(activ15)
	activ_btn7 = types.KeyboardButton(otmena)

	act.add(activ_btn1,activ_btn2)	
	act.add(activ_btn3,activ_btn4)	
	act.add(activ_btn5,activ_btn6)
	act.add(activ_btn8,activ_btn9)
	act.add(activ_btn10,activ_btn11)
	act.add(activ_btn12,activ_btn13)
	act.add(activ_btn15,activ_btn16)
	act.add(activ_btn7)
	return act


def cancel():
	markup = types.ReplyKeyboardMarkup(True)
	key1 = types.KeyboardButton("Отмена")
	markup.add(key1)
	return markup

def popolnenie():
	pop = types.InlineKeyboardMarkup()
	pop1 = types.InlineKeyboardButton(balanceqiwi, callback_data = "balanceqiwi")
	pop4 = types.InlineKeyboardButton(balancecard, callback_data = "balancecard")
	pop3 = types.InlineKeyboardButton(otmena, callback_data = "otmena")

	pop.add(pop1)
	pop.add(pop4)
	pop.add(pop3)
	return pop


def soglashenie() -> object:
	prinyatpravila = types.InlineKeyboardMarkup()
	prinyatpravila_btn1 = types.InlineKeyboardButton(text=prinyat, callback_data="prinyal")
	prinyatpravila.add(prinyatpravila_btn1)
	return prinyatpravila

#------------ Админка ------------
def adminpanel():
	adm = types.InlineKeyboardMarkup()
	adm1 = types.InlineKeyboardButton(text="Изменить Qiwi", callback_data="qiwi")	
	adm65 = types.InlineKeyboardButton(text="Изменить Карту", callback_data="cardcard")	
	adm2 = types.InlineKeyboardButton(text="Статистика", callback_data="stat")
	adm3 = types.InlineKeyboardButton(text="Рассылка", callback_data="send")	
	adm4 = types.InlineKeyboardButton(text="Закрыть", callback_data="cancel")
	adm5 = types.InlineKeyboardButton(text="Изменить процент", callback_data="procent")
	adm6 = types.InlineKeyboardButton(text="Изменить саппорта мамонту", callback_data='change_mamont_support')
	adm.add(adm1)	
	adm.add(adm65)	
	adm.add(adm5)	
	adm.add(adm2)
	adm.add(adm3)	
	adm.add(adm6)
	adm.add(adm4)


	return adm
#------------ Админка ------------
#------------ Ворк ------------
def workerpanel():
	wrk = types.InlineKeyboardMarkup()
	wrk2 = types.InlineKeyboardButton(text="🎉 Создать промо", callback_data="prom")
	wrk7 =  types.InlineKeyboardButton(text="🌈 Список мамонтов", callback_data="spisok")
	wrk12 = types.InlineKeyboardButton(text="❗️Информация про статус❗️", callback_data="infworker")
	wrk71 =  types.InlineKeyboardButton(text="🦋 О проекте", callback_data="projekt")
	wrk3 = types.InlineKeyboardButton(text="Закрыть", callback_data="cancel")
	
	wrk.add(wrk7)
	wrk.add(wrk2, wrk12)
	wrk.add(wrk71)
	wrk.add(wrk3)
	

	return wrk
#------------ ворк ------------




rem = types.ReplyKeyboardRemove()	