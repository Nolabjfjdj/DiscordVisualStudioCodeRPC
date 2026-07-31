import discord
import os
from flask import Flask
from threading import Thread

TOKEN = os.environ.get("TOKEN")

app = Flask(__name__)

@app.route('/')
def home():
    return "RPC en ligne !"

Thread(target=lambda: app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080))), daemon=True).start()

class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Connecté en tant que {self.user}")
        await self.ws.send_as_json({
            "op": 3,
            "d": {
                "since": None,
                "activities": [
                    {
                        "type": 4,
                        "name": "Custom Status",
                        "state": "Joue à Minecraft sur DonutSMP | https://discord.gg/mjKYbGWgxc",
                        "emoji": {
                            "name": "🎮"
                        }
                    },
                    {
                        "name": "Minecraft Java 1.21.5",
                        "type": 0,
                        "application_id": "1531146855163891813",
                        "details": "Playing on server",
                        "state": "Playing in donutsmp.net",
                        "assets": {
                            "large_image": "1532589955417636935",
                            "large_text": "Minecraft Java 1.21.5"
                        },
                        "buttons": ["Rejoindre"],
                        "metadata": {
                            "button_urls": [
                                "https://donutsmp.net"
                            ]
                        }
                    }
                ],
                "status": "dnd",
                "afk": False
            }
        })
        print("RPC mis à jour !")

client = MyClient()
client.run(TOKEN)
