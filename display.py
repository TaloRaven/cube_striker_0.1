import curses

from curses import  wrapper
from src.functions.game_loop import game_loop
def main(stdscr):
    stdscr.clear()
    stdscr.addstr(9,9,'111111111111111111111111111111111111')
    stdscr.addstr(9,9,'overwriten')
    game_loop()
    stdscr.refresh()
    stdscr.getch()


wrapper(main)