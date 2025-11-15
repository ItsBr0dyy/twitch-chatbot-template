# Import modules
from twitchAPI.chat import Chat, EventData, ChatMessage, ChatSub, ChatCommand
from twitchAPI.type import AuthScope, ChatEvent
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.twitch import Twitch
import asyncio
import random

# Set up contestants
APP_ID = "CLIENT_ID"
APP_SECRET = "CLIENT_SECRET"
USER_SCOPE = [AuthScope.CHAT_READ, AuthScope.CHAT_EDIT, AuthScope.CHANNEL_MANAGE_BROADCAST]
TARGET_CHANNEL = 'TARGET_CHANNEL'

async def on_message(msg: ChatMessage):
    # Print username and chat message
    print(f'{msg.user.display_name} - {msg.text}')

# Bot connected successfully
async def on_ready(ready_event: EventData):
    # Connect to TARGET_CHANNEL
    await ready_event.chat.join_room(TARGET_CHANNEL)

    # Print ready message
    print('Bot Ready')

# Lurk command
async def lurk_command(cmd: ChatCommand):
    chance = random.randint(0, 4)

    if chance == 0:
        await cmd.reply('/me Thanks for stopping by, enjoy the stream :)')
    elif chance == 1:
        await cmd.reply("/me We appreciate you for being here, even in silent mode :)")
    elif chance == 2:
        await cmd.reply("/me Enjoy your lurk, and thanks for hanging out WW")
    elif chance == 3:
        await cmd.reply("/me Thank you for lurking, make sure to mute the tab, not the stream")
    elif chance == 4:
        await cmd.reply("/me Take your time, we'll be here when you're back o7")

# unlurk command
async def unlurk_command(cmd: ChatCommand):
    chance = random.randint(0, 4)

    if chance == 0:
        await cmd.reply('/me Welcome back brodie :)')
    elif chance == 1:
        await cmd.reply("/me Thank you for tabbing the stream :)")
    elif chance == 2:
        await cmd.reply("/me WWW")
    elif chance == 3:
        await cmd.reply("/me has returned from the depths of lurk")
    elif chance == 4:
        await cmd.reply("/me welcome back how was your lurk?")

# quote command
async def quote_command(cmd: ChatCommand):
    chance = random.randint(0, 6)

    if chance == 0:
        await cmd.reply("/me Be yourself; everyone else is already taken. — Oscar Wilde")
    elif chance == 1:
        await cmd.reply("/me Believe you can and you are halfway there. — Theodore Roosevelt")
    elif chance == 2:
        await cmd.reply("/me The only limit to our realization of tomorrow will be our doubts of today. — Franklin D. Roosevelt")
    elif chance == 3:
        await cmd.reply("/me Live as if you were to die tomorrow. — Mahatma Gandhi")
    elif chance == 4:
        await cmd.reply("/me In three words I can sum up everything I've learned about life: it goes on. — Robert Frost")
    elif chance == 5:
        await cmd.reply("/me If you cannot do great things, do small things in a great way. — Martin Luther King Jr.")
    elif chance == 6:
        await cmd.reply("/me It does not matter how slowly you go, as long as you do not stop. — Confucius")

# discordjoin command
async def discordbot_command(cmd: ChatCommand):
        await cmd.reply('/me Add the bot to your server: https://discord.com/oauth2/authorize?client_id=1418412121703710720&permissions=8&integration_type=0&scope=bot')

# Vanity command
async def vanity_command(cmd: ChatCommand):
        await cmd.reply('/me https://vanity.zonian.dev')

# 67 command
async def sixseven_command(cmd: ChatCommand):
        await cmd.reply('/me 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67')

# botdiscord command
async def botdiscord_command(cmd: ChatCommand):
        await cmd.reply('/me Join The Discord: https://discord.gg/Xbm5Kr5vSJ')

# dihsize command
async def dihsize_command(cmd: ChatCommand):
    chance = random.randint(0, 6)

    if chance == 0:
        await cmd.reply("/me dih size is 67")
    elif chance == 1:
        await cmd.reply("/me dih size is too small")
    elif chance == 2:
        await cmd.reply("/me dih size is 2 inches (it is average tho)")
    elif chance == 3:
        await cmd.reply("/me dih size is 99999999")
    elif chance == 4:
        await cmd.reply("/me dih size is- WTFFFF")
    elif chance == 5:
        await cmd.reply("/me dih size is too massive")
    elif chance == 6:
        await cmd.reply("/me dih size is 10 centimeters")

# hi command
async def hi_command(cmd: ChatCommand):
        await cmd.reply('/me hi how are you!!')

# coinflip command
async def coinflip_command(cmd: ChatCommand):
    chance = random.randint(0, 3)

    if chance == 0:
        await cmd.reply('/me Heads')
    elif chance == 1:
        await cmd.reply("/me Tails")
    elif chance == 2:
        await cmd.reply("/me Tails")
    elif chance == 3:
        await cmd.reply("/me Heads")

# fact command
async def fact_command(cmd: ChatCommand):
    chance = random.randint(0, 6)

    if chance == 0:
        await cmd.reply('/me Did you know that Fossabot is a clanker?')
    elif chance == 1:
        await cmd.reply("/me Did you know that the sun is about 400 times larger than the moon.")
    elif chance == 2:
        await cmd.reply("/me Did you know that honey never spoils.")
    elif chance == 3:
        await cmd.reply("/me Did you know that octopuses have three hearts.")
    elif chance == 4:
        await cmd.reply("/me Did you know that koalas have fingerprints that are almost identical to humans.")
    elif chance == 5:
        await cmd.reply("/me Did you know that the femur is the longest bone in the human body.")
    elif chance == 6:
        await cmd.reply("/me Did you know that our brain is constantly eating itself.")

# online command
async def online_command(cmd: ChatCommand):
        await cmd.reply('/me Bot is online and functioning!')

# updating command
async def updating_command(cmd: ChatCommand):
        await cmd.reply('/me Bot is getting updated and will be back up in a few minutes!')

# donation command
async def donation_command(cmd: ChatCommand):
        await cmd.reply('/me Support the bot by paying a one-time fee: https://streamelements.com/itsbr0dyybot/tip')

# sleep command
async def sleep_command(cmd: ChatCommand):
        await cmd.reply('/me sub up to wake him up')

# logs command
async def logs_command(cmd: ChatCommand):
        await cmd.reply('/me You can check logs from any chat from any user with: https://tv.supa.sh/logs')

# doufwme command
async def doufwme_command(cmd: ChatCommand):
        await cmd.reply('/me i fw you heavy lil twan') 

# mobile command
async def mobile_command(cmd: ChatCommand):     
        await cmd.reply('/me Unlock 7tv on Mobile with Frosty, Chatsen or DankChat here! (DankChat is only available on android not IOS): https://www.frostyapp.io/?referrer=7tv.app | https://chatsen.app/?referrer=7tv.app | https://dank.chat/?referrer=7tv.app')

# enhancer command
async def enhancer_command(cmd: ChatCommand):
        await cmd.reply('/me Download the Twitch Enhancer extension for a better Twitch experience! https://www.twitchenhancer.com/')

# chatterino command
async def chatterino_command(cmd: ChatCommand):
        await cmd.reply('/me https://chatterino.com')

# 7tv command
async def seventv_command(cmd: ChatCommand):
        await cmd.reply('/me Do you want to see exclusive emotes that most people cannot see? Download 7TV here!: https://7tv.app/')

# prime command
async def prime_command(cmd: ChatCommand):
        await cmd.reply('/me Have an Amazon Prime account? Get Twitch Prime for a monthly free subscription! https://twitch.amazon.com/prime') 

# twitchcon command
async def twitchcon_command(cmd: ChatCommand):
        await cmd.reply('/me TwitchCon tickets are now on sale and will unlock a global badge. Additionally, if you use a referral link, you will also unlock the Chrome Star badge.') 

# multitwitch command
async def multitwitch_command(cmd: ChatCommand):
        await cmd.reply('/me Multitwitch is a website that allows you to watch multiple streams at once. https://multitwitch.tv/')

# ask command
async def ask_command(cmd: ChatCommand):
        await cmd.reply('/me you dumbass really think i am smart enough to answer that question?')

async def on_sub(sub: ChatSub):
    print(f'New subscription in {sub.room.name}:\n'
          f'  Type: {sub.sub_plan}\n'
          f'  Message: {sub.sub_message}')

async def main():
    twitch = await Twitch(APP_ID, APP_SECRET)
    auth = UserAuthenticator(twitch, USER_SCOPE)
    token, refresh_token = await auth.authenticate()
    await twitch.set_user_authentication(token, USER_SCOPE, refresh_token)

    chat = await Chat(twitch)

# Bot setup function
async def run_bot():
    # Authenticate application
    bot = await Twitch(APP_ID, APP_SECRET)
    auth = UserAuthenticator(bot, USER_SCOPE)
    token, refresh_token = await auth.authenticate()
    await bot.set_user_authentication(token, USER_SCOPE, refresh_token)

    # Initialize chat class
    chat = await Chat(bot)

    # Register events
    chat.register_event(ChatEvent.READY, on_ready)
    chat.register_event(ChatEvent.MESSAGE, on_message)
    chat.register_event(ChatEvent.SUB, on_sub)

    # Register commands
    chat.register_command('lurk', lurk_command)
    chat.register_command('unlurk', unlurk_command)
    chat.register_command('vanity', vanity_command)
    chat.register_command('logs', logs_command)
    chat.register_command('hi', hi_command)
    chat.register_command('coinflip', coinflip_command)
    chat.register_command('online', online_command)
    chat.register_command('updating', updating_command)
    chat.register_command('donation', donation_command)
    chat.register_command('dihsize', dihsize_command)
    chat.register_command('sleep', sleep_command)
    chat.register_command('doufwme', doufwme_command)
    chat.register_command('prime', prime_command)
    chat.register_command('chatterino', chatterino_command)
    chat.register_command('7tv', seventv_command)
    chat.register_command('fact', fact_command)
    chat.register_command('twitchcon', twitchcon_command)
    chat.register_command('enhancer', enhancer_command)
    chat.register_command('mobile', mobile_command)
    chat.register_command('quote', quote_command)
    chat.register_command('discordbot', discordbot_command)
    chat.register_command('67', sixseven_command)
    chat.register_command('multitwitch', multitwitch_command)
    chat.register_command('ask', ask_command)

    # Start the chat bot
    chat.start()

    try:
        input('press ENTER to stop\\n')
    finally:
        chat.stop()
        await bot.close()


asyncio.run(run_bot())
