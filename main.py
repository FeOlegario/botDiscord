import os
import discord
import tempfile
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
async def ajuda_comandos(ctx):
    embed1 = discord.Embed(
        title="Como usar o bot",
        description=":rotating_light: Para obter os BOPs deve-se atentar nesses dois modos:",
        color= 57599
    )
    embed1.add_field(
        name=":small_blue_diamond: Modo 1 sem arquivo",
        value=":writing_hand: Digite `!f ` seguido da mensagem que deseja formatar.",
        inline=False
    )

    embed1.set_image(url=r"https://media.discordapp.net/attachments/937132531386572913/1345918836183928884/sem_arquivo.png?ex=67c64c18&is=67c4fa98&hm=d37747b920d8b8c51b409a06c9368eb0d2a937fef09d44c6abdbf8aae4a77a4b&=&format=webp&quality=lossless")


    embed2 = discord.Embed(
        title="",
        description="",
        color= 57599
    )


    embed2.add_field(
        name=":small_orange_diamond: Modo 2 com arquivo",
        value=":writing_hand: Digite `!f a` e anexe o arquivo contendo as mensagens que deseja formatar.",
        inline=False
    )
    embed2.set_image(url=r"https://media.discordapp.net/attachments/937132531386572913/1345918835781271695/com_arquivo.png?ex=67c64c18&is=67c4fa98&hm=ece66367c2f33f9396f39cf3966b73291c463fc6b4a5f4df9d2d9c10e59a3483&=&format=webp&quality=lossless")

    await ctx.message.delete()
    await ctx.send(embed=embed1, delete_after=60)
    await ctx.send(embed=embed2, delete_after=60)



@bot.command(name='f')
async def formatar(ctx, *, mensagens: str):
    if mensagens == "a" and ctx.message.attachments:
        anexo = ctx.message.attachments[0]
        conteudo = await anexo.read()
        mensagens = conteudo.decode("utf-8")
    

    resultado = formatar_texto(mensagens)  

    # Criar um arquivo temporário
    with tempfile.NamedTemporaryFile(delete=False, mode="w", encoding="utf-8", suffix=".txt") as temp_file:
        temp_file.write(resultado)
        temp_filename = temp_file.name  # Salva o caminho do arquivo gerado

    # Preparar o envio do arquivo
    file = discord.File(temp_filename, filename="saida.txt")

    await ctx.message.delete()
    await ctx.send(f"""Aqui está o resultado formatado, {ctx.author.mention}.
{len(mensagens.splitlines())} BOPs. :white_check_mark:
""", file=file)

bot.run(TOKEN)