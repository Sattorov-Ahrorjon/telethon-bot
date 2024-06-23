from telethon import TelegramClient, events
import config

bot = TelegramClient(session='bot', api_id=config.API_ID, api_hash=config.API_HASH).start(bot_token=config.BOT_TOKEN)
client = TelegramClient(session='client', api_id=config.API_ID, api_hash=config.API_HASH)


@bot.on(events.NewMessage(pattern='/start'))
async def handle_start_command(event):
    await event.respond('Salom! Bu Telethon yordamida yaratilgan Telegram botidir.')
    raise events.StopPropagation


@bot.on(events.NewMessage(pattern='/help'))
async def handle_help_command(event):
    await event.respond(
        'Quyidagi komandalar mavjud:\n'
        '/start - Botni boshlash\n'
        '/help - Yordam olishingiz mumkin\n'
        '#post <matn> - Matnni aks ettirish')
    raise events.StopPropagation


@bot.on(events.NewMessage(pattern='#post'))
async def handle_post_command(event):
    group_ids = [-1002224182641]
    await client.connect()
    text_l = str(event.message.message).split('#post')[1:]
    text = "".join(text_l)
    for i in group_ids:
        await client.send_message(
            i, text
        )

    await event.respond("Habar yuborildi!")
    raise events.StopPropagation


bot.run_until_disconnected()
