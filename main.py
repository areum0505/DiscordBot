import discord
from discord.ext import commands
import lol

bot = commands.Bot(command_prefix='$')  # 접두사가 '$'


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command(aliases=['안녕'])
async def hello(ctx):  # '$hello'라는 메시지를 보냈을 때 @ Hello!를 보내줌
    await ctx.send('{0.author.mention} Hello!'.format(ctx))


@bot.command(name='롤')
async def random_lol(ctx, *, text=''):
    result = lol.getResult(text)
    embed = discord.Embed(title="결과", color=discord.Color.green())
    for key, value in result.items():
        if value != '':
            embed.add_field(name=key, value=value, inline=True)
    if embed.fields:
        await ctx.send(embed=embed)
    else:
        await ctx.send("잘못된 명령어입니다.")


@bot.event
async def on_command_error(ctx, exception):
    if isinstance(exception, commands.CommandNotFound):
        await ctx.send("잘못된 명령어입니다.")


bot.run('ODYxNDMwMjIwNzQ0NDI1NTAz.YOJraQ.L7c5IyCo3qQQfQ389OoQpkt61Ow')
