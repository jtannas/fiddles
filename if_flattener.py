"""
Fiddle to see if I can make something to 'flatten' an n-level if
statement using a list.
"""

### IMPLEMENTATION ############################################################
from collections import namedtuple
from functools import partial


class IfCall():
    """Class container for an if statement.

    Typical use case is for flattening an if statement via a list of
    IfCall objects. Supports lazy evaluation of the condition if it is
    provided as a function or as a partial function.

    Typical use:
    -------------------------------------------------------
        if_calls = [
            IfCall(...),
            IfCall(...),
            IfCall(...),
            IfCall(...),
            IfCall(...),
        ]

        for if_call in if_calls:
            branch = if_call.active_branch
            if callable(if_call.func) is True:
                if_call.func()
            if if_call.break_ is True:
                break
        else:
            print('Loop executed without breaking.')
    -------------------------------------------------------

    """

    def __init__(
            self,
            condition,  # Supports bool, functions, and partials
            true_func=None,
            false_func=None,
            true_break: bool=False,
            false_break: bool=False):
        """Init the class members with the inputs.

        Args:
            - condition: if <condition> is True...
            - true_func: return this if condition is true
            - false_func: return this if conditon is false
            - true_break (boolean): signal on whether to break after true_func
            - false_break (boolean): signal on whther to break after false_func

        """

        self.__dict__.update(
            {k: v for k, v in locals().items() if k != 'self'}
             )  # yapf: disable

    @property
    def _condition_val(self):
        """Evaluates the provided condition."""
        return self.condition() if callable(self.condition) else self.condition

    @property
    def active_branch(self):
        """Returns the branch that is pointed to by self.condition ."""
        branch = namedtuple('branch', 'condition func break_')

        if self._condition_val is True:
            b = branch(True, self.true_func, self.true_break)
        else:
            b = branch(False, self.false_func, self.false_break)
        return b

    @property
    def inactive_branch(self):
        """Return the branch that isn't pointed to by self.condition ."""
        branch = namedtuple('branch', 'condition func break_')

        if self._condition_val is not True:
            b = branch(False, self.false_func, self.false_break)
        else:
            b = branch(True, self.true_func, self.true_break)
        return b


### EXAMPLE ###################################################################
def smaller_than(num1, num2):
    """Example function to demonstrate lazy evaluation."""
    return num1 < num2


if_calls = [
    IfCall(
        condition=(1 == 1),  # Immediate Evaluation
        true_func=partial(print, '1 is 1'),
        true_break=False,
        false_func=partial(print, '1 is not 1'),
        false_break=True),
    IfCall(
        condition=partial(smaller_than, 2, 1),  # Lazy Evaluation
        true_func=partial(print, '2 is smaller than 1'),
        true_break=False,
        false_func=partial(print, '2 is not smaller than 1'),
        false_break=False),
]

for if_call in if_calls:
    branch = if_call.active_branch
    if callable(branch.func) is True:
        branch.func()
    if branch.break_ is True:
        break
else:
    print('Loop executed without breaking.')
