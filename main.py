import requests
from bs4 import BeautifulSoup
import time
import telegram
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

bot = telegram.Bot(token=TOKEN)

URL = "https://www.yad2.co.il/realestate/rent"

seen = set()

GOOD_AREAS = [
    "כרמל",
    "אחוזה",
    "כרמל צרפתי",
    "כרמליה",
    "רמת אשכול"
]

BAD_AREAS = [
    "הדר",
    "חליסה",
    "קרית אליעזר",
    "בת גלים"
]

while True:
    try:
        r = requests.get(URL)
        soup = BeautifulSoup(r.text, "html.parser")

        ads = soup.find_all("a")

        for ad in ads:
            text = ad.get_text(strip=True)

            if len(text) < 30:
                continue

            if any(area in text for area in GOOD_AREAS):

                if not any(bad in text for bad in BAD_AREAS):

                    if text not in seen:

                        seen.add(text)

                        message = f"""
🏠 Новая квартира

{text}

🔗 https://www.yad2.co.il/realestate/rent
"""

                        bot.send_message(
                            chat_id=CHAT_ID,
                            text=message
                        )

        time.sleep(600)

    except Exception as e:
        print(e)
        time.sleep(60)
