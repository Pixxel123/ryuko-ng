import enum
import logging

import discord
from discord.ext import commands
from discord.ext.commands import Cog

logging.basicConfig(
    format="%(asctime)s (%(levelname)s) %(message)s (Line %(lineno)d)",
    level=logging.INFO,
)


class Roles(Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roles(self, ctx):
        game_roles = [
            {"id": role.id, "name": role.name}
            for role in ctx.guild.roles
            if "Looking for LDN game" in role.name
        ]
        numbered_roles = [(number, name) for number, name in enumerate(game_roles, 1)]
        numbered_roles = {k: v for (k, v) in game_roles.items()}
        # await ctx.send(f"{ctx.author.mention} Here are the current roles in the server: {'\n'.join([1,2])}")
        print(numbered_roles)


def setup(bot):
    bot.add_cog(Roles(bot))
