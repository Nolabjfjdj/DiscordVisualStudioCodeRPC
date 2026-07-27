import discord
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

class MyClient(discord.Client):
    await self.change_presence(
    activity=discord.Activity(
        name="Visual Studio Code",
        type=discord.ActivityType.playing,
        details="Bedrock Pattern Searcher Minecraft",
        state="💻 discord.gg/mjKYbGWgxc",
        large_image="icon_vscode",
        application_id="1531146855163891813"
    ),
    status=discord.Status.dnd
)
        print("RPC mis à jour !")

client = MyClient()
client.run(TOKEN)
