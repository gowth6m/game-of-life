BOARD = [[]]
PREVIOUS_BOARD = [[]]
LIST_OF_POINTS = [[]]

# SHAPES
DOBBY = [[1, 2], [1, 3], [2, 3], [3, 1], [0, 1]]


def drawEmptyBoard(width, height):
    global BOARD
    BOARD = [["." for x in range(width)] for y in range(height)]


def drawInFormat(boardArr):
    for i in boardArr:
        print(i)
    print(" ")


def replacePoint(x, y):
    BOARD[x][y] = "#"


def replacePoints(values):
    for pair in values:
        replacePoint(pair[0], pair[1])


def checkForNeighbour(point):
    for y in BOARD:
        if y == point[1]:
            for x in y:
                if x == point[0]:
                    if x == "#" and (y[y.index(x) - 1] == "#" or y[y.index(x) + 1] == "#"):
                        return True
    return False


def evolve():
    for y in BOARD:
        for x in y:
            if checkForNeighbour([(BOARD.index(y)), (y.index(x))]):
                y[y.index(x) - 1] = "x"


# def evolution():
#     for i in range(0, 5):
#         evolve()
#         drawInFormat(BOARD)


if __name__ == '__main__':
    drawEmptyBoard(5, 6)
    drawInFormat(BOARD)
    replacePoints(DOBBY)
    drawInFormat(BOARD)
    evolve()
    drawInFormat(BOARD)
    # evolution()
