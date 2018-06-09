
import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircmsgs as ircmsgs
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('RandCMDs')
except ImportError:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x: x


class Shrug(callbacks.Plugin):
    """Shrug"""
    threaded = False
    def shrug(self, irc, msg, args):
        """ shrug """
        irc.reply('┻━┻ ︵ ¯\_(ツ)_/¯ ︵ ┻━┻')
        if self.registryValue("superShrug",msg.args[0]):
            irc.sendMsg(ircmsgs.privmsg(msg.args[0],' $shrug'))
            irc.sendMsg(ircmsgs.privmsg(msg.args[0],' -shrug'))
            irc.sendMsg(ircmsgs.privmsg(msg.args[0],' +shrug'))
Class = Shrug


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
