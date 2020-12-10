def parseInput():
    input = []

    with open('input.txt') as inputFile:
        for line in inputFile:
            input.append(int(line)) # Skip the newline character

    return input

def partOne(input):
    input.sort()

    deltas = []

    for i in range(len(input)):
        deltas.append(0)
        if i == 0:
            deltas[i] = input[i]
        else:
            deltas[i] = input[i] - input[i-1]
            if i == len(input) - 1:
                deltas.append(3)

    result = deltas.count(1) * deltas.count(3)

    print('Part one: ' + str(result))
    return(result)

def partTwo(input):
    # Add min and max joltage to matrix, then sort array
    input.sort()
    input.append(input[-1] + 3)
    input.append(0)
    input.sort()
    print(input)

    arrangements = []

    # Initialise the first three steps
    # The first node (the zero) has no possible paths
    arrangements.append(1)

    # The second node (the first in the sequence) has one path: from the zero
    arrangements.append(1)

    # The third node (the second in the sequence) can have up to two paths: from the zero or from the first in the sequence
    # from zero
    if input[2] - input[0] <= 3:
        arrangements.append(2)
    # from the first
    elif input[2] - input[1] <= 3:
        arrangements.append(1)

    # For all following paths
    for i in range(3, len(input)):
        arr = 0
        if input[i] - input[i-1] <= 3:
            arr += arrangements[i-1]
        if input[i] - input[i-2] <= 3:
            arr += arrangements[i-2]
        if input[i] - input[i-3] <= 3:
            arr += arrangements[i-3]
        arrangements.append(arr)

    print(arrangements)

    print("Part two: " + str(arrangements[-1]))
    return(arrangements[-1])


def possibleBranches(startPoint, input):
    c = 0

    for i in range(startPoint + 1, min(startPoint + 4, len(input))):
        if startPoint + 1 >= len(input):
            return(1)
        if input[i] - input[startPoint] <= 3:
            c += 1

    return(c)

def main():
    input = parseInput()

    #partOne(input)
    partTwo(input)

if __name__ == "__main__":
    main()
