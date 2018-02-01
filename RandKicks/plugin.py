
import supybot.utils as utils
import re

from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircmsgs as ircmsgs
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('RandKicks')
except ImportError:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x: x


class RandKicks(callbacks.Plugin):
    """RandKicks"""
    threaded = True
    def doPrivmsg(self,irc,msg):
        if msg.args[0].isalnum():
            return
        SpamDet = self.registryValue('spamDet',msg.args[0])
        FunDet = self.registryValue('funDet',msg.args[0])
        spamregexes = []
        spamkickmsg = []
        funregexes = []
        funkickmsg = []
        spamregexes.append('.*▄.*▄.*')
        spamkickmsg.append('Spam')
        #spamregexes.append('test2')
        #spamkickmsg.append('Spam2')
        funregexes.append('.*i.*l.*o.*v.*e.*W.*i.*l.*l.*y.*o.*u.*m.*e.*')
        funkickmsg.append("No")
        #funregexes.append('test3')
        #funkickmsg.append('Testing2')
        if SpamDet:
            for i in range(0, len(spamregexes)):
                if re.match(spamregexes[i],' '.join(msg.args[1:]), re.IGNORECASE):
                    irc.queueMsg(ircmsgs.kick(msg.args[0],msg.nick,spamkickmsg[i])) 
        if FunDet:
            for i in range(0, len(funregexes)):
                if re.match(funregexes[i],' '.join(msg.args[1:]), re.IGNORECASE):
                    irc.queueMsg(ircmsgs.kick(msg.args[0],msg.nick,funkickmsg[i]))
Class = RandKicks


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
