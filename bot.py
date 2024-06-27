import time
import config
from telethon import TelegramClient, events

bot = TelegramClient(session='bot', api_id=config.API_ID, api_hash=config.API_HASH).start(bot_token=config.BOT_TOKEN)
client = TelegramClient(session='client', api_id=config.API_ID, api_hash=config.API_HASH)

GROUP_IDS = [
    -1001114873336, -1001101869964, -1001384382030, -1001944716489,
    -1001749101070, -1001359748528, -1001458177815, -1001394512469,
    -1001484252579, -1001380457159, -1001614791472, -1001496595543,
    -1001487366957, -1001750892504, -1001200466918, -1001731181261,
    -1001919181053, -1001489222508, -1001143107143, -1001138127394,
    -1001511712693, -1001375743983, -1001467738475, -1001407189643,
    -1001370529818, -1001423580746, -1001372087764, -1001387986186,
    -1001428084502, -1001542449863, -1001384066217, -1001777359440,
    -1001816980890, -1001468782788, -1001235383010, -1001212928907,
    -1001505243780, -1001059051836, -1001293398637, -1001876981390,
    -1001350790526, -1001968617410, -1001359825425, -1001706489494,
    -1001179208674, -1001596215627, -1001856031859, -1001423471919,
    -1001359451175, -1001267349240, -1002025511325, -1001701008155,
    -1001417767206, -1001252761752, -1001756943635, -1001221096553,
    -1002020203750, -1001402515144, -1001380557237, -1001445079778,
    -1001266334274, -1001417286148, -1001714979004, -1002076176061,
    -1001901226169, -1001211599803, -1001694470321, -1001396962795,
    -1001404320177, -1001829987949, -1001583069351, -1001485372590,
    -1001653016719
]


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
    if int(event.peer_id.user_id) in list(map(int, config.ADMINS)):
        await client.connect()
        text_l = str(event.message.message).split('#post')[1:]
        text = "".join(text_l)
        for g_id in GROUP_IDS:
            try:
                await client.send_message(
                    g_id, text
                )
            except BaseException as e:
                print(e)
            time.sleep(30)

        await event.respond("Habar yuborildi!")
    raise events.StopPropagation


bot.run_until_disconnected()
