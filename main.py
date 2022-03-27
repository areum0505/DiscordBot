import discord
from discord.ext import commands
from lol import lol

bot = commands.Bot(command_prefix='$')  # 접두사가 '$'
_lol = lol()


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command(aliases=['안녕'])
async def hello(ctx):  # '$hello'라는 메시지를 보냈을 때 @ Hello!를 보내줌
    await ctx.send('{0.author.mention} Hello!'.format(ctx))


@bot.command(name='롤')
async def random_lol(ctx, *, text=''):
    result = _lol.getResult(text)
    embed = discord.Embed(title="결과", color=discord.Color.green())
    for key, value in result.items():
        if value != '' and key != '이미지':
            embed.add_field(name=key, value=value, inline=True)
    if embed.fields:
        embed.set_thumbnail(url=result['이미지'])
        await ctx.send(embed=embed)
    else:
        await ctx.send("잘못된 명령어입니다.")


@bot.event
async def on_command_error(ctx, exception):
    if isinstance(exception, commands.CommandNotFound):
        await ctx.send("잘못된 명령어입니다.")


bot.run('token')
