import discord
import yaml

_config = yaml.safe_load(open("../config.yaml", 'r'))

estado = discord.Client()

@estado.event
async def on_ready():
    print('We have logged in as {0.user}'.format(estado))

@estado.event
async def on_message(message):
    if message.author == estado.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        return

    if (message.author.id != ((_config['guardaSovietico'][0])['id'])) & (message.author.id != ((_config['oficialSovietico'][0])['id'])) & (message.content.endswith('Eu trouxe vodka')):
        user = message.author
        role = discord.utils.get(user.guild.roles, name="Autorização de entrada")
        await user.add_roles(role)
        return

@estado.event
async def on_voice_state_update(member, before, after):
    if(before.channel != None):
        if(after.channel != None):
            if (after.channel.id == (((_config['canais'])['deVoz'])['Moscou'])):
                role = discord.utils.get(member.guild.roles, name="Autorização de entrada")
                await member.remove_roles(role)
                
                role = discord.utils.get(member.guild.roles, name='Moscou')
                await member.add_roles(role)
                await member.edit(mute = False)
                return

            elif (after.channel.id == (((_config['canais'])['deVoz'])['Stalingrado'])):
                role = discord.utils.get(member.guild.roles, name="Autorização de entrada")
                await member.remove_roles(role)
                
                role = discord.utils.get(member.guild.roles, name='Stalingrado')
                await member.add_roles(role)
                await member.edit(mute = False)
                return

            else:
                return

        else:
            if(before.channel.id == (((_config['canais'])['deVoz'])['Moscou'])):
                role = discord.utils.get(member.guild.roles, name='Moscou')
                await member.remove_roles(role)

                role = discord.utils.get(member.guild.roles, name="Autorização de entrada")
                await member.add_roles(role)
                return

            elif(before.channel.id == (((_config['canais'])['deVoz'])['Stalingrado'])):
                role = discord.utils.get(member.guild.roles, name='Stalingrado')
                await member.remove_roles(role)

                role = discord.utils.get(member.guild.roles, name="Autorização de entrada")
                await member.add_roles(role)
                return

    else:
        if(after.channel != None):
            if(after.channel.id == (((_config['canais'])['deVoz'])['Moscou'])):
                role = discord.utils.get(member.guild.roles, name="Autorização de entrada")
                await member.remove_roles(role)

                role = discord.utils.get(member.guild.roles, name='Moscou')
                await member.add_roles(role)
                await member.edit(mute = False)
                return

            elif(after.channel.id == (((_config['canais'])['deVoz'])['Stalingrado'])):
                role = discord.utils.get(member.guild.roles, name="Autorização de entrada")
                await member.remove_roles(role)
                
                role = discord.utils.get(member.guild.roles, name='Stalingrado')
                await member.add_roles(role)
                return

        else:
            return

estado.run(_config['discordBotKey'])
