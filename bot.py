import discord-selfbot
import asyncio
import os
from flask import Flask
from threading import Thread

TOKEN = os.environ.get("TOKEN")

app = Flask(__name__)

@app.route('/')
def home():
    return "RPC en ligne !"

Thread(target=lambda: app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080))), daemon=True).start()

class MyClient(vynpard.Client):
    async def on_ready(self):
        print(f"Connecté en tant que {self.user}")
        await self.change_presence(
            activity=vynpard.Activity(
                name="Visual Studio Code",
                type=vynpard.ActivityType.playing,
                details="Bedrock Pattern Searcher Minecraft",
                state="Editing bedrock_patterns.py"
            ),
            status=vynpard.Status.online
        )
        print("RPC mis à jour !")

client = MyClient()
client.run(TOKEN)
