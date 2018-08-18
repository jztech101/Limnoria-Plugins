
import supybot.utils as utils
import re

from supybot.commands import *
import sys
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
def isChan(chan, checkprefix):
    if not chan:
        return False
    elif chan.startswith("#"):
        return True
    elif checkprefix and len(chan) >= 2 and not chan[0].isalnum() and chan[1] == "#":
        return True
    else:
        return False

class RandKicks(callbacks.Plugin):
    """RandKicks"""
    threaded = True
    def doPrivmsg(self,irc,msg):
        if not isChan(msg.args[0], True):
            return
        SpamDet = self.registryValue('spamDet',msg.args[0])
        FunDet = self.registryValue('funDet',msg.args[0])
        spamregexes = []
        spamkickmsg = []
        funregexes = []
        funkickmsg = []
        spamregexes.append('.*▄.*▄.*')
        spamkickmsg.append('Spam Script')
        spamregexes.append('Christel just posted this')
        spamkickmsg.append('Propoganda Spam')
        spamregexes.append('After the acquisition by Private Internet Access, Freenode is now being used')
        spamkickmsg.append('Propoganda Spam')
        spamregexes.append('wqz')
        spamkickmsg.append('Link Spam')
        #spamregexes.append('   .*')
        #spamkickmsg.append('Blank Space Spam')
        spamregexes.append('ADn2IJnTRyM')
        spamkickmsg.append('Link Spam')
        funregexes.append('something')
        funkickmsg.append("something else")
        #funregexes.append('test3')
        #funkickmsg.append('Testing2')
        msg2 = ircutils.stripFormatting(' '.join(msg.args[1:]))
        print(msg2)
        nicks = 0
        if SpamDet:
            for i in range(0, len(spamregexes)):
                if re.search(spamregexes[i],msg2, re.IGNORECASE):
                    irc.queueMsg(ircmsgs.kick(msg.args[0],msg.nick,spamkickmsg[i]))
                    return
            for i in msg2.split(" "):
                #print(i)
                if i in irc.state.channels[msg.args[0]].users:
                    nicks = nicks + 1
                if nicks >= 4:
                    irc.queueMsg(ircmsgs.kick(msg.args[0],msg.nick,"Mass Highlight Spam"))
                    return

        if FunDet:
            for i in range(0, len(funregexes)):
                if re.match(funregexes[i],msg2, re.IGNORECASE):
                    irc.queueMsg(ircmsgs.kick(msg.args[0],msg.nick,funkickmsg[i]))
                    return
Class = RandKicks


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
