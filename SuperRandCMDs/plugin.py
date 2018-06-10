
import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircmsgs as ircmsgs
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('SuperRandCMDs')
except ImportError:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x: x


class SuperRandCMDs(callbacks.Plugin):
    """SuperRandCMDs"""
    threaded = False
    def shrug(self, irc, msg, args):
        """ shrug """
        if self.registryValue("super",msg.args[0]):
            irc.sendMsg(ircmsgs.privmsg(msg.args[0],'$shrug'))
            irc.sendMsg(ircmsgs.privmsg(msg.args[0],'+shrug'))
            irc.sendMsg(ircmsgs.privmsg(msg.args[0],'-shrug'))
        irc.reply('┻━┻ ︵ ¯\_(ツ)_/¯ ︵ ┻━┻')
    def ping(self, irc, msg, args):
        """ ping """
        if self.registryValue("super",msg.args[0]):
            irc.sendMsg(ircmsgs.privmsg(msg.args[0],'$ping'))
            irc.sendMsg(ircmsgs.privmsg(msg.args[0],'+ping'))
            irc.sendMsg(ircmsgs.privmsg(msg.args[0],'-ping'))
        irc.reply('pong')


    def moo(self, irc, msg, args):
        """ moo """
        if self.registryValue("super",msg.args[0]):
            irc.sendMsg(ircmsgs.privmsg(msg.args[0],'$moo'))
            irc.sendMsg(ircmsgs.privmsg(msg.args[0],'+moo'))
            irc.sendMsg(ircmsgs.privmsg(msg.args[0],'-moo'))
        irc.reply('Mooo0ooooOOOOOoooooo')

    def pong(self, irc, msg, args):
        """ pong """
        if self.registryValue("super",msg.args[0]):
            irc.sendMsg(ircmsgs.privmsg(msg.args[0],'$pong'))
            irc.sendMsg(ircmsgs.privmsg(msg.args[0],'+pong'))
            irc.sendMsg(ircmsgs.privmsg(msg.args[0],'-pong'))
        irc.reply('ping')


    def potato(self, irc, msg, args):
        """ potato """
        if self.registryValue("super",msg.args[0]):
            irc.sendMsg(ircmsgs.privmsg(msg.args[0],'$potato'))
            irc.sendMsg(ircmsgs.privmsg(msg.args[0],'+potato'))
            irc.sendMsg(ircmsgs.privmsg(msg.args[0],'-potato'))
        irc.reply("is a potato", action=True)

Class = SuperRandCMDs


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
