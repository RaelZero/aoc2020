def parseInput():
    input = []

    with open('input.txt') as inputFile:
        for line in inputFile:
            input.append(line[:-1])

    return input

def partOne(input):
    trees = traverse(input, 3, 1)

    print("Part One: " + str(trees))

def partTwo(input):
    paths = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    totalTrees = 1

    for (right, down) in paths:
        totalTrees *= traverse(input, right, down)

    print("Part Two: " + str(totalTrees))

def traverse(map, rightStep, downStep):
    mapHeight = len(map)
    mapWidth = len(map[0])

    count = 0

    row = 0
    column = 0

    while row < mapHeight:
        if (map[row][column] ==  '#'):
            count += 1
            print(str(row) + " " + str(column) + " [T]" )

        else:
            print(row,column)

        column = (column + rightStep) % mapWidth
        row += downStep

    return(count)

def main():
    input = parseInput()

    partOne(input)
    partTwo(input)

if __name__ == "__main__":
    main()
