import curses
import socket
import sys
import time
import RPi.GPIO as GPIO

"""The following defines the motors A and B and the second attribute is forward or backward"""
motor_af = 37
motor_ab = 33
motor_bf = 36
motor_bb = 32

def writeLine( s ):
    """Using curses let's display a line of information"""
    screen.addstr( 0, 0, '                    ' )
    screen.addstr( 0, 0, s )
    return

def sendLine( s ):
    """For socket connections let's send a line to the other side"""
    HOST, PORT = "localhost", 9999
    sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    try:
        sock.connect( ( HOST, PORT ) )
        sock.sendall( s + "\n")
        writeLine( sock.recv( 1024 ) )
    finally:
        sock.close()
    return

############################################################################
##  Initialize
############################################################################

GPIO.setmode(GPIO.BOARD)
GPIO.setup(motor_af,GPIO.OUT)
GPIO.setup(motor_ab,GPIO.OUT)
GPIO.setup(motor_bf,GPIO.OUT)
GPIO.setup(motor_bb,GPIO.OUT)
GPIO.output(motor_af,GPIO.LOW)
GPIO.output(motor_ab,GPIO.LOW)
GPIO.output(motor_bf,GPIO.LOW)
GPIO.output(motor_bb,GPIO.LOW)

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
            GPIO.output(motor_ab,GPIO.LOW)
            GPIO.output(motor_bf,GPIO.LOW)
            GPIO.output(motor_bb,GPIO.HIGH)
            GPIO.output(motor_af,GPIO.HIGH)
            #sendLine( 'RIGHT' )
        elif char == curses.KEY_LEFT:
            writeLine( 'LEFT' )
            GPIO.output(motor_af,GPIO.LOW)
            GPIO.output(motor_bb,GPIO.LOW)
            GPIO.output(motor_bf,GPIO.HIGH)
            GPIO.output(motor_ab,GPIO.HIGH)
            #sendLine( 'LEFT' )
        elif char == curses.KEY_UP:
            writeLine( 'FORWARD' )
            GPIO.output(motor_ab,GPIO.LOW)
            GPIO.output(motor_bb,GPIO.LOW)
            GPIO.output(motor_af,GPIO.HIGH)
            GPIO.output(motor_bf,GPIO.HIGH)
            #sendLine( 'FAST' )
        elif char == curses.KEY_DOWN:
            writeLine( 'BACKWARDS' )
            GPIO.output(motor_af,GPIO.LOW)
            GPIO.output(motor_bf,GPIO.LOW)
            GPIO.output(motor_ab,GPIO.HIGH)
            GPIO.output(motor_bb,GPIO.HIGH)
            #sendLine( 'SLOW' )
        else:
            writeLine( 'UNKNOWN' )
finally:
    curses.nocbreak()
    screen.keypad( 0 )
    curses.echo()
    curses.endwin()
    GPIO.cleanup()
