import re, inspect
from discord.ext import commands

regexes = [
	re.compile(r"(?:<@!)?(\d{17,20})>?"),
	re.compile(r"@?(.+)#?(\d{4})?")
]

devs = [252104964753719296, 573986854366347274, 427802690236579850]


async def get_users(client, users):
	"""Takes a list of IDs or mentions and returns list of user objects"""
	crunched = []
	for x in users:
		if match := re.match(regexes[0], x):
			if len(match.groups()) != 1:
				crunched.append(x)
			if (user := client.get_user(int(match.group(1)))) is not None:
				crunched.append(user)
			else:
				crunched.append(x)
		else:
			print(f"Could not get user from ID {match.group(1)}")
	return crunched


def admin_dash_o(ctx, args, perms):
	if len(args) == 0:  # todo: make the part up to line 26 a function since it's the exact same in all commands
		raise commands.MissingRequiredArgument(inspect.Parameter("args", inspect.Parameter.VAR_POSITIONAL))

	if args[0] == "-o" and ctx.message.author.id in devs:
		if len(args) == 1:
			raise commands.MissingRequiredArgument(inspect.Parameter("args", inspect.Parameter.VAR_POSITIONAL))
		return 2

	return 1 if (p := ctx.message.author.permissions_in(ctx.message.channel)).manage_messages and perms == 0 or perms \
		== 1 and p.kick_members or perms == 2 and p.ban_members else 0 # DO NOT QUESTION THIS CODE
