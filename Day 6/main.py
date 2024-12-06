import os


def getPosition(testGrid):
    for y in range(len(testGrid)):
        for x in range(len(testGrid)):
            if testGrid[y][x] == '^':
                return [y, x]


def checkValid(testGrid, checkPos):
    if checkPos[0] >= len(testGrid):
        return False
    elif checkPos[0] < 0:
        return False
    if checkPos[1] >= len(testGrid[0]):
        return False
    elif checkPos[1] < 0:
        return False
    return True


def moveForward(testGrid, testDirection, testPosition):
    if testDirection == 'north':
        if not checkValid(testGrid, [testPosition[0] - 1, testPosition[1]]):
            return 'EXIT'
        if testGrid[testPosition[0] - 1][testPosition[1]] == "#":
            return False
        else:
            testGrid[testPosition[0] - 1][testPosition[1]] = "^"
            testGrid[testPosition[0]][testPosition[1]] = "X"
            return True
    if testDirection == 'east':
        if not checkValid(testGrid, [testPosition[0], testPosition[1] + 1]):
            return 'EXIT'
        if testGrid[testPosition[0]][testPosition[1] + 1] == "#":
            return False
        else:
            testGrid[testPosition[0]][testPosition[1] + 1] = "^"
            testGrid[testPosition[0]][testPosition[1]] = "X"
            return True
    if testDirection == 'south':
        if not checkValid(testGrid, [testPosition[0] + 1, testPosition[1]]):
            return 'EXIT'
        if testGrid[testPosition[0] + 1][testPosition[1]] == "#":
            return False
        else:
            testGrid[testPosition[0] + 1][testPosition[1]] = "^"
            testGrid[testPosition[0]][testPosition[1]] = "X"
            return True
    if testDirection == 'west':
        if not checkValid(testGrid, [testPosition[0], testPosition[1] - 1]):
            return 'EXIT'
        if testGrid[testPosition[0]][testPosition[1] - 1] == "#":
            return False
        else:
            testGrid[testPosition[0]][testPosition[1] - 1] = "^"
            testGrid[testPosition[0]][testPosition[1]] = "X"
            return True


def printableGrid(testGrid):
    returnStr = ''
    for y in testGrid:
        returnStr += ''.join(y) + '\n'
    return returnStr


def turnDir(currentDir):
    s = {'north': 'east', 'east': 'south', 'south': 'west', 'west': 'north'}
    return s[currentDir]

def testStuck():
    """"""

with open(os.path.abspath('./small_input.txt'), 'r') as f:
    """
    For grid, it's y then x because it's easier
    """
    fileText = f.read()

    grid = [list(x) for x in fileText.split('\n')]

    guard_position = getPosition(grid)

    guard_direction = 'north'
    """
    north, south, east, west
    """

    """Part one:"""
    moving = True
    while moving:
        move = moveForward(grid, guard_direction, guard_position)
        guard_position = getPosition(grid)
        if move == 'EXIT':
            break
        if not move:
            guard_direction = turnDir(guard_direction)
        # print(printableGrid(grid))

    count = printableGrid(grid).count('X') + 1
    print("Part one:", count)

    """Part two:"""


