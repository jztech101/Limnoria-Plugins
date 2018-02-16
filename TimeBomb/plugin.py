
import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircmsgs as ircmsgs
import supybot.schedule as schedule
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import random
import time
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('RandCMDs')
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

class TimeBomb(callbacks.Plugin):
    """TimeBomb"""

    def __init__(self, irc):
        self.timebomb = False
        self.bombtarget = ""
        self.chan = ""
        self.rng = random.Random()
        self.rng.seed()
        self.goodWire = ""
        self.wires = ['Blue', 'Green', 'Red', 'Yellow', 'Pink', 'Purple', 'Orange', 'Black', 'Gray', 'White', 'Brown']
    def timebomb(self, irc, msg, args):
        """TimeBomb"""
        if not isChan(msg.args[0], True) or not self.registryValue(self,msg.args[0],"TimeBomb"):
            return
        if msg.args[1] not in irc.state.channels[msg.args[0]].users:
            self.bombtarget = self.sender
        else:
            self.bombtarget = msg.args[1]
        self.timebomb = True
        self.goodWire = self.rng.choice(self.wires)
        logChannel = self.registryValue('logChan')
        self.chan = msg.args[0]
        irc.queueMsg(ircmsgs.privmsg(logChannel, "[TimeBomb] " + msg.prefix + ': (' + self.chan + ') A bomb has been shoved down ' + self.bombtarget + '\'s pants, the good wire is the ' + self.goodWire + ' one')))
        irc.reply('A bomb has been shoved inside ' + self.bombtarget + '\'s underwear, it will detonate in 30 seconds. These are the wires: ' + ' '.join(self.wires))
        schedule.addEvent(self, self.detonate(irc), time.time() + 30, 'detonate')
    def cut(self, irc, msg, args, something):
        """cut"""
        if not self.timebomb:
            return
        if self.sender == self.bombtarget:
            if self.goodWire.toLower() == msg.args[1]:
                self.timebomb = False
                irc.reply("The bomb has been defused!")
            else:
                self.detonate(irc)
        else:
            self.bombtarget = self.sender
            irc.reply("Uh-Oh. The bomb has suddenly moved itself into " + self.bombtarget + '\'s pants')
    def detonate(self, irc):
        """ detonate """
        if self.timebomb:
            irc.queueMsg(ircmsgs.kick(self.chan, self.bombtarget, "KA-BOOOOOOOOOOOOOOOOM!"))
Class = TimeBomb


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
