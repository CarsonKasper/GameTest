import time
import keyboard

board = """{0}{1}{2}
{3}{4}{5}
{6}{7}{8}"""

x, y = 1, 3

while True:
    if keyboard.is_pressed('a'): x = max(0, x - 1)
    if keyboard.is_pressed('d'): x = min(2, x + 1)
    if keyboard.is_pressed('w'): y = max(0, y - 3)
    if keyboard.is_pressed('s'): y = min(6, y + 3)

    boardset = [1] * 9
    boardset[x + y] = 0

    print(board.format(*boardset))
    print('\n')
    time.sleep(0.1)