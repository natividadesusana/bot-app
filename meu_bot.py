import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == '?regras':
            await message.channel.send(f'{message.author.name} as regras do servidor são: \n {os.linesep}1- Respeite os outros integrantes{os.linesep}2- Ao escrever, mande todo o texto de uma só vez{os.linesep}3- Evite falar de assuntos privados{os.linesep}4- Evite postar antes das 7hr e depois das 21hr')            
        elif message.content == '?nivel':
            await message.author.send(f'Olá {message.author.name}, seu Nível é 1 !')

    async def on_member_join(self,member):
        guild = member.guild
        if guild.system_channel is not None:
            mensagem = f'{member.mention} acabou de entrar no {guild.name}'
            await guild.system_channel.send(mensagem)

intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run('OTM1MTY2MDU4ODUwMDUwMTQw.Ye6rQg.n1MDpI7lw4XpF3_Prqw_YttBoot')