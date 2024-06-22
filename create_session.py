import asyncio
import config
from telethon import TelegramClient, errors

client = TelegramClient(session='client', api_id=config.API_ID, api_hash=config.API_HASH)


async def sign_in_in_terminal():
    await client.connect()
    phone = False
    code = False
    password = False
    if not await client.is_user_authorized():
        while True:
            try:
                while not phone:
                    phone = input("Telefon raqamingizni kiriting: ")

                phone_code_hash = (await client.send_code_request(phone=phone)).phone_code_hash
                print(f"Kod Telegram hisobingizga yuborildi: {phone}")

                while not code:
                    code = input("Tasdiqlash kodini kiriting: ")

                await client.sign_in(phone=phone, code=code, phone_code_hash=phone_code_hash)
                break
            except errors.PhoneCodeExpiredError:
                print("Tasdiqlash kodi muddati o'tib ketdi. Yangi kod yuboriladi.")
            except errors.SessionPasswordNeededError:
                while not password:
                    password = input("2 bosqichli autentifikatsiya parolini kiriting: ")
                await client.sign_in(password=password)
                break
    print("Sessiya muvaffaqiyatli ro'yxatdan o'tkazildi va saqlandi!")


asyncio.run(sign_in_in_terminal())
