import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == 'regras':
            await message.channel.send(f'{message.author.name} as regras do servidor são:{os.linesep}1- Respeite os outros integrantes{os.linesep}2-Ao escrever, mande todo o texto de uma só vez{os.linesep}3- Evite falar de assuntos privados{os.linesep}4- Evite postar antes das 7h ou depois das 21h')

client = MyClient()
client.run('OTM1MTY2MDU4ODUwMDUwMTQw.Ye6rQg.gDZq6yxnnrttgrueuQP3WenMFb0')