def parseInput():
    input = []

    with open('input.txt') as inputFile:
        for line in inputFile:
            input.append((line[0], int(line[1:-1]))) # Append tuple in format (command, value)

    print(input)
    return input

def partOne(input):
    vPos = 0
    hPos = 0
    heading = 90

    for (command, value) in input:
        if command == 'N':
            vPos += value
        elif command == 'E':
            hPos += value
        elif command == 'S':
            vPos -= value
        elif command == 'W':
            hPos -= value
        elif command == 'L':
            heading = (heading - value) % 360
        elif command == 'R':
            heading = (heading + value) % 360
        elif command == 'F':
            if heading == 0:
                vPos += value
            elif heading == 90:
                hPos += value
            elif heading == 180:
                vPos -= value
            elif heading == 270:
                hPos -= value

        #print(str(vPos) + 'N ' + str(hPos) + 'E')

    result = abs(vPos) + abs(hPos)
    print('Part one: ' + str(result))
    return(result)

def partTwo(input):
    shipVPos = 0
    shipHPos = 0

    wpVPos = 1
    wpHPos = 10

    heading = 90

    for (command, value) in input:
        if command == 'N':
            wpVPos += value
        elif command == 'E':
            wpHPos += value
        elif command == 'S':
            wpVPos -= value
        elif command == 'W':
            wpHPos -= value
        elif command == 'L' or command == 'R':
            oldH = wpHPos
            oldV = wpVPos
            if (value == 90 and command == 'L') or \
                (value == 270 and command == 'R'):
                #CCW
                wpVPos = oldH
                wpHPos = -oldV
            elif value == 180:
                wpVPos = -oldV
                wpHPos = -oldH
            elif (value == 270 and command == 'L') or \
                (value == 90 and command == 'R'):
                #CW
                wpHPos = oldV
                wpVPos = -oldH

        elif command == 'F':
            shipVPos += wpVPos * value
            shipHPos += wpHPos * value

        print((command, value))
        print(str(shipVPos) + 'N ' + str(shipHPos) + 'E')
        print(str(wpVPos) + 'N ' + str(wpHPos) + 'E\n')

    result = abs(shipVPos) + abs(shipHPos)
    print('Part two: ' + str(result))
    return(result)

def main():
    input = parseInput()

    partOne(input)
    partTwo(input)

if __name__ == "__main__":
    main()
