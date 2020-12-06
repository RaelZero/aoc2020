def parseInput():
    input = []

    with open('input.txt') as inputFile:
        groupAnswers = []
        groupCount = 0
        for line in inputFile:
            if line == '\n':
                input.append([groupCount, groupAnswers])
                groupCount = 0
                groupAnswers = []
            else:
                groupCount += 1
                for c in line:
                    if c != '\n':
                        groupAnswers.append(c)

    return input

def partOne(input):
    yesCount = 0

    for group in input:
        yesCount += len(set(group[1]))

    print("Part One: " + str(yesCount))

    return yesCount


def partTwo(input):
    allYesCount = 0

    for group in input:
        groupYesCount = 0

        for ans in set(group[1]):
            if group[1].count(ans) == group[0]:
                groupYesCount += 1

        allYesCount += groupYesCount

    print("Part two: " + str(allYesCount))

    return(allYesCount)

def main():
    input = parseInput()

    partOne(input)
    partTwo(input)

if __name__ == "__main__":
    main()
