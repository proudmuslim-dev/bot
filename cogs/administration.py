from discord.ext import commands
import discord
from contextlib import redirect_stdout
from termcolor import cprint
import io, textwrap, traceback, os

owners = [573986854366347274, 252104964753719296,]


async def is_owner(ctx):
	return ctx.author.id in owners


class Administration(commands.Cog):
	"""Administration Commands"""

	def __init__(self, client):
		self.client = client

	@commands.command(hidden=True)
	async def logout(self, ctx):
		"""Shuts down bot"""
		if ctx.author.id in owners:
			await self.client.logout()

		else: 
			await ctx.send(":x: You are not one of my owners and therefore are incapable of ameliorating yourself to the stations required to operate this command.")


	@commands.command(hidden=True)
	@commands.check(is_owner)
	async def reload(self, ctx, *ext):
		"""Reloads extensions"""

		if ext:
			for x in ext:
				try:
					self.client.reload_extension(x)

				except Exception as e:  # todo: log this
					if ctx is not None:
						await ctx.send(
							"Couldn't find extension {x}!" if isinstance(e, commands.errors.ExtensionNotFound)
							else f"Error occurred reloading extension {x}:\n{e}")
					cprint(f"Error occurred reloading extension {x}:\n{e}", "red")

				else:
					if ctx is not None:
						await ctx.send(f"Successfully reloaded extension {x}!")
					cprint(f"Successfully reloaded extension {x}!", "green")

		else:
			for x in os.listdir(os.fsencode("cogs"))[1:]:
				try:
					self.client.reload_extension(x.decode()[:-3])

				except Exception as e:  # todo: log this
					cprint(f"Error occurred reloading extension {x.decode()[:-3]}:\n{e}", "red")
					if ctx is not None:
						await ctx.send(f"Error occurred reloading extension {x.decode()[:-3]}:\n{e}")

				else:
					if ctx is not None:
						await ctx.send(f"Successfully reloaded extension {x.decode()[:-3]}!")
					cprint(f"Successfully reloaded extension {x.decode()[:-3]}!", "green")

	# Copyright (c) 2015 Rapptz - Modified Slightly
	@commands.command(hidden=True, name="eval")
	@commands.check(is_owner)
	async def _eval(self, ctx, *, body):
		"""Evaluates code"""

		env = {
			"self": self,
			"client": self.client,
			"ctx": ctx
		}

		env.update(globals())

		if body.startswith("```") and body.endswith("```"):
			body = "\n".join(body.split("\n")[1:-1])

		else:
			body = body.strip("` \n")
		stdout = io.StringIO()

		to_compile = f"""import discord, os, math, sys, asyncio, termcolor, json, re
async def func():\n{textwrap.indent(body, "  ")}"""

		try:
			exec(to_compile, env)

		except Exception as e:
			return await ctx.send(f"```py\n{e.__class__.__name__}: {e}\n```")

		func = env["func"]

		try:
			with redirect_stdout(stdout):
				ret = await func()

		except Exception:
			value = stdout.getvalue()
			embed = discord.Embed(color=discord.Colour.from_rgb(255, 130, 53))
			embed.add_field(name="Exception", value=f"```py\n{value}{traceback.format_exc()}\n```")
			await ctx.send(embed=embed)

		else:
			value = stdout.getvalue()

			try:
				await ctx.message.add_reaction("\u2705")

			except:
				pass

			if ret is None:
				if value:
					embed = discord.Embed(color=discord.Colour.from_rgb(255, 130, 53))
					embed.add_field(name="Output", value=f"```py\n{value}\n```")

					await ctx.send(embed=embed)

			else:
				self._last_result = ret
				embed = discord.Embed(color=discord.Colour.from_rgb(255, 130, 53))
				embed.add_field(name="Output", value=f"```py\n{value}{ret}\n```")

				await ctx.send(embed=embed)
					
	# End Copyright Notice


def setup(client):
	client.add_cog(Administration(client))


def teardown(client):
	client.remove_cog(Administration.__name__)
