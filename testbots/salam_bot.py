import asyncio
from spluspy import SoroushClient

bot = SoroushClient('salam_bot')


@bot.on_message(incoming=True)
async def handler(event):
    if not event.is_private:
        return

    text = event.raw_text.strip()

    if text == 'سلام':
        await event.reply('خوبی')
    elif text in ('خوبی', 'خوبی؟', 'خوبی!'):
        await event.reply('ممنون، خوبم!')


async def main():
    await bot.start()
    print('ربات فعال شد!')
    await bot.run_until_disconnected()


asyncio.run(main())
