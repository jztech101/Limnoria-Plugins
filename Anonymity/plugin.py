
import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircmsgs as ircmsgs
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('Anonymity')
except ImportError:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x: x


class Anonymity(callbacks.Plugin):
    """Anonymity"""
    threaded = False
    def act(self, irc, msg, args, something):
        """ acts """
        if ircutils.isChannel(msg.args[0]):
            channel = msg.args[0]
        else:
            channel = msg.nick
        idex = 0
        if len(something) > 1 and something[0].startswith('#'):
            channel = something[0]
            idex = 1
        irc.queueMsg(ircmsgs.action(channel, ' '.join(something[idex:])))

    act = wrap(act, ['owner', many('something')])

    def say(self, irc, msg, args, something):
        """ says """
        if ircutils.isChannel(msg.args[0]):
            channel = msg.args[0]
        else:
            channel = msg.nick
        idex=0
        if len(something) > 1 and (something[0].startswith('#') or (not something[0][0].isalnum() and something[0][1] == "#")):
            channel = something[0]
            idex = 1
        irc.queueMsg(ircmsgs.privmsg(channel, ' '.join(something[idex:])))
    say = wrap(say, ['owner', many('something')])



Class = Anonymity


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
