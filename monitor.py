import requests
import time

while True:

    r = requests.get("https://www.pokemoncenter.com")

    text = r.text.lower()

    if "queue" in text:

        requests.post(
            "https://api.pushover.net/1/messages.json",
            data={

                "token": "ahbm3vb2pvgjfcf9dcnqtzp4q8wu13",

                "user": "uibasy7ccr5h21zig4trcu53wo87df",

                "title": "🚨 POKEMON CENTER 🚨",

                "message": "QUEUE LIVE GO GO GO",

                "priority": 2,

                "retry": 30,

                "expire": 600,

                "sound": "siren"
            }
        )

    time.sleep(60)
