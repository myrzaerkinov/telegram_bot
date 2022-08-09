from aiogram import types, Bot, Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
import logging
from decouple import config


TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f"Привет мой хозяин {message.from_user.full_name}")


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_1")
    markup.add(button_call_1)

    question = "Сколько будет 1 + 1?"
    answers = ['1', '2', '3', '4', '55']
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Это же легко",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )

@dp.callback_query_handler(lambda call: call.data == "button_call_2")
async def quiz_2(call: types.CallbackQuery):
    question = "Кто создатель языка программирования Python?"
    answers = [
        '4',
        '8',
        '5',
        'Guido Van Ronssum',
        'Ilon Mask'
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Это же легко",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,

        )



@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, message.text) #kuda i chto otpravlyat'


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)


