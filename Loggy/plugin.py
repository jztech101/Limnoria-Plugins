
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


Class = Loggy


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
