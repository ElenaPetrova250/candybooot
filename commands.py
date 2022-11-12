 
from aiogram import types

import view
import model
from bot import bot


async def start(message: types.Message):
    await view.greetings(message)

async def set_count(message: types.Message):
    await bot.send_message(message.from_user.id,
                        f'{message.from_user.first_name}, '
                        f'Ты первый, возьми себе конфет, от 1 до 28. Сколько хочешь взять?')

def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

def bot_calc(value):
    k = (1,29)
    while value-k <= 28 and value > 29:
        k = (1,29)
    return k

value = set_count
flag = (0,2)
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = randint(1,29)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)


def getNumber(message: types.Message):
    while value-k <= 28 and value > 29:
        k = randint(1,29)
    return 

async def finish(message: types.Message):
    await bot.send_message(message.from_user.id,
                        f'{message.from_user.first_name}, '
                        f'до свидания!')

async def getNumber(message: types.Message):
    number = message.text
    if 0 < int(number) < 29:
        print(number)
    else:
        await bot.send_message(message.from_user.id, 'Ах, ты грязный читер!')