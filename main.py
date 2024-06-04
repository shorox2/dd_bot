from aiogram import types, Dispatcher, executor, Bot

async def on_startup(_):
    print('WIN!')

TOKEN_API = '6820251663:AAFnuqzGkBvCcyYJIsoZxXp84PvNWMkVhww'

bot = Bot(token=TOKEN_API,
          parse_mode='HTML')
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await message.answer('Я готов к работе!')
    await bot.send_sticker(chat_id=message.chat.id,
                           sticker= 'CAACAgIAAxkBAAEF5ctmXzXcxD46N5jcYV6psXH6mSnVwgACVE0AAikKMUo9ML-4TI74xzUE')
    await message.delete()

@dp.message_handler()
async def dd_refresh_cmd(message: types.Message):
    text = message.text
    if text[12:21] == 'instagram':
        res = text[:8] + 'dd' + text[12:]
        await message.answer(text=res)
        await message.delete()

# @dp.message_handler()
# async def sticker_id_cmd(message: types.Message):
#     await message.answer(message)

if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=on_startup)