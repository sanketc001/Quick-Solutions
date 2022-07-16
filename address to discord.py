import subprocess
import requests
import json
import time
import discord
TOKEN = open('token','r').readline()
client = discord.Client()
@client.event
async def on_ready():
    print('We have successfully logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.lower() == 'hello':
        await message.channel.send(f'Hello, {message.author.display_name}!')
        return
    if message.content.lower() == 'mods':
        await message.channel.send("https://drive.google.com/drive/folders/1U9FGuS8YG8GtR-lR6q5ZglZwbjwnMkYW?usp=sharing")
        return
    if message.content.lower() == 'server':
        ngrok = subprocess.Popen(['ngrok', 'tcp', '-region', 'in', '25565'], stdout=subprocess.PIPE)
        time.sleep(2)
        localhost_url = "http://localhost:4040/api/tunnels"
        tunnel_url = requests.get(localhost_url).text
        j = json.loads(tunnel_url)
        tunnel_url = j['tunnels'][0]['public_url'][6:]
        print(tunnel_url)
        channel = client.get_channel(997879178995179610)
        await channel.send(tunnel_url)
        return
    if message.content.lower() == 'bye':
        await message.channel.send(f'See you later, {message.author.display_name}!')
        return
subprocess.Popen(['server.bat'], stdout=subprocess.PIPE)
client.run(TOKEN)
