import curses


# Use list addition with the += operator
def flatten_list(the_lists):
    result = []
    for _list in the_lists:
        result += _list
    return result


import os


class ScreenCleaner:
    def __repr__(self):
        os.system('cls')  # This actually clears the screen
        return ''  # Because that's what repr() likes


def cls(): print("\n" * 50)


def query_yes_no(stdscr, question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
            It must be "yes" (the default), "no" or None (meaning
            an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    stdscr = curses.initscr()

    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:

        stdscr.refresh()
        stdscr.addstr(20, 9, question + prompt)
        choice = stdscr.getkey()
        if default is not None and choice == "":
            stdscr.clear()
            stdscr.refresh()
            return valid[default]

        elif choice in valid:
            stdscr.clear()
            stdscr.refresh()
            return valid[choice]
        else:
            stdscr.clear()
            stdscr.addstr(22, 9, "Please respond with y or no to continue).\n")
            stdscr.refresh()
