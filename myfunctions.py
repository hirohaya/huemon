from sys import stdout
from time import sleep

#Print one character at time in one line
def print_char(text):
    for char in text:
        stdout.write(char)
        sleep(0.01)
