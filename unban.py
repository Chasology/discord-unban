import discord

TOKEN = ''
GUILD_ID = ''
TXT_FILE = 'unban.txt'

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Ready and steady!')

    guild = client.get_guild(int(GUILD_ID))

    with open(TXT_FILE, 'r') as file:
        user_ids = file.read().splitlines()

    for user_id in user_ids:
        try:
            await guild.unban(discord.Object(int(user_id)))
            print(f'User ID {user_id} unbanned.')
        except discord.errors.NotFound:
            print(f'User ID {user_id} not found.')

    await client.close()

client.run(TOKEN)