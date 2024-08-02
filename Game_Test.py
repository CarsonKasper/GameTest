import time
import keyboard

board = """{0}{1}{2}
{3}{4}{5}
{6}{7}{8}"""
x = 1
y = 3
while True:
    if keyboard.is_pressed('a'):
        x = x - 1
    if keyboard.is_pressed('d'):
        x = x + 1
    if keyboard.is_pressed('w'):
        y = y - 3
    if keyboard.is_pressed('s'):
        y = y + 3

    if x < 0:
        x = 0
    if x > 2:
        x = 2
    if y < 0:
        y = 0
    if y > 6:
        y = 6

    location = x + y

    zero = 1
    one = 1
    two = 1
    three = 1
    four = 1
    five = 1
    six = 1
    seven = 1
    eight = 1

    if location == 0:
        zero = 0
    elif location == 1:
        one = 0
    elif location == 2:
        two = 0
    elif location == 3:
        three = 0
    elif location == 4:
        four = 0
    elif location == 5:
        five = 0
    elif location == 6:
        six = 0
    elif location == 7:
        seven = 0
    else:
        eight = 0

    print(board.format(zero, one, two, three, four, five, six, seven, eight))
    print('\n')
    time.sleep(0.1)

