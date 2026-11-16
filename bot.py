import time
import requests
from bs4 import BeautifulSoup
from telegram import Bot
import os

# يمكنك وضع التوكن هنا مباشرة أو جعله سرياً عبر إعدادات Render
TOKEN = "9020410548:AAGU_x55iMS2Im2qc3nH4DCmDC-BS3oDvTc"
CHAT_ID = "6368301233"
URL = "https://egy.voxcinemas.com/movies/avengers-doomsday-infinity-vision"

def check_vox():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    try:
        response = requests.get(URL, headers=headers, timeout=15)
        if response.status_code == 200:
            text = response.text
            if "Book Tickets" in text or "Showtimes" in text or "احجز الآن" in text:
                return True
    except Exception as e:
        print(f"خطأ في الاتصال: {e}")
    return False

def main():
    bot = Bot(token=TOKEN)
    print("بدأت مراقبة موقع ڤوكس سينما على سحابة Render...")
    
    while True:
        if check_vox():
            msg = f"🚨 **تنبيه عاجل!** تذاكر فيلم **Avengers: Doomsday** متاحة الآن على ڤوكس مصر!\nاحجز فوراً: {URL}"
            # استخدام asyncio لإرسال الرسالة بشكل متوافق
            import asyncio
            async def send_msg():
                await bot.send_message(chat_id=CHAT_ID, text=msg, parse_mode="Markdown")
            asyncio.run(send_msg())
            print("تم إرسال التنبيه بنجاح!")
            break  # يتوقف بعد إرسال التنبيه أو يمكنك إزالتها لو أردت استمرار المراقبة
        
        # يفحص الموقع كل ساعة
        time.sleep(3600)

if __name__ == "__main__":
    main()
