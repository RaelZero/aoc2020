import copy

def parseInput():
    input = []

    with open('input.txt') as inputFile:
        for line in inputFile:
            input.append(line[:-1]) # Skip the newline character

    return input

def partOne(input):
    result = simulate(input, 'adj')

    print("Part one: " + str(result))
    return(result)

def partTwo(input):
    result = simulate(input, 'vis')

    print("Part two: " + str(result))
    return(result)

def simulate(seats, criterion):
    currSeats = copy.deepcopy(seats)
    prevSeats = copy.deepcopy(seats)
    occupiedSeats = 0
    prevOccupiedSeats = 0

    changed = True

    if criterion == 'adj':
        checkMatrix = getAdjacencyMatrix(seats)
    if criterion == 'vis':
        checkMatrix = getVisibilityMatrix(seats)

    while changed == True:
        changed = False
        prevSeats = copy.deepcopy(currSeats)
        prevOccupiedSeats = occupiedSeats

        for row in range(len(prevSeats)):
            for column in range(len(prevSeats[row])):
                if prevSeats[row][column] == '.':
                    continue
                else:
                    toCheck = checkMatrix[row][column]

                    occupiedAdjacent = 0
                    for a in toCheck:
                        if prevSeats[a[0]][a[1]] == '#':
                            occupiedAdjacent += 1

                    if prevSeats[row][column] == 'L' and occupiedAdjacent == 0:

                        tmp = list(currSeats[row])
                        tmp[column] = '#'
                        currSeats[row] = ''.join(tmp)

                    elif prevSeats[row][column] == '#' and \
                        (occupiedAdjacent >= 4 and criterion == 'adj') \
                        or \
                        (occupiedAdjacent >= 5 and criterion == 'vis'):

                        tmp = list(currSeats[row])
                        tmp[column] = 'L'
                        currSeats[row] = ''.join(tmp)

        occupiedSeats = 0
        for row in range(len(currSeats)):
            for column in range(len(currSeats[row])):
                if currSeats[row][column] == '#':
                    occupiedSeats += 1

        if occupiedSeats != prevOccupiedSeats:
            changed = True

        #print("New state - occupied seats: " + str(occupiedSeats))

    return(occupiedSeats)

def getAdjacencyMatrix(seats):
    adjMatrix = []

    for row in range(len(seats)):
        adjMatrix.append([])

        for column in range(len(seats[row])):
            adjMatrix[row].append(getAdjacent(row, column, seats))

    #print(adjMatrix)
    return(adjMatrix)

def getAdjacent(row, column, seats):
    adj = [(r, c)
           for r in [row-1, row, row+1]
           if r in range(len(seats))

           for c in [column-1, column, column+1]
           if c in range(len(seats[row]))]

    adj.remove((row, column))

    #print(str((row, column)) + ' ' + str(adj))
    return(adj)

def getVisibilityMatrix(seats):
    visMatrix = []

    for row in range(len(seats)):
        visMatrix.append([])

        for column in range(len(seats[row])):
            visMatrix[row].append(getVisible(row, column, seats))

    #print(visMatrix)
    return(visMatrix)

# Horrible horrible horrible
def getVisible(row, column, seats):
    visible = []

    if seats[row][column] == '.':
        return(visible)

    # East
    i = column + 1
    while i < len(seats[row]):
        if seats[row][i] == '#' or seats[row][i] == 'L':
            visible.append((row, i))
            break
        i += 1

    # West
    i = column - 1
    while i >= 0:
        if seats[row][i] == '#' or seats[row][i] == 'L':
            visible.append((row, i))
            break
        i -= 1

    # North
    i = row + 1
    while i < len(seats):
        if seats[i][column] == '#' or seats[i][column] == 'L':
            visible.append((i, column))
            break
        i += 1

    # South
    i = row - 1
    while i >= 0:
        if seats[i][column] == '#' or seats[i][column] == 'L':
            visible.append((i, column))
            break
        i -= 1

    # North-East
    i = row + 1
    j = column + 1
    while i < len(seats) and j < len(seats[row]):
        if seats[i][j] == '#' or seats[i][j] == 'L':
            visible.append((i, j))
            break
        i += 1
        j += 1

    # North-West
    i = row + 1
    j = column - 1
    while i < len(seats) and j >= 0:
        if seats[i][j] == '#' or seats[i][j] == 'L':
            visible.append((i, j))
            break
        i += 1
        j -= 1

    # South-East
    i = row - 1
    j = column + 1
    while i >= 0 and j < len(seats[row]):
        if seats[i][j] == '#' or seats[i][j] == 'L':
            visible.append((i, j))
            break
        i -= 1
        j += 1

    # South-West
    i = row - 1
    j = column - 1
    while i >= 0 and j >= 0:
        if seats[i][j] == '#' or seats[i][j] == 'L':
            visible.append((i, j))
            break
        i -= 1
        j -= 1

    visible.sort()

    #print(str((row, column)) + ': ' + str(visible))
    return(visible)

def main():
    input = parseInput()

    partOne(input)
    partTwo(input)

if __name__ == "__main__":
    main()
