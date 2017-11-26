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

    if message.content.startswith("<@264348648542961664>") or message.content.startswith("<@"+client.user.id+">") or "<@264348648542961664>" in message.content:
        url ="https://api.myjson.com/bins/r0tyv"
        status = myjson.get(url)
        status = json.loads(status)
        if status["status"] == "offline":
            em = discord.Embed()
            em.set_thumbnail(url = "https://cdn.dribbble.com/users/187497/screenshots/2008551/message.gif")
            em.set_author(name = "Message(on_absence)", icon_url = "https://cdn.dribbble.com/users/320087/screenshots/1391703/024_cloud.gif")
            em.add_field(name = "Content:", value = "```{}```".format(message.content),inline = False)
            em.add_field(name = "Message_ID:", value = "```{}```".format(message.id),inline = False)
            em.timestamp
            await client.send_message(message.author, content = "**__Feature-on-test__:** "+"**This is an automated Message**: "+"`Out atm, will get back to you asap :D`", embed = em)

    elif message.content.startswith('noble!status'):
        if message.author.id == client.user.id:
            url ="https://api.myjson.com/bins/r0tyv"
            status = myjson.get(url)
            status = json.loads(status)
            await client.send_message(channel, "`Currently: {}` Link: https://api.myjson.com/bins/r0tyv".format(status["status"]))

print("Starting......")

safe_token = "{}".format(tokens)
client.run(safe_token, bot = False, reconnect = True)
