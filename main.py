import os
import discord
from discord.ext import commands
from dotenv import load_dotenv


def formatar_texto(bops):
    bops_formatados = bops.strip().splitlines()
    bops_saida = "','".join(bops_formatados)
    return f"('{bops_saida}')"

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user} pronto pra uso!')


@bot.command(name='ping')
async def ping(ctx):
    await ctx.send(f"Pong! 🏓 Latência: {round(bot.latency * 1000)}ms")


@bot.command(name='ajuda')
async def bop(ctx):
    await ctx.author.send(f"""
Olá, {ctx.author}! Eu sou um bot que formata mensagens para serem usadas em queries SQL. Para formatar uma mensagem, digite `!f` seguido da mensagem que deseja formatar. Não precisa se preocupar com as quebras de linha, eu cuido disso pra você!
""")

@bot.command(name='f')
async def formatar(ctx, *, mensagens: str):
    resultado = formatar_texto(mensagens)
    await ctx.message.delete()
    await ctx.send(f"Aqui está o resultado formatado {ctx.author.mention}:\n```{resultado}```")

bot.run(TOKEN)