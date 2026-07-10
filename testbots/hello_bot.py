from spluspy import Client


bot = Client("hello_bot")


@bot.on_message()
async def handler(m):
    print(f"Got message from {m.sender_id} in {m.chat_id}: {m.text}")
    await m.reply("سلام")





bot.run()
