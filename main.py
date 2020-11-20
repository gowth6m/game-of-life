BOARD = [[]]


def drawEmptyBoard(width, height):
    global BOARD
    BOARD = [["." for x in range(width)] for y in range(height)]


def replacePoint(x, y):
    BOARD[x][y] = "#"


def drawInFormat(boardArr):
    for i in boardArr:
        print(i)
    print("-----------------")



if __name__ == '__main__':
    drawEmptyBoard(5, 6)
    drawInFormat(BOARD)
    replacePoint(1, 2)
    drawInFormat(BOARD)
