from telethon.sync import TelegramClient
import time
api_id = input("API ID:")
api_hash = input("API HASH:")
phone_number = input("your telegram number:")
session_name = 'my_session'
client = TelegramClient(session_name, api_id, api_hash)
async def send_message():
    await client.start(phone_number)    
    while True:
        #ادخل اليوزر المجموعه الي تريد يندز الها الرسائل 
        GROUP_USER='@c_w_e '
        MESSG="""
حط رسالتك اهنا
        """
        await client.send_message(GROUP_USER,MESSG)
        #اهنا تكدر تتحكم بالوقت الارسال مثلا كل 5 ثواني 
        time.sleep(5)
client.loop.run_until_complete(send_message())