def parseInput():
    input = []

    with open('input.txt') as inputFile:
        for line in inputFile:
            input.append(line[:-1]) # Skip the newline character

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
