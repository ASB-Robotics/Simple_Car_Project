import curses

# Simple console based controller accepting keyboard arrow commands to control car

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

try
    screen.addstr(0,0,'Command')
    while True
        char = screen.getch()
        if char == ord('q')
            break
        elif char == curses.KEY_RIGHT
            screen.addstr(0, 0, 'RIGHT  ')
            # TODO Issue RIGHT command socket message
        elif char == curses.KEY_LEFT
            screen.addstr(0, 0, 'LEFT   ')
        elif char == curses.KEY_UP
            screen.addstr(0, 0, 'FAST   ')
        elif char == curses.KEY_DOWN
            screen.addstr(0, 0, 'SLOW   ')
        else
            screen.addstr(0,0, 'UNKNOWN ')
finally
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()


