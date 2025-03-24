import os
import discord


user_id1_int = int(os.environ["HI_USER1_ID"])
user_id2_int = int(os.environ["HI_USER2_ID"])
asker_id_int_helper_id_int_list_dict = {user_id1_int: [user_id2_int]}
helper_id_int_asker_id_int_list_dict = {user_id2_int: [user_id1_int]}


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #
    if message.channel.type == discord.ChannelType.private:
        from_user_id_int = message.author.id
        if from_user_id_int in asker_id_int_helper_id_int_list_dict:
            to_user_id_int_list = asker_id_int_helper_id_int_list_dict[from_user_id_int]
        else:
            to_user_id_int_list = helper_id_int_asker_id_int_list_dict[from_user_id_int]
        #
        for to_user_id_int in to_user_id_int_list:
            to_user = await client.fetch_user(to_user_id_int)
            await to_user.send(message.content)


token_str = os.environ["HI_TOKEN"]
client.run(token_str)
