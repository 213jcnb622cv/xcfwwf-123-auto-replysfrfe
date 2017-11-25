#auto-reply
import discord
import json
import myjson
import os
tokens = os.environ.get("Token")
client = discord.Client()

@client.event
async def on_ready():
    print("ONLINE REPLIER")
    print(client.user.name)

@client.event
async def on_message(message):
    channel = message.channel
    if message.content.startswith("noble!set"):
        if message.author.id == client.user.id:
            url ="https://api.myjson.com/bins/r0tyv"
            status = myjson.get(url)
            status = json.loads(status)
            stats = message.content[len("noble!set"):].strip()
            stats = stats.lower()
            if stats == "online" or stats == "offline":
                status["status"]= "{}".format(stats)
                url = myjson.store(json.dumps(status),update= url)
                await client.send_message(channel, "`SET!`")
            else:
                await client.send_message(channel,"`Error!`")

    if message.content.startswith("<@264348648542961664>") or message.content.startswith("<@"+client.user.id+">"):
        url ="https://api.myjson.com/bins/r0tyv"
        status = myjson.get(url)
        status = json.loads(status)
        if status["status"] == "offline":
            await client.send_message(message.author, "**This is an automated Message**\n**Feature on test:** `Sorry, out at the moment, will get back to asap :D`")


print("Starting......")

safe_token = "{}".format(tokens)
client.run(safe_token, bot = False, reconnect = True)
