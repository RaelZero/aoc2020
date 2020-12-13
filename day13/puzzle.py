def parseInput():
    with open('input.txt') as inputFile:
        startTime = int(inputFile.readline())
        buses = []
        for b in str.split(inputFile.readline()[:-1], ','):
            if b != 'x':
                buses.append(b)

    input = (startTime, buses)

    return input

def partOne(input):
    pass

def partTwo(input):
    pass

def main():
    input = parseInput()

    partOne(input)
    partTwo(input)

if __name__ == "__main__":
    main()
