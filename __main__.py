# the main(stdscri) method was adapted from https://stackoverflow.com/a/3524350
# this needs to be run on macOS through the command line

import curses
from game import Game


def main(stdscr):
    first_run = True
    # do not wait for input when calling getch
    stdscr.nodelay(1)
    app = Game(stdscr)
    while app.get_state():
        # get keyboard input, returns -1 if none available
        c = stdscr.getch()
        curses.curs_set(0)
        if first_run:
            first_run = setup_screen(stdscr)
            print("\x1b[8;24;160t")
        if c != -1:
            print(app.get_view())
            stdscr.refresh()
            if app.do_turn(c) == 0:
                quit_screen(stdscr)
                q = int(stdscr.getch())
                print(q)
                if q == 121:
                    print("in quit")
                    app.set_state(-1)
                    break
                else:
                    continue
            # return curser to start position
            print(app.get_view())
            stdscr.refresh()
            stdscr.move(0, 0)


def setup_screen(stdscr):
    frame = ""
    x = stdscr.getmaxyx()[0]
    y = stdscr.getmaxyx()[1]
    for i in range((x//2) - 2):
        frame += "\n"
    frame += "Gladiator".center(y)
    # frame += "\n"
    frame += "press any key".center(y)
    frame += ("x: " + str(x) + " y: " + str(y)).center(y)

    print_screen(stdscr, frame)
    return False


def quit_screen(stdscr):
    frame = ""
    x = stdscr.getmaxyx()[0]
    y = stdscr.getmaxyx()[1]
    for i in range((x//2) - 2):
        frame += "\n"
    frame += "Are you Sure you want to quit?".center(y)
    # frame += "\n"
    frame += "y/n".center(y)

    for i in range((x//2) - 2):
        frame += "\n"

    print_screen(stdscr, frame)


def print_screen(stdscr, frame=""):
    print(frame)


if __name__ == '__main__':
    curses.wrapper(main)
    # app = Game()
    # print(app.get_window())
