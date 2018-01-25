
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
        logChannel = self.registryValue('logChan')
        if not logChannel or not logChannel.startswith("#"):
            return
        if not msg.args[0].isalnum():
            irc.queueMsg(ircmsgs.privmsg(logChannel, "[Notice] " + msg.prefix + ': (' +msg.args[0]+ ') '  +' '.join(msg.args[1:])))
        else:
            irc.queueMsg(ircmsgs.privmsg(logChannel, "[Notice] " + msg.prefix + ': '  +' '.join(msg.args[1:])))
    def doPrivmsg(self,irc,msg):
        logChannel = self.registryValue('logChan')
        if not logChannel or not msg.args[0].isalnum() or not logChannel.startswith("#"):
            return
        irc.queueMsg(ircmsgs.privmsg(logChannel, "[PM] " + msg.prefix + ': ' + ' '.join(msg.args[1:])))
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



Class = Loggy


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
