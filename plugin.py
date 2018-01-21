
import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('Loggy')
except ImportError:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x: x


class Loggy(callbacks.Plugin):
    """Loggy"""
    threaded = True


Class = Loggy


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
