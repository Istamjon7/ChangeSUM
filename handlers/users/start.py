from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart


import requests
import json

from aiogram.types import ContentTypes

from keyboards.default.regKey import btn
from loader import dp




@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=btn)


@dp.message_handler(content_types=['text'])
async def first(message: types.Message):
    text = message.text
    print(text)
    # if text=="💲USD-SUM":
    inputs = 'USD'
    outputs = 'UZS'
    url = 'https://v6.exchangerate-api.com/v6/e256ebea0d0b9ea9da942178/latest/' + inputs
    response = requests.get(url)
    rest = json.loads(response.text)
    result = (rest['conversion_rates'][outputs])
    # await message.answer(result)
    if text.isdigit():
        await message.answer(result*int(text))


    # if text=="SO'M-💲USD":
    #     outputs = 'USD'
    #     inputs = 'UZS'
    # if text=="RUBL-SO'M":
    #     inputs = 'RUB'
    #     outputs = 'UZS'
    # if text=="💲SO'M-RUBL":
    #     outputs = 'RUB'
    #     inputs = 'UZS'
    # if text=="💲USD-RUBL":
    #     inputs = 'USD'
    #     outputs = "RUB"
    # if text=="💲RUBL-USD💲":
    #     outputs = 'USD'
    #     inputs = 'RUB'


