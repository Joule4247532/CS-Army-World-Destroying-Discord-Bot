import os, sys
import typing
import argparse
import itertools

class ArgumentParser(argparse.ArgumentParser):
    def _get_action_from_name(self, name):
        """Given a name, get the Action instance registered with this parser.
        If only it were made available in the ArgumentError object. It is
        passed as it's first arg...
        """
        container = self._actions
        if name is None:
            return None
        for action in container:
            if '/'.join(action.option_strings) == name:
                return action
            elif action.metavar == name:
                return action
            elif action.dest == name:
                return action

    def error(self, message):
        exc = sys.exc_info()[1]
        if exc:
            exc.argument = self._get_action_from_name(exc.argument_name)
            raise exc
        super(ArgumentParser, self).error(message)



class AdminPlugin:
    async def plugins(discord_plugin_manager, message, discord_client: object) -> str:
        temp = []
        for i in discord_plugin_manager.plugin_exports:
            temp.append({"plugin": i['plugin'], "status": "active"})

        await discord_client.send_message(message.channel, "PLUGIN    STATUS")
        for i in temp:
            await discord_client.send_message(message.channel, f"{i['plugin']}  {i['status']}")


