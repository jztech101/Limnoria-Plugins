
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
def getHostname(nick, irc):
    return ircutils.hostFromHostmask(irc.state.nickToHostmask(nick))

class TimeBomb(callbacks.Plugin):
    """TimeBomb"""

    def __init__(self, irc):
        self.__parent = super(TimeBomb, self)
        self.__parent.__init__(irc)
        self.bomb = False
        self.bombtarget = ""
        self.chan = ""
        self.sender = ""
        self.rng = random.Random()
        self.rng.seed()
        self.goodWire = ""
        self.wires = ['Blue', 'Green', 'Red', 'Yellow', 'Pink', 'Purple', 'Orange', 'Black', 'Gray', 'White', 'Brown']
    def timebomb(self, irc, msg, args, something):
        """TimeBomb"""
        if not isChan(msg.args[0], True) or not self.registryValue("bombsEnabled",msg.args[0]):
            return
        elif self.bomb:
            irc.reply("A bomb is already running with seconds on the clock, please wait until it explodes (or gets defused)")
            return
        nick = msg.nick
        if len(something) > 0 and something[0] in irc.state.channels[msg.args[0]].users and something[0] != irc.nick:
            nick = something[0]
        if self.registryValue("bombsExempt",msg.args[0]):
            for x in self.registryValue("bombsExempt",msg.args[0]).split(","):
               if x == getHostname(nick, irc):
                  nick = msg.nick
                  break
        self.bombtarget = nick
        self.bomb = True
        self.sender = msg.nick
        self.goodWire = self.rng.choice(self.wires)
        logChannel = self.registryValue('logChan')
        self.chan = msg.args[0]
        if logChannel:
            irc.queueMsg(ircmsgs.privmsg(logChannel, "[TimeBomb] " + msg.prefix + ': (' + self.chan + ') A bomb has been shoved down ' + self.bombtarget + '\'s underwear, the good wire is the ' + self.goodWire + ' one'))
        irc.reply('A bomb has been shoved inside ' + self.bombtarget + '\'s underwear, it will detonate in 60 seconds. These are the wires: ' + ' '.join(self.wires))
        #schedule.removeEvent('detonate')
        schedule.addEvent(self.detonate, time.time() + 59, 'detonate', [irc, msg])
    timebomb = wrap(timebomb, [optional(many('something'))])
    def cut(self, irc, msg, args, something):
        """cut"""
        if not self.bomb:
            return
        if msg.nick == self.bombtarget:
            if len(something) > 0 and self.goodWire.lower() == something[0].lower():
                self.bombtarget = self.sender
                self.sender = msg.nick
                irc.reply("The bomb has been defused and is sent back with seconds on the clock!")
            else:
                self.detonate(irc, msg)
        else:
            self.bombtarget = msg.nick
            irc.reply("Uh-Oh. The bomb has suddenly moved itself into " + self.bombtarget + '\'s underwear')
    cut = wrap(cut, [optional(many('something'))])
    def detonate(self, irc, msg):
        """ detonate """
        if self.bomb:
            if not irc.state.channels[self.chan].isOp(irc.nick) and self.registryValue("bombDefenseEnabled", msg.args[0]):
                irc.sendMsg(ircmsgs.privmsg("chanserv", "op " + self.chan))
            schedule.addEvent(irc.queueMsg, time.time() + 1, 'detonating', [ircmsgs.kick(self.chan, self.bombtarget, "KA-BOOOOOOOOOOOOOOOOM!")])
            self.bomb = False
        schedule.removeEvent('detonate')
Class = TimeBomb


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
