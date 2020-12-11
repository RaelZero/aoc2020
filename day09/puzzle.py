def parseInput():
    input = []

    with open('input.txt') as inputFile:
        for line in inputFile:
            input.append(int(line))

    return input

def partOne(input):
    preamble = 25

    for i in range(preamble, len(input)):
        if not validate(i, preamble, input):
            print("Part one: " + str(input[i]))
            return(input[i])

def validate(valueIndex, prefixLength, input):
    for i in range(1, prefixLength + 1):
        for j in range(1, prefixLength + 1):
            if i != j:
                if (input[valueIndex-i] + input[valueIndex-j]) == input[valueIndex]:
                    return(True)
    return(False)

def partTwo(input, prevResult):
    upper, lower = findBoundaries(input, prevResult)

    weaknessSet = []
    for i in range(upper, lower):
        weaknessSet.append(input[i])

    weaknessSet.sort()

    result = weaknessSet[0] + weaknessSet[-1]

    print("Part two: " + str(result))
    return(result)


def findBoundaries(input, target):
    for i in range(len(input)):
        acc = 0

        for j in range(i, len(input)):
            acc += input[j]

            if acc > target:
                break
            if acc == target:
                return(i,j)

def main():
    input = parseInput()

    p1res = partOne(input)
    partTwo(input, p1res)

if __name__ == "__main__":
    main()
