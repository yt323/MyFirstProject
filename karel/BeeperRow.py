"""
File: BeeperRow.py
Name:
-------------------------
This program makes Karel fill up
Street 1 with beepers
(This program should be world insensitive)
"""

from karel.stanfordkarel import *


def main():
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()

















####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)