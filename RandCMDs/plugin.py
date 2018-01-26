
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


class RandCMDs(callbacks.Plugin):
    """RandCMDs"""
    threaded = False
    def pong(self, irc, msg, args):
        """pong"""
        irc.reply("ping")
    def cookie(self, irc, msg, args, something):
        """cookie"""
        nick = msg.nick
        if something and len(something)>0:
            nick = ' '.join(something[0:])
        irc.reply("gives " + nick + " a cookie", action=True)
    cookie = wrap(cookie, [optional(many('something'))])
Class = RandCMDs


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
