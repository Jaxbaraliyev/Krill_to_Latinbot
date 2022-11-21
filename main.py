import logging
from aiogram import Bot,Dispatcher,executor,types
from translitirate import to_latin, to_cyrillic
logging.basicConfig(level=logging.INFO)

bot = Bot(token="5837691066:AAGyMx-qbUeUlIKo3h6CThqux_Ww8-Z-qFQ")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    ism = message.from_user.full_name
    await message.answer(f"Assalomu alaykum {ism}😊.Botimizga xush kelibsiz!\n"
                         f"O`zgartirmoqchi bo`lgan so`zingizni kiriting!")

@dp.message_handler(commands=['admin'])
async def admin(message:types.Message):
    a = "@Ramziddin_17_17"
    await message.answer(f"Admin: {a}")

@dp.message_handler(commands=['help'])
async def admin(message:types.Message):
    await message.answer("Bu botimiz faqatgina krill harfidagi so`zlarni lotinga va aksincha lotin harfidagi so`zlarni "
                         "krill o`girib beradi! Sizga xizmat ko`rsatganimizdan mamnunmiz!😊")

@dp.message_handler(lambda message: True)
async def bot(message:types.Message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    await message.answer(javob(msg))


if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)



