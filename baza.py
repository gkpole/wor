import sqlite3

import config

import telebot
from telebot import types
from config import token
import datetime

bot = telebot.TeleBot(token) # токен бота для админов|воркеров

# BD = SQLt() 

class SQLt():
    def __init__(self):
        self.connection = sqlite3.connect("data.db")
        self.cursor = self.connection.cursor()
    
    def delete_promocode(self,test):
        with self.connection:
            self.cursor.execute(f"DELETE  from promocode where code = \'{test}\'")
    
    def select_summa_promo(self,test):
        with self.connection:
            return self.cursor.execute(f"select summa from promocode where code = \'{test}\'").fetchone()[0]

    def promo_count(self,test):
        with self.connection:
            return self.cursor.execute(f"select count(*) from promocode where code = \'{test}\'").fetchone()[0]
    
    def tp_update(self,p,user_id):
        with self.connection:
            self.cursor.execute(f"UPDATE users SET tp = {p} where id = {user_id}")

    def procent_update(self,p):
        with self.connection:
            self.cursor.execute(f"UPDATE procent SET p = {int(p)}")

    def select_mid(self,user_id):
        with self.connection:
            return self.cursor.execute(f"select mid from process where id = {user_id}").fetchone()[0]

    def new_xz_who(self,user_id,mid):
        with self.connection:
            self.cursor.execute(f"INSERT INTO process (id,mid) VALUES ({user_id},{mid})")

    def more_info(self, user_id):
        with self.connection:
            return self.cursor.execute(f"SELECT * from users where id = {user_id}").fetchone()

    def delete_progress(self,user_id):
        with self.connection:
            self.cursor.execute(f"DELETE FROM process WHERE id = {user_id}")

    def select_stavka(self,user_id):
        with self.connection:
            return self.cursor.execute(f"select summ from stavka WHERE id = {user_id}").fetchone()[0]
    
    def update_stat2(self,user_id):
        with self.connection:
            self.cursor.execute(f"UPDATE users SET status = {2} where id = {user_id}")

    def update_stat1(self,user_id):
        with self.connection:
            self.cursor.execute(f"UPDATE users SET status = {1} where id = {user_id}")

    def update_stat(self,user_id):
        with self.connection:
            self.cursor.execute(f"UPDATE users SET status = {0} where id = {user_id}")

    def stavka_add(self,user_id,skolko):
        with self.connection:
            self.cursor.execute(f"INSERT INTO stavka (id,summ) VALUES ({user_id},{int(skolko)})")

    def delete_stavka(self,user_id):
        with self.connection:
            self.cursor.execute(f"DELETE FROM stavka WHERE id = {user_id}")

    def select_summ_from_payments(self,user_id):
        with self.connection:
            return self.cursor.execute(f"select summ from payments WHERE id = {user_id}").fetchone()[0]

    def Iinit(self,wow,user_id):
        with self.connection:
            self.cursor.execute(f"INSERT INTO payments (summ,id) VALUES ({int(wow)},{user_id})")

    def delete_paymentst(self,user_id):
        with self.connection:
            self.cursor.execute(f"DELETE FROM payments WHERE id = {user_id}")

    def update_oplata_status(self,user_id):
        with self.connection:
            self.cursor.execute(f"UPDATE oplata SET status = {1} where id = {user_id}")

    def get_id_oplatac(self,user_id):
        with self.connection:
            return self.cursor.execute(f"select id from oplatac where id = {user_id}").fetchone()[0]


    def select_summ_oplatac(self,user_id):
        with self.connection:
            return self.cursor.execute(f"select summ from oplatac where id = {user_id}").fetchone()[0]

    def select_count_oplatac(self,user_id):
        with self.connection:
            return self.cursor.execute(f"select count(*) from oplatac where id = {user_id}").fetchone()[0]

    def select_count_oplata(self,user_id):
        with self.connection:
            return self.cursor.execute(f"select * from oplata where id = {user_id}").fetchone()[3]

    def select_num_qiwi(self):
        with self.connection:
            return self.cursor.execute("select num from qiwi").fetchone()[0]

    def select_nick_qiwi(self):
        with self.connection:
            return self.cursor.execute("select nick from qiwi").fetchone()[0]

    def new_oplata_insert(self, user_id, commet, status, skolko, pay_url, msg):
        with self.connection:
            self.cursor.execute(f"""INSERT INTO oplata (id, code, status, summ, pay_url, msg_text) VALUES('{user_id}', '{commet}', '{status}', '{skolko}', '{pay_url}', '{msg}')""")
    
    def all_info_pay(self, user_id):
        with self.connection:
            return self.cursor.execute(f"SELECT * FROM oplata where id = {user_id}").fetchone()



    def get_num_from_card(self):
        with self.connection:
            return self.cursor.execute("select num from card").fetchone()[0]

    def insert_new_oplatac(self,user_id,skolko):
        with self.connection:
            self.cursor.execute(f"INSERT INTO oplatac (id,summ) VALUES({user_id},{skolko})")

    def delete_oplatac(self,user_id):
        with self.connection:
            self.cursor.execute(f"DELETE from oplatac where id = {user_id}")

    def rassilka(self):
        with self.connection:
            return self.cursor.execute("SELECT id FROM users").fetchall()


    def Update_qiwi_token1(self,profile):
        with self.connection:
            self.cursor.execute(f"UPDATE qiwi SET num = {profile}")


    def Update_qiwi_token2(self,newqiwi):
        with self.connection:
            self.cursor.execute(f"UPDATE qiwi SET token = \'{newqiwi}\'")


    def update_card(self,num):
        with self.connection:
            self.cursor.execute(f"UPDATE card SET num = {num}")
    
    def xyita(self,summ,codecode):
        with self.connection:
            self.cursor.execute(f"INSERT INTO promocode (summa,code)"
                                    f"VALUES ({summ},\'{codecode}\')")


    def select_tp(self,user_id):
        with self.connection:
            return self.cursor.execute(f"SELECT tp FROM users where id = {user_id}").fetchone()[0]


    def get_mamonts(self,user_id):
        with self.connection:
            return self.cursor.execute(f"SELECT mamont FROM ignors_mamont where user_id = {user_id}").fetchall()

    def get_id_for_boss(self,user_id):
        with self.connection:
            return self.cursor.execute(f"SELECT id FROM users where boss = {user_id}").fetchall()

    def count_boss(self,user_id):
        with self.connection:
            return self.cursor.execute(f"SELECT count(*) FROM users where boss = {user_id}").fetchone()[0]


    def get_numn(self,chat_id):
        with self.connection:
            return self.cursor.execute(f"select summ from oplatac WHERE id = {chat_id}").fetchone()[0]

    def get_p(self):
        with self.connection:
            return self.cursor.execute(f"select p from procent").fetchone()[0]

    def update_balance(self,user_id,balance_up):
        with self.connection:
            self.cursor.execute(f"UPDATE users SET balance = {balance_up} WHERE id = {user_id}")

    def delete_oplata(self,user_id):
        with self.connection:
            self.cursor.execute(f"DELETE FROM oplata WHERE id = {user_id}")



    def token_qiwi(self):
        with self.connection:
            return self.cursor.execute(f"select token from qiwi").fetchone()[0]

    def qiwi_get(self):
        with self.connection:
            return self.cursor.execute("select num from qiwi").fetchone()[0]

    def status_from_oplata(self,user_id):
        with self.connection:
            return self.cursor.execute(f"select * from oplata where id = {user_id}").fetchone()

    def count_select(self):
        with self.connection:
            return self.cursor.execute(f"SELECT COUNT (*) FROM users").fetchone()[0]

    def get_username(self,user_id):
        with self.connection:
            return self.cursor.execute(f"SELECT username FROM users where id = {user_id}").fetchone()[0]

    def get_name(self,user_id):
        with self.connection:
            return self.cursor.execute(f"SELECT name FROM users where id = {user_id}").fetchone()[0]

    def support_select_usrs(self,chat_id,table="ignors_support_otkaz"):
        with self.connection:
            return self.cursor.execute(f"SELECT user_id FROM {table} where id = {chat_id}").fetchall()

    def support_select(self,w=0):
        with self.connection:
            return self.cursor.execute(f"SELECT id FROM users where tp = {w}").fetchall()

    def support_counts(self,suppo):
        with self.connection:
            return self.cursor.execute(f"SELECT count(*) FROM users where tp = {suppo}").fetchone()[0]


    def verifications(self,user_id,b):
        with self.connection:
            self.cursor.execute("UPDATE `users` SET `verif` = ? WHERE `id` = ?" , (b,user_id))
    
    def zreezy(self,b,user_id):
        with self.connection:
            self.cursor.execute("UPDATE `users` SET `freeze` = ? WHERE `id` = ?" , (b,user_id))

    def status_uppdate(self,status,ids):
        with self.connection:
            self.cursor.execute("UPDATE `users` SET `status` = ? WHERE `id` = ?" , (status, ids))
    
    def nacalo_wtf(self):
        with self.connection:
            self.cursor.execute('''CREATE TABLE if not exists card(num int)''')
    
    def nacalo_count_card(self):
        with self.connection:
            return self.cursor.execute(f"select count(*) from card").fetchone()[0]
    def huiny(self):
        with self.connection:
            self.cursor.execute(f"INSERT INTO card (num) "
                f"VALUES ({7777777777})")
    def toje_hyuta(self):
        with self.connection:
            self.cursor.execute('''CREATE TABLE if not exists oplatac(n int,id int,summ int)''')

    def counts_users_for_name(self,name):
        with self.connection:
            return self.cursor.execute(f"select count(*) from users where id = {name}").fetchone()[0]


    def counts_users_for(self,message):
        with self.connection:
            return self.cursor.execute(f"select count(*) from users where id = {message.chat.id}").fetchone()[0]

    def select_ref(self,ref):
        with self.connection:
            return self.cursor.execute(f"select count(*) from users where id = {ref}").fetchone()[0]

    def insert_new_mamonts(self,id,name,boss,user_name):
        with self.connection:
            time_rega = datetime.datetime.now().strftime('%d.%m.%Y')
            self.cursor.execute(f"""INSERT INTO users (id,name,boss, username,balance,status, date_reg) VALUES ("{id}", "{name}", "{boss}", "{user_name}", 0, 0, "{time_rega}")""")

    def select_users_for_ids(self,id_mamonts):
        with self.connection:
            return self.cursor.execute(f"SELECT name FROM users where id = {int(id_mamonts)}").fetchone()[0]
    def active_get(self,user_id):
        with self.connection:
            return self.cursor.execute('SELECT active FROM users WHERE id = ?', (user_id,)).fetchone()[0]

    def active_update(self,message):
        with self.connection:
            self.cursor.execute("UPDATE `users` SET `active` = ? WHERE `id` = ?" , (message.text[1:], message.from_user.id))

    def info_all_user(self,user_id):
        with self.connection:
            return self.cursor.execute(f"SELECT * FROM users where id = {user_id}").fetchone()

    def popolnenie_info(self,message,deystvie = 1):
        if message.text[0] == "-":
            deystvie = 0
            t = message.text[1:]
        else:
            t = message.text[1:]

        with self.connection:
            response = self.cursor.execute('SELECT active FROM users WHERE id = ?', (message.from_user.id,)).fetchone()[0]
        



            if t.isdigit():
                balance_user = self.cursor.execute(f"select balance from users WHERE id = {response}").fetchone()[0]
                ddd = int(balance_user)+( int(  ["-","+"][deystvie]+str(t) ) )


                self.cursor.execute(f"UPDATE users SET balance = {ddd} where id = {response}")



                j = ["Вычли ","Прибавили "][deystvie]+str(t)
               
                bot.send_message(message.from_user.id,f"{j} рублей")
            else:
                bot.send_message(message.from_user.id,"Неправильный формат!\n\nВычесть с баланса \"-500\"\nПрибавить к балансу \"200\" или \"+200\" ")

    def ignor_tp_help(self,user_id_mamont,user_id_tp,table="ignors_support_otkaz"):
        with self.connection:
            return self.cursor.execute(f"INSERT INTO {table} VALUES (?,?)", (user_id_tp,user_id_mamont))

    def update_tp(self,user_id_mamont,user_id_tp):
        with self.connection:
            self.cursor.execute("UPDATE `users` SET `tp` = ? WHERE `id` = ?" , (user_id_tp, user_id_mamont))

    def get_supports_user(self):
        with self.connection:
            return self.cursor.execute('SELECT id FROM Tex_poddejka').fetchall()


    def get_token_photo(self,name):
        with self.connection:
            return self.cursor.execute('SELECT token FROM photo WHERE name_photo = ?',(name,)).fetchone()[0]

    def update_photo_token(self,token_new,name_photo):
        with self.connection:
            return self.cursor.execute("UPDATE `photo` SET `token` = ? WHERE `name_photo` = ?" , (token_new, name_photo))

    def update_requisites1(self,message):
        try:
            msg = message.text.split(':')
            id = int(msg[0])
            number = int(msg[1])
            update_requisites(id, number)
            bot.send_message(message.from_user.id, '<b>Реквизиты обновлены!</b>', parse_mode = 'HTML')
            self.connection.close()
        except Exception as e:
            bot.send_message(message.from_user.id, '<b>Произошла ошибка, возможно вы ввели неправильный ID!</b>',
                parse_mode = 'HTML')
            self.connection.close()
            pass


    def photo_test_load(self):
        with self.connection:
            return self.cursor.execute('SELECT * FROM photo').fetchall()


    def new_ignor_mamont(self,work_id,mamont_id,table="ignors_mamont"):
        try:
            params = (work_id,mamont_id)
            with self.connection:
                self.cursor.execute(f"INSERT INTO {table} VALUES (?,?)", (params))
            return 1
        except:
            return 0


    def update_cerses(self,chat_id,curs):
        with self.connection:
            self.cursor.execute("UPDATE `users` SET `curses_name` = ? WHERE `id` = ?" , (curs.upper(), chat_id))

    def get_currencies(self):
        with self.connection:
            result = dict(USD=0,UAH=0,KZT=0,BYN=0,RUB=0)
            for i in result:
                sql = 'SELECT price FROM curses WHERE name_curs = ?'
                result[i] = self.cursor.execute(sql,(i,)).fetchone()[0]
        return result

    def get_user_curses(self,chat_id):
        with self.connection:         
            return self.cursor.execute('SELECT curses_name FROM users WHERE id = ?', (chat_id,)).fetchone()[0]



    def posts_curses(self,curs_dict):
        for i in curs_dict:
            with self.connection:
                self.cursor.execute("UPDATE `curses` SET `price` = ? WHERE `name_curs` = ?" , (curs_dict[i], i))


    def refka_add(self,user_id_mamont,user_id_boss):
        with self.connection:
            self.cursor.execute("UPDATE `users` SET `refka` = ? WHERE `id` = ?" , (user_id_boss, user_id_mamont))

    def requisites_mamonts(self,chat_id):
        with self.connection:
            sql = 'SELECT requisites FROM users WHERE id = ?'
            response = self.cursor.execute(sql, (int(chat_id),)).fetchone()
        return(response)


    def podderjka_NN(self,chat_id):
        with self.connection:
            sql = "SELECT tp FROM users WHERE id =?"
            response = self.cursor.execute(sql, (int(chat_id),)).fetchall()


            if response[0][0] == 0:
                return [[config.poderjka]]


        return(response)

    def update_requisites_user_id(self,id,code, requisites):
        with self.connection:
            params = (str(id),int(code), int(requisites))
            self.cursor.execute("INSERT INTO requisites VALUES (?,?, ?)", params)
        return 1
    
    def worker_code(self,user_id):
        try:
            with self.connection: 
                result = self.cursor.execute('SELECT * FROM `users` WHERE `id` = ?', (user_id,)).fetchall()
                for row in result:
                    return row[2]
        except:
            pass    


    def req1(self,message):
        with self.connection: 
            result = self.cursor.execute('SELECT * FROM `users` WHERE `id` = ?', (message.from_user.id,)).fetchall()
        
            code = result[0][2]

            number = message.text
            if number.isdigit() and len(number) > 9 and len(number) < 20:

                params = (str(message.from_user.id),int(code), int(number))
                self.cursor.execute("INSERT INTO requisites VALUES (?,?, ?)", params)

                ver_keyboard = types.InlineKeyboardMarkup(row_width=1)
                ver_keyboard.add(
                        types.InlineKeyboardButton(text='Принять', callback_data='zayvka_prinyl'),
                        types.InlineKeyboardButton(text='Отклонить', callback_data='zayvka_close'))
                bot.send_message(code,f"Ваш мамонт желает изменить реквизиты!\n\nID: [{message.from_user.id}](tg://user?id={message.from_user.id})\nUser: {message.from_user.first_name}\nРеквизиты: {number}",parse_mode="Markdown",reply_markup=ver_keyboard)
                bot.send_message(message.from_user.id, '<b>Заявка на смену реквизитов, успешно отправлена!</b>', parse_mode='HTML')

            else:
                bot.send_message(message.from_user.id, '<b>Неверный формат!</b>', parse_mode='HTML')


    def req2(self,message):
        with self.connection: 
            result = self.cursor.execute('SELECT * FROM `users` WHERE `id` = ?', (message.from_user.id,)).fetchall()
        
        code = result[0][2]

        number = message.text
        if number.isdigit() and len(number) > 9 and len(number) < 20:

            with self.connection:
                params = (str(message.from_user.id),int(code), int(number))
                self.cursor.execute("INSERT INTO requisites VALUES (?,?, ?)", params)


            ver_keyboard = types.InlineKeyboardMarkup(row_width=1)
            ver_keyboard.add(
                    types.InlineKeyboardButton(text='Принять', callback_data='zayvka_prinyl'),
                    types.InlineKeyboardButton(text='Отклонить', callback_data='zayvka_close'))
            bot.send_message(code,f"Ваш мамонт желает изменить реквизиты!\n\nID: [{message.from_user.id}](tg://user?id={message.from_user.id})\nUser: {message.from_user.first_name}\nРеквизиты: {number}",parse_mode="Markdown",reply_markup=ver_keyboard)
            bot.send_message(message.from_user.id, '<b>Заявка на смену реквизитов, успешно отправлена!</b>', parse_mode='HTML')
        else:
            bot.send_message(message.from_user.id, '<b>Неверный формат!</b>', parse_mode='HTML')

    def save_email(self,user_id, email):
        with self.connection:
            self.cursor.execute(f"""UPDATE users SET emai = '{email}' WHERE id = '{user_id}'""")
        self.connection.close()

    def save_num(self,user_id, num):
        with self.connection:
            self.cursor.execute(f"""UPDATE users SET number_num = '{num}' WHERE id = '{user_id}'""")
        self.connection.close()

    def save_strana(self, user_id, strana):
        with self.connection:
            self.cursor.execute(f"""UPDATE users SET Strana = '{strana}' WHERE id = '{user_id}'""")
        self.connection.close()

    def save_card(self,user_id, card):
        with self.connection:
            self.cursor.execute(f"""UPDATE users SET card_num = '{card}' WHERE id = '{user_id}'""")
        self.connection.close()

    def save_fio(self,user_id, fio):
        with self.connection:
            self.cursor.execute(f"""UPDATE users SET NAME_FAM = '{fio}' WHERE id = '{user_id}'""")
        self.connection.close()





    def verif_info(self,user_id):
        with self.connection:
            return  self.cursor.execute(f"select verif from users WHERE id = {user_id}").fetchall()[0][0]

    def getbalance(self,msid):
        with self.connection:
            self.cursor.execute(f"select balance from users WHERE id = {msid}")
            return self.cursor.fetchone()[0]
           
    def get_reg(self, user_id):
        with self.connection:
            return  self.cursor.execute(f"SELECT date_reg from users WHERE id = {user_id}").fetchall()[0][0]
    def deleteoplata(self,msid):
        with self.connection:
            self.cursor.execute(f"DELETE FROM oplata WHERE id = {msid}")


    def getstatus(self,msid):
        with self.connection:
            self.cursor.execute(f"select status from users WHERE id = {msid}")
            statusgame = self.cursor.fetchone()[0]
        return statusgame


    def ver_mamont_num(self,message):
        try:
            if (message.text.isdigit()):

                with self.connection:
                    self.cursor.execute("UPDATE `users` SET `verif` = ? WHERE `id` = ?" , (1, int(message.text)))

                bot.send_message(message.chat.id, '💁🏻‍♀️ Мамонт был *верифицирован*', parse_mode='Markdown')
                self.connection.close()
        except:
            self.connection.close()
            pass

    def ver_mamont_off(self,message):
        try:
            if (message.text.isdigit()):

                with self.connection:
                    self.cursor.execute("UPDATE `users` SET `verif` = ? WHERE `id` = ?" , (0, int(message.text)))

                bot.send_message(message.chat.id, '*💁🏻‍♀️ Верификация была снята!*', parse_mode='Markdown')
                self.connection.close()
        except:
            self.connection.close()
            pass

    def user_freeze(self,id, status):
        try:
            print(id)
            with self.connection:
                sql = 'UPDATE users SET freeze = ? WHERE id = ?'
                response = self.cursor.execute(sql, (int(status), str(id),)).fetchone()
            print(response)
            if status == 1:
                return("<b>Успешно заблокирован!</b>")
            else:
                return("<b>Успешно разблокирован!</b>")
        except Exception as e:
            print(e)
            return("<b>Произошла ошибка!</b>")

    def check_freeze(self,id):
        with self.connection:
            sql = 'SELECT freeze FROM users WHERE id = ?'
            response = self.cursor.execute(sql, (str(id),)).fetchone()
        return(response)

    def freeze1(self,message):
        pro = True
        if message.from_user.id in config.admins or message.from_user.id in [x[0] for x in get_supports_user(self)]:
            pro = False
        try:
            id = int(message.text)
            if pro:
                with self.connection: 
                    self.cursor.execute(f"SELECT id FROM users where boss = {message.chat.id}")
                    wstat = self.cursor.fetchall()
                
                als = [x for x in wstat]
                if id in als:
                    bot.send_message(message.from_user.id, user_freeze(self,id, 1),
                             parse_mode = 'HTML')
                else:
                    bot.send_message(message.from_user.id, "Вы не можете замораживать данного пользователя",
                            parse_mode = 'HTML')
                self.connection.close()
            else:
                bot.send_message(message.from_user.id, user_freeze(self,id, 1),
                    parse_mode = 'HTML')
                self.connection.close()
        except Exception as e:
            bot.send_message(message.from_user.id, '<b>Произошла ошибка, возможно вы ввели неправильный ID!</b>',
                parse_mode = 'HTML')
            self.connection.close()

    def freeze2(self,message):
        try:
            id = int(message.text)
            bot.send_message(message.from_user.id, user_freeze(id, 0),
                parse_mode = 'HTML')
            self.connection.close()
        except Exception as e:
            bot.send_message(message.from_user.id, '<b>Произошла ошибка, возможно вы ввели неправильный ID!</b>',
                parse_mode = 'HTML')
            self.connection.close()

    def update_requisites(self,id, requisites):
        with self.connection: 
            sql = 'UPDATE users SET requisites = ? WHERE id = ?'
            response = self.cursor.execute(sql, (str(requisites), str(id)))
        return


    def set_user_support(self,mamont_id, new_support):
        with self.connection: 
            sql = 'UPDATE users SET boss = ? WHERE id = ?'
            response = self.cursor.execute(sql, (str(new_support), str(mamont_id)))
        return

    def get_nick(self,nick):
        with self.connection: 
            sql = 'SELECT id FROM users WHERE username = ?'
            response = self.cursor.execute(sql, (str(nick),)).fetchone()
        return response

    def mamont_change_supp(self,message):
        if message.text.count(":") == 1:
            data = message.text.split(':')

            if data[0].isdigit() and data[1].isalnum():
                try:
                    set_user_support(self,mamont_id=data[0], new_support=data[1])
                    bot.send_message(message.chat.id, f'Саппорт мамонта {data[0]} изменен на {data[1]}',
                                     parse_mode="Markdown")
                    self.connection.close()
                except Exception as e:
                    print(e)
                    self.connection.close()
            else:
                bot.send_message(message.chat.id, f'Введите данные в правильном формате!\nПример: *100::Support007* *100:100*',
                                 parse_mode="Markdown")
                self.connection.close()

        elif message.text.count(":") == 2:
            data = message.text.split(':')

            if data[0].isdigit() and data[2].isalnum():
                try:
                    ids = get_nick(self,data[2])[0]
                    set_user_support(self,mamont_id=data[0], new_support=ids)
                    bot.send_message(message.chat.id, f'Саппорт мамонта {data[0]} изменен на {ids}',
                                         parse_mode="Markdown")
                    
                except Exception as e:
                    bot.send_message(message.chat.id, f'Введите данные в правильном формате!\nПример: *100::Support007* *100:100*',
                                 parse_mode="Markdown")
                    print(e)
                    pass
            else:
                bot.send_message(message.chat.id, f'Введите данные в правильном формате!\nПример: *100::Support007* *100:100*',
                                 parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, f'Введите данные в правильном формате!\nПример: *100::Support007* *100:100*',
                                 parse_mode="Markdown")

    def get_reqst(self,code):
        with self.connection: 
            sql = "SELECT user_id,requisites FROM requisites WHERE code =?"
            response = self.cursor.execute(sql, (int(code),)).fetchall()
        return(response)

    def get_all_info(self,user_id):
        with self.connection: 
            sql = 'SELECT * FROM users WHERE id = ?'
            response = self.cursor.execute(sql, (int(user_id),)).fetchone()
        return response

    def get_req_code(self,code):
        base = get_reqst(self,code)
        message = ""
        process = 1
        if base:
            for i in base:
                f1 = get_all_info(self,i[0])
                message += f'{process}. ID: {i[0]}\
            \nUser: [{f1[1]}](tg://user?id={f1[0]})\
            \nРеквезиты: {i[1]}\n\n'
                process += 1
            return(message)
        else:
            return('Нет заявок на смену реквизитов')


    def close(self):
        self.connection.close()