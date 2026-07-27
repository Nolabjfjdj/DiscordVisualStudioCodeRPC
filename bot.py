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
                        "state": "Développe Bedrock Pattern Searcher sur VSCode | https://discord.gg/mjKYbGWgxc",
                        "emoji": {
                            "name": "💻"
                        }
                    },
                    {
                        "name": "Visual Studio Code",
                        "type": 0,
                        "application_id": "1531146855163891813",
                        "details": "Bedrock Pattern Searcher Minecraft",
                        "state": "Editing file PatternSearchEngine.java",
                        "assets": {
                            "large_image": "mp:icon_vscode",
                            "large_text": "Visual Studio Code"
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
