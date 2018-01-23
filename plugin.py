
import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircmsgs as ircmsgs
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('Loggy')
except ImportError:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x: x


class Loggy(callbacks.Plugin):
    """Loggy"""
    threaded = True
    def doNotice(self, irc, msg):
        logChannel = self.registryValue('LogChan')
        if not logChannel or not logChannel.startswith("#"):
            return
        if msg.args[0].startswith('#'):
            irc.queueMsg(ircmsgs.privmsg(logChannel, "[Notice] " + msg.prefix + ': (' +msg.args[0]+ ') '  +' '.join(msg.args[1:])))
        else:
            irc.queueMsg(ircmsgs.privmsg(logChannel, "[Notice] " + msg.prefix + ': '  +' '.join(msg.args[1:])))
    def doPrivmsg(self,irc,msg):
        logChannel = self.registryValue('LogChan')
        if not logChannel or msg.args[0].startswith("#") or not logChannel.startswith("#"):
            return
        irc.queueMsg(ircmsgs.privmsg(logChannel, "[PM] " + msg.prefix + ': ' + ' '.join(msg.args[1:])))
    def act2(self, irc, msg, args, something):
        """ acts """
        channel = msg.args[0]
        idex = 0
        if len(something) > 1 and something[0].startswith('#'):
            channel = something[0]
            idex = 1
        irc.queueMsg(ircmsgs.action(channel, ' '.join(something[idex:])))

    act2 = wrap(act2, ['owner', many('something')])

    def say2(self, irc, msg, args, something):
        """ says """
        channel = msg.args[0]
        idex = 0
        if len(something) > 1 and something[0].startswith('#'):
            channel = something[0]
            idex = 1
        irc.queueMsg(ircmsgs.privmsg(channel, ' '.join(something[idex:])))
    say2 = wrap(say2, ['owner', many('something')])



Class = Loggy


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
