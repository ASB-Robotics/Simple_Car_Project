import curses
import socket
import sys

def writeLine( s ):
    screen.addstr( 0, 0, '                    ' )
    screen.addstr( 0, 0, s )
    return

def sendLine( s ):
    HOST, PORT = "localhost", 9999
    sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    try:
        sock.connect( ( HOST, PORT ) )
        sock.sendall( s + "\n")
        writeLine( sock.recv( 1024 ) )
    finally:
        sock.close()
    return

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad( True )

try:
    writeLine( 'Car Command?' )
    while True:
        char = screen.getch()
        if char == ord( 'q' ):
            break
        elif char == curses.KEY_RIGHT:
            writeLine( 'RIGHT' )
            sendLine( 'RIGHT' )
        elif char == curses.KEY_LEFT:
            writeLine( 'LEFT' )
            sendLine( 'LEFT' )
        elif char == curses.KEY_UP:
            writeLine( 'FAST' )
            sendLine( 'FAST' )
        elif char == curses.KEY_DOWN:
            writeLine( 'SLOW' )
            sendLine( 'SLOW' )
        else:
            writeLine( 'UNKNOWN' )
finally:
    curses.nocbreak()
    screen.keypad( 0 )
    curses.echo()
    curses.endwin()
