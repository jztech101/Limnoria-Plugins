
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
        spamkickmsg.append('Spam Script')
        #spamregexes.append('test2')
        #spamkickmsg.append('Spam2')
        funregexes.append('.*i.*l.*o.*v.*e.*W.*i.*l.*l.*y.*o.*u.*m.*e.*')
        funkickmsg.append("No")
        #funregexes.append('test3')
        #funkickmsg.append('Testing2')
        nicks = 0
        if SpamDet:
            for i in range(0, len(spamregexes)):
                if re.match(spamregexes[i],' '.join(msg.args[1:]), re.IGNORECASE):
                    irc.queueMsg(ircmsgs.kick(msg.args[0],msg.nick,spamkickmsg[i]))
                    return
            for i in str(msg.args[1:]).split(" "):
                i = re.sub(r'\W+','',i)
                if i in irc.state.channels[msg.args[0]].users:
                    nicks = nicks + 1
                if nicks >= 3:
                    irc.queueMsg(ircmsgs.kick(msg.args[0],msg.nick,"Mass Highlight Spam"))
                    return

        if FunDet:
            for i in range(0, len(funregexes)):
                if re.match(funregexes[i],' '.join(msg.args[1:]), re.IGNORECASE):
                    irc.queueMsg(ircmsgs.kick(msg.args[0],msg.nick,funkickmsg[i]))
                    return
Class = RandKicks


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
