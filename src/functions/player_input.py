
#!/usr/bin/env python3
from functions.next_wave import next_wave
from colorama import init, Fore
init(autoreset=True)
from colorama import init
import curses
init(autoreset=True)



def game_command(stdscr ,player_input):
    if player_input=='/h ':
        stdscr.clear()
        stdscr.refresh()
        stdscr.addstr(10, 10, f'''

                  Goal of the game survive as long as you can
                  You can break cubes only if at least 2 of adjusted cubes are same color,
                  you get score for breaking yellow blocks,
                  you get no points from breaking anather colors 
                  you get -1 point for every break attempt 
                  the more adjusted yellow blocks are, the bigger score reward
                  Good luck !

                  commands /h- help

                  press any key to contiune 
                  ''')

        stdscr.getkey()

def query_yes_no(stdscr ,question, default="yes"):
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
        stdscr.addstr(20,9,question + prompt)
        choice=stdscr.getkey()
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
            stdscr.addstr(22,9,"Please respond with y or no to continue).\n")
            stdscr.refresh()





def player_input(stdscr,level, game_state):
    x=''
    while len(x) < 3:
        player_inp = stdscr.getkey()


        if player_inp == 'q':
            stdscr.clear()
            stdscr.refresh()
            game_state = 'game_over'
            break
        if player_inp == ' ':
            if x == '':
                x = ' '
            stdscr.clear()
            stdscr.refresh()
            break
        x += player_inp

    # TODO doesnt work
    if '/' in x:
        game_command(stdscr, x)
    if x == ' ':

        try:
            level, game_state = next_wave(level, game_state)
        except:
            game_state='game_over'
    else:
        try:
            level.grid = level.grid.break_group(int(x))
            stdscr.clear()
            stdscr.refresh()
        except:
            pass
    curses.echo()

    return level, game_state