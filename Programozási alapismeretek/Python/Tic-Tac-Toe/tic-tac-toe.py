sor = 3
oszlop = 3
# board = [" "*oszlop]*sor #ez nem jó mert nem tudom
board = [" "," "," "],[" "," "," "],[" "," "," "]
players = ["X", "O"]

def drawBoard():
    for i in range(sor):
        for j in range(oszlop):
            print(f"[{board[i][j]}]",end="")
        print()

# def winTest():
#     for i in range(sor)

def game():
    gameIsOn = True
    playerPos = [0, 0]
    currentPlayer = 0
    while gameIsOn:
        drawBoard()

        inputLoop = True
        while inputLoop:
            print(f"{players[currentPlayer]} jön")
            playerPos[0] = input("sor: ")
            playerPos[1] = input("oszlop: ")
            try:
                playerPos[0] = int(playerPos[0])
                playerPos[1] = int(playerPos[1])
            except:
                print("A megadott érték nem egy egész szám")
                continue
            if (playerPos[0] < 1 or playerPos[0] > sor) or (playerPos[1] < 1 or playerPos[1] > oszlop):
                print("A megadott koordináta a pályán kívül esik")
                continue
            else:
                playerPos[0]-=1
                playerPos[1]-=1
            if board[playerPos[0]][playerPos[1]] == " ":
                board[playerPos[0]][playerPos[1]] = players[currentPlayer]
                inputLoop = False
            else:
                print("A meghatározott terület már foglalt")

        # winTest()

        if currentPlayer == 0:
            currentPlayer = 1
        else:
            currentPlayer = 0


game()