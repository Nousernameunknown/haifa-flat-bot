import requests
from bs4 import BeautifulSoup
import time
from telegram import Bot
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

bot = Bot(token=TOKEN)

SEARCH_URL = "https://www.yad2.co.il/realestate/rent?city=4000"

seen_ads = set()

GOOD_AREAS = [
    "כרמל",
    "אחוזה",
    "כרמל צרפתי",
    "כרמליה",
    "רמת אשכול",
    "רמת בגין"
]

BAD_AREAS = [
    "הדר",
    "חליסה",
    "קרית אליעזר",
    "בת גלים",
    "נווה פז"
]

GOOD_WORDS = [
    "בעלי חיים",
    "חתול",
    "חיות",
    "מרפסת",
    "נוף",
    "ממד"
]

BAD_WORDS = [
    "ללא בעלי חיים",
    "שותפים",
    "לטווח קצר"
]

MAX_PRICE = 4800

headers = {
    "User-Agent": "Mozilla/5.0"
}

while True:

    try:

        response = requests.get(
            SEARCH_URL,
            headers=headers,
            timeout=20
        )

        soup = BeautifulSoup(response.text, "html.parser")

        text_blocks = soup.find_all(text=True)

        for text in text_blocks:

            clean = text.strip()

            if len(clean) < 80:
                continue

            if any(area in clean for area in GOOD_AREAS):

                if any(bad in clean for bad in BAD_AREAS):
                    continue

                if any(bad in clean for bad in BAD_WORDS):
                    continue

                if clean in seen_ads:
                    continue

                seen_ads.add(clean)

                message = f"""
🏠 Найдена квартира

{clean[:1000]}

🔗 https://www.yad2.co.il/realestate/rent
"""

                bot.send_message(
                    chat_id=CHAT_ID,
                    text=message
                )

                print("Sent:", clean[:100])

        time.sleep(600)

    except Exception as e:

        print("ERROR:", e)

        time.sleep(60)
        print("BOT IS RUNNING")

while True:
    pass
