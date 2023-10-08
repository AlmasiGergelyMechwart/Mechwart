row = 3
col = 3
board = []
for i in range(row):
    board.append([])
    for j in range(col):
        board[i].append(" ")

players = ["X", "O"]

def drawBoard():
    for i in range(row):
        for j in range(col):
            print(f"[{board[i][j]}]",end="")
        print()

def winTest():
    dontB = True
    for i in range(row):
        if dontB == False:
            break
        for j in range(col):
            if board[i][j] == " ":
                dontB = False
                break
    if dontB:
        return "D"

    for a in range(row):
        if board[a][a] != " ":
            temp = board[a][a]
        else:
            continue

        for i in range(row): # oszlop
            if temp != board[i][a]:
                break
        else:
            return temp
        
        for i in range(col): # sor
            if temp != board[a][i]:
                break
        else:
            return temp
        
    if row != col:
        return
        
    if board[0][0] != " ":
        temp = board[0][0]
        for i in range(1, row): # átló (bal fent - jobb lent)
            if temp != board[i][i]:
                break
        else:
            return temp
    
    if board[row-1][0] != " ":
        temp = board[row-1][0]
        for i in range(1, row): # átló (bal lent - jobb fent)
            if temp != board[row-1-i][i]:
                break
        else:
            return temp

def game():
    playerPos = [0, 0]
    currentPlayer = 0

    if row != col:
        print("Nem négyzet alakú pályán átlós nyereség nem lehetséges")

    while True:
        while True:
            drawBoard()

            print(f"{players[currentPlayer]} jön")
            playerPos[0] = input("sor: ")
            playerPos[1] = input("oszlop: ")
            try:
                playerPos[0] = int(playerPos[0])
                playerPos[1] = int(playerPos[1])
            except:
                print("A megadott érték nem egy egész szám")
                continue
            if (playerPos[0] < 1 or playerPos[0] > row) or (playerPos[1] < 1 or playerPos[1] > col):
                print("A megadott koordináta a pályán kívül esik")
                continue
            else:
                playerPos[0]-=1
                playerPos[1]-=1
            if board[playerPos[0]][playerPos[1]] == " ":
                board[playerPos[0]][playerPos[1]] = players[currentPlayer]
                break
            else:
                print("A meghatározott terület már foglalt")

        winner = winTest()
        if winner:
            drawBoard()
            if winner == "D":
                print("Döntetlen")
            else:
                print(f"{winner} nyert")
            break

        if currentPlayer == 0:
            currentPlayer = 1
        else:
            currentPlayer = 0


game()
