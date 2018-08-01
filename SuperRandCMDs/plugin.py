
import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircmsgs as ircmsgs
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import supybot.schedule as schedule
import time
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
            if 'Celena' in irc.state.channels[msg.args[0]].users:
                irc.sendMsg(ircmsgs.privmsg(msg.args[0],'$shrug'))
            if 'Cassi' in irc.state.channels[msg.args[0]].users:
                irc.sendMsg(ircmsgs.privmsg(msg.args[0],'+shrug'))
            if 'Cindie' in irc.state.channels[msg.args[0]].users:
                irc.sendMsg(ircmsgs.privmsg(msg.args[0],'-shrug'))
            if 'OCBot' in irc.state.channels[msg.args[0]].users:
                irc.sendMsg(ircmsgs.privmsg(msg.args[0],'@@shrug'))
            if 'Botergos' in irc.state.channels[msg.args[0]].users:
                irc.sendMsg(ircmsgs.privmsg(msg.args[0],'!shrug'))
            schedule.addEvent(irc.reply, time.time() + 1, 'delay shrug', ['┻━┻ ︵ ¯\_(ツ)_/¯ ︵ ┻━┻'])
        else:
            irc.reply('┻━┻ ︵ ¯\_(ツ)_/¯ ︵ ┻━┻')

    def ping(self, irc, msg, args):
        """ ping """
        if self.registryValue("super",msg.args[0]):
            if 'Celena' in irc.state.channels[msg.args[0]].users:
                irc.sendMsg(ircmsgs.privmsg(msg.args[0],'$ping'))
            if 'Cassi' in irc.state.channels[msg.args[0]].users:
                irc.sendMsg(ircmsgs.privmsg(msg.args[0],'+ping'))
            if 'Cindie' in irc.state.channels[msg.args[0]].users:
                irc.sendMsg(ircmsgs.privmsg(msg.args[0],'-ping'))
            schedule.addEvent(irc.reply, time.time() + 1, 'delay pong', ['pong'])
        else:
            irc.reply('pong')


    def moo(self, irc, msg, args):
        """ moo """
        if self.registryValue("super",msg.args[0]):
            if 'Celena' in irc.state.channels[msg.args[0]].users:
                irc.sendMsg(ircmsgs.privmsg(msg.args[0],'$moo'))
            if 'Cassi' in irc.state.channels[msg.args[0]].users:
                irc.sendMsg(ircmsgs.privmsg(msg.args[0],'+moo'))
            if 'Cindie' in irc.state.channels[msg.args[0]].users:
                irc.sendMsg(ircmsgs.privmsg(msg.args[0],'-moo'))
            schedule.addEvent(irc.reply, time.time() + 1, 'delay moo', ['MoooooooOooooOooooooOoooo'])
        else:
            irc.reply('Mooo0ooooOOOOOoooooo')

    def pong(self, irc, msg, args):
        """ pong """
        if self.registryValue("super",msg.args[0]):
            if 'Celena' in irc.state.channels[msg.args[0]].users:
                irc.sendMsg(ircmsgs.privmsg(msg.args[0],'$pong'))
            if 'Cassi' in irc.state.channels[msg.args[0]].users:
                irc.sendMsg(ircmsgs.privmsg(msg.args[0],'+pong'))
            if 'Cindie' in irc.state.channels[msg.args[0]].users:
                irc.sendMsg(ircmsgs.privmsg(msg.args[0],'-pong'))
            schedule.addEvent(irc.reply, time.time() + 1, 'delay ping', ['ping'])
        else:
            irc.reply('ping')


    def potato(self, irc, msg, args):
        """ potato """
        if self.registryValue("super",msg.args[0]):
            if 'Celena' in irc.state.channels[msg.args[0]].users:
                irc.sendMsg(ircmsgs.privmsg(msg.args[0],'$potato'))
            if 'Cassi' in irc.state.channels[msg.args[0]].users:
                irc.sendMsg(ircmsgs.privmsg(msg.args[0],'+potato'))
            if 'Cindie' in irc.state.channels[msg.args[0]].users:
                irc.sendMsg(ircmsgs.privmsg(msg.args[0],'-potato'))
            schedule.addEvent(irc.reply, time.time() + 1, 'delay potato', ["is a potato"], {"action":True})
        else:
            irc.reply("is a potato", action=True)


    def burn(self, irc, msg, args):
        """ burn """
        if self.registryValue("super",msg.args[0]):
            if 'Celena' in irc.state.channels[msg.args[0]].users:
                irc.sendMsg(ircmsgs.privmsg(msg.args[0],'$burn'))
            if 'Cassi' in irc.state.channels[msg.args[0]].users:
                irc.sendMsg(ircmsgs.privmsg(msg.args[0],'+burn'))
            if 'Cindie' in irc.state.channels[msg.args[0]].users:
                irc.sendMsg(ircmsgs.privmsg(msg.args[0],'-burn'))
            schedule.addEvent(irc.reply, time.time() + 1, 'delay burn', ["watches the world burn"], {"action":True})
        else:
            irc.reply("watches the world burn", action=True)


Class = SuperRandCMDs


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
