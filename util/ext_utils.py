# Comment for credit
from termcolor import cprint


def cog_load(client, cog):
	try:
		client.add_cog(cog(client))
	except Exception as e: # todo: log this
		cprint(f"Error occurred setting up {cog.__name__} Cog:\n{e}", "red")
	else:
		cprint(f"Loaded {cog.__name__} Cog.", "green")


def cog_unload(client, cog):
	try:
		client.remove_cog(cog.__name__)
	except Exception as e: # todo: log this
		cprint(f"Error occurred removing {cog.__name__} Cog:\n{e}", "red")
	else:
		cprint(f"Unloaded {cog.__name__} Cog.", "red")
