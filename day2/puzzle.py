def parseInput():
    input = []

    with open('input.txt') as inputFile:
        for line in inputFile:
            input.append(line)

    return input

def partOne(input):
    valid = 0

    for line in input:
        bounds, targetChar, password = line.split()

        lower, upper = bounds.split('-')
        lower = int(lower)
        upper = int(upper)

        targetChar = targetChar[0]

        charCount = 0
        for char in password:
            if char == targetChar:
                charCount += 1

        if charCount >= lower and charCount <= upper:
            valid += 1

    print("Part 1: " + str(valid))

def partTwo(input):
    import operator

    valid = 0

    for line in input:
        bounds, targetChar, password = line.split()

        lower, upper = bounds.split('-')
        lower = int(lower)
        upper = int(upper)

        targetChar = targetChar[0]

        if operator.xor(password[lower-1] == targetChar, password[upper-1] == targetChar):
            valid += 1

    print("Part 588: " + str(valid))


def main():
    input = parseInput()

    partOne(input)
    partTwo(input)

if __name__ == "__main__":
    main()
