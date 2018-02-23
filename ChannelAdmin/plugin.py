
import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircmsgs as ircmsgs
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('ChannelAdmin')
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

def kickx(irc, channel, nick, reason, sender):
        irc.queueMsg(ircmsgs.kick(channel, nick, "[" + sender + "] " +reason))

def getHostmask(nick, irc):
    hostmask = nick
    if "!" not in nick or "@" not in nick or ':' not in nick:
        hostmask = irc.state.nickToHostmask(nick)
        hostmask = "*!*@" + ircutils.hostFromHostmask(hostmask)
    return hostmask

class ChannelAdmin(callbacks.Plugin):
    """ChannelAdmin"""
    threaded = False
    def ban(self, irc, msg, args, channel, nick):
        """ ban """
        irc.queueMsg(ircmsgs.mode(channel, "+b", getHostmask(nick, irc)))
    ban = wrap(ban, ['op', ('haveHalfop+', _('ban')),'text'])

    def unban(self, irc, msg, args, channel, nick):
        """ unban """
        irc.queueMsg(ircmsgs.mode(channel, "-b", getHostmask(nick, irc)))
    unban = wrap(unban, ['op', ('haveHalfop+', _('unban')),'text'])

    def quiet(self, irc, msg, args, channel, nick):
        """ quiet """
        irc.queueMsg(ircmsgs.mode(channel, "+q", getHostmask(nick, irc)))
    quiet = wrap(quiet, ['op', ('haveHalfop+', _('quiet')),'text'])

    def unquiet(self, irc, msg, args, channel, nick):
        """ unquiet """
        irc.queueMsg(ircmsgs.mode(channel, "-q", getHostmask(nick, irc)))
    unquiet = wrap(unquiet, ['op', ('haveHalfop+', _('unquiet')),'text'])

    def kick(self, irc, msg, args, channel, nick):
        """ kick """
        nick = nick.split(" ")
        reason = "Your behavior is not conductive to the desired environment"
        if len(nick) > 1:
            reason = " ".join(nick[1:])
        if "," in nick[0]:
            for nic in nick[0].split(","):
                kickx(irc, channel, nic, reason, msg.nick)
        else:
            kickx(irc, channel, nick[0], reason, msg.nick)
    kick = wrap(kick, ['op', ('haveHalfop+', _('kick')),'text'])

    def kban(self, irc, msg, args, channel, nick):
        """ kban """
        nick = nick.split(" ")
        reason = "Your behavior is not conductive to the desired environment"
        if len(nick) > 1:
            reason = " ".join(nick[1:])
        kickx(irc,channel,nick[0], reason, msg.nick)
        irc.queueMsg(ircmsgs.mode(channel, "+b", getHostmask(nick[0], irc)))
    kban = wrap(kban, ['op', ('haveHalfop+', _('kickban')),'text'])

    def invite(self, irc, msg, args, channel, nick):
        """ invite """
        irc.queueMsg(ircmsgs.invite(channel, nick))
    invite = wrap(invite, ['op', ('haveHalfop+', _('invite')),'text'])

    def topic(self, irc, msg, args, channel, nick):
        """ topic """
        irc.queueMsg(ircmsgs.topic(channel, nick))
    topic = wrap(invite, ['op', ('haveHalfop+', _('topic')), 'text'])

    def mode(self, irc, msg, args, channel, nick):
        """ mode """
        irc.queueMsg(ircmsgs.mode(channel, nick))
    mode = wrap(mode, ['op', ('haveHalfop+', _('mode')), 'text'])

    def op(self, irc, msg, args, channel, nick):
        """ op """
        irc.queueMsg(ircmsgs.mode(channel, "+o", nick))
    mode = wrap(mode, ['op', ('haveHalfop+', _('op')), 'text'])

    def deop(self, irc, msg, args, channel, nick):
        """ deop """
        irc.queueMsg(ircmsgs.mode(channel, "-o", nick))
    mode = wrap(mode, ['op', ('haveHalfop+', _('deop')), 'text'])

    def voice(self, irc, msg, args, channel, nick):
        """ voice """
        irc.queueMsg(ircmsgs.mode(channel, "+v", nick))
    mode = wrap(mode, ['op', ('haveHalfop+', _('voice')), 'text'])

    def devoice(self, irc, msg, args, channel, nick):
        """ devoice """
        irc.queueMsg(ircmsgs.mode(channel, "-v", nick))
    mode = wrap(mode, ['op', ('haveHalfop+', _('devoice')), 'text'])


Class = ChannelAdmin


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
