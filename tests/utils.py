from pathlib import Path
from thefuck import types
from thefuck.conf import DEFAULT_PRIORITY


def Command(script='', stdout='', stderr=''):
    return types.Command(script, stdout, stderr)


def Rule(name='', match=lambda *_: True,
         get_new_command=lambda *_: '',
         enabled_by_default=True,
         side_effect=None,
         priority=DEFAULT_PRIORITY,
         requires_output=True):
    return types.Rule(name, match, get_new_command,
                      enabled_by_default, side_effect,
                      priority, requires_output)


def CorrectedCommand(script='', side_effect=None, priority=DEFAULT_PRIORITY):
    return types.CorrectedCommand(script, side_effect, priority)


root = Path(__file__).parent.parent.resolve()
