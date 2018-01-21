
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
    irc.queueMsg(ircmsgs.privmsg('#techcavern', msg))
    logChannel = self.registryValue('LogChan')
    if logChannel is None:
        return
    irc.queueMsg(ircmsgs.privmsg(logChannel, msg))


Class = Loggy


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
