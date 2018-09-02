
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
        FunDet = self.registryValue('funDet',msg.args[0])
        kickstr = "KICK"
        funregexes.append('something')
        funkickmsg.append("something else")

        if FunDet:
            for i in range(0, len(funregexes)):
                if re.match(funregexes[i],msg2, re.IGNORECASE):
                    irc.queueMsg(ircmsgs.IrcMsg(prefix='', command=kickstr,
                      args=(msg.args[0], msg.nick, funkickmsg[i]), msg=None))
                    return
Class = RandKicks


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
