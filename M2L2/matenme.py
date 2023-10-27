import discord
from discord.ext import commands

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')
    channel_id = 1157005777387655178
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send(''' Hola mi nombre es reciclar 
                            mis comandos son ?vidrio, ?carton,
                           ?plastico, ?manzana, ?lata,
                           ?cigarro, ?bateria, ?celular y ?poliestireno''')

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def vidrio(ctx):
    await ctx.send("El vidrio se demora 4000 años en descomponerse")

@bot.command()  
async def carton(ctx):
    await ctx.send("El carton se demora 1 años en descomponerse")

@bot.command()  
async def plastico(ctx):
    await ctx.send("El plastico se demora 150 años en descomponerse y una botella PET 1500 años")

@bot.command()  
async def manzana(ctx):
    await ctx.send("Una manzana se demora 6 meses en descomponerse")

@bot.command()  
async def lata(ctx):
    await ctx.send("Una lata se demora 200 años en descomponerse")

@bot.command()  
async def cigarro(ctx):
    await ctx.send("Un cigarro se demora entre un 1 y 5 años en descomponerse")

@bot.command()  
async def bateria(ctx):
    await ctx.send("Una bateria se demora entre un 500 y 1000 años en descomponerse")

@bot.command()  
async def celular(ctx):
    await ctx.send("la pantalla de un celular se puede demorar entre 4000 años y sus componentes electronicos se demora 300 a 1000 años en descomponerse")

@bot.command()  
async def poliestireno(ctx):
    await ctx.send("nunca se descompone")

bot.run("MTE2NDcyNDA1NDkyNjgyNzU4MQ.GgnG6f.nmHC2puF-O2JFnTLNWsdt0RCY_tSrYZrEvdHNc")















