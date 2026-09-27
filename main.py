import discord
from discord import app_commands

# Configura as intenções obrigatórias
intents = discord.Intents.default()
intents.message_content = True  # Permite ler conteúdo das mensagens

class MeuBot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        # Cria a árvore de comandos de barra (Slash Commands)
        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):

        await self.tree.sync()
        print(f'Bot conectado com sucesso como {self.user}!')


client = MeuBot()


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.lower() == 'plastico':
        await message.channel.send(f'O plástico leva em média 400 a 450 anos para se decompor na natureza.')


@client.tree.command(name="latas", description="Amarelo é metal, vermelha é plástico, azul é papel e verde é vidro.")
async def latas(interaction: discord.Interaction):
    await interaction.response.send_message("Amarelo é metal, vermelha é plástico, azul é papel e verde é vidro.")
#token abaixo
client.run('TOKEN')
