
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
def isChan(chan, checkprefix):
    if not chan:
        return False
    elif chan.startswith("#"):
        return True
    elif checkprefix and len(chan) >= 2 and not chan[0].isalnum() and chan[1] == "#":
        return True
    else:
        return False

class Loggy(callbacks.Plugin):
    """Loggy"""
    threaded = True
    def doNotice(self, irc, msg):
        logChannel = self.registryValue('logChan')
        if not logChannel:
            return
        if isChan(msg.args[0], True):
            irc.queueMsg(ircmsgs.privmsg(logChannel, "[Notice] " + msg.prefix + ': (' +msg.args[0]+ ') '  +' '.join(msg.args[1:])))
        else:
            irc.queueMsg(ircmsgs.privmsg(logChannel, "[Notice] " + msg.prefix + ': '  +' '.join(msg.args[1:])))
    def doPrivmsg(self,irc,msg):
        logChannel = self.registryValue('logChan')
        if not logChannel or isChan(msg.args[0], True):
            return
        irc.queueMsg(ircmsgs.privmsg(logChannel, "[PM] " + msg.prefix + ': ' + ' '.join(msg.args[1:])))
    def doInvite(self, irc, msg):
        logChannel = self.registryValue('logChan')
        if not logChannel:
            return
        irc.queueMsg(ircmsgs.privmsg(logChannel, "[Invite] " + msg.prefix + ": " + msg.args[1]))
    def doPart(self, irc, msg):
        logChannel = self.registryValue('logChan')
        if not logChannel:
            return
        if msg.nick == self.nick:
            if len(msg.args) > 3:
                irc.queueMsg(ircmsgs.privmsg(logChannel, "[Part] " + msg.prefix + ': (' +msg.args[0]+ ') '  + msg.args[3:]))
            else:
                irc.queueMsg(ircmsgs.privmsg(logChannel, "[Part] " + msg.prefix + ': (' +msg.args[0]+ ') ')
    def doKick(self, irc, msg):
        logChannel = self.registryValue('logChan')
        if not logChannel:
            return
        if msg.nick == self.nick:
            if len(msg.args) > 3:
                irc.queueMsg(ircmsgs.privmsg(logChannel, "[Kick] " + msg.prefix + ': (' +msg.args[1]+ ') ' + msg.args[3:]))
            else:
                irc.queueMsg(ircmsgs.privmsg(logChannel, "[Kick] " + msg.prefix + ': (' +msg.args[1]+ ')')
   

Class = Loggy


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
