
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
    def potato(self, irc, msg, args):
        """ potato """
        irc.reply("is a potato", action=True)
    def moo(self, irc, msg, args):
        """ moo """
        irc.reply("moOoOoOoOoOoOoOoOoOoOoOoO")
    def shrug(self, irc, msg, args):
        """ shrug """
        irc.reply('┻━┻ ︵ ¯\_(ツ)_/¯ ︵ ┻━┻')
    def test(self, irc, msg, args, something):
        """ test """
        self.moo = "moo"
        irc.reply(self.moo)
    test = wrap(test, ['owner', many('something')])
    def test2(self,irc, msg, args, something):
        """ test2 """
        irc.reply(self.moo)
    test2 = wrap(test2, ['owner', many('something')])
Class = RandCMDs


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
