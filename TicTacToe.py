import sys

def TicTacToe():
    Places = ['1', '2', '3', '4', '5', '6', '7', '8', '9',]
    Xturn = 1
    while True:
        print(f'''[{Places[0]}][{Places[1]}][{Places[2]}]
[{Places[3]}][{Places[4]}][{Places[5]}]
[{Places[6]}][{Places[7]}][{Places[8]}]''')
        
        if (Places[0] == 'X' and Places[1] == 'X' and Places[2] == 'X') or (Places[3] == 'X' and Places[4] == 'X' and Places[5] == 'X') or (Places[6] == 'X' and Places[7] == 'X' and Places[8] == 'X') or (Places[0] == 'X' and Places[3] == 'X' and Places[6] == 'X') or (Places[1] == 'X' and Places[4] == 'X' and Places[7] == 'X') or (Places[2] == 'X' and Places[5] == 'X' and Places[8] == 'X') or (Places[0] == 'X' and Places[4] == 'X' and Places[8] == 'X') or (Places[2] == 'X' and Places[4] == 'X' and Places[6] == 'X'):
            print('X wins!')
            break
        if (Places[0] == 'O' and Places[1] == 'O' and Places[2] == 'O') or (Places[3] == 'O' and Places[4] == 'O' and Places[5] == 'O') or (Places[6] == 'O' and Places[7] == 'O' and Places[8] == 'O') or (Places[0] == 'O' and Places[3] == 'O' and Places[6] == 'O') or (Places[1] == 'O' and Places[4] == 'O' and Places[7] == 'O') or (Places[2] == 'O' and Places[5] == 'O' and Places[8] == 'O') or (Places[0] == 'O' and Places[4] == 'O' and Places[8] == 'O') or (Places[2] == 'O' and Places[4] == 'O' and Places[6] == 'O'):
            print('O wins!')
            break
        
        choice = input('What spot?')
        if choice.isdigit() == False:
            print("Spot Doesn't Exist")
            Xturn += 1
        else:
            choice = int(choice)
            if choice > 9 or choice < 1:
                print("Spot Doesn't Exist")
                Xturn += 1
            else:
                if Places[choice -1] == 'X' or Places[choice -1] == 'O':
                    print('That Spots Taken')
                    Xturn += 1
                else:
                    Places[choice - 1] = 'X' if Xturn == 1 else 'O'
        Xturn = abs(Xturn - 1)

if len(sys.argv) > 3:
    if sys.argv[1] == 'Super' and sys.argv[2] == 'Secret' and sys.argv[3] == 'Game':
        TicTacToe()
else:
    print('Nothing Weird Here')
