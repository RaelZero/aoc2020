def parseInput():
    input = []

    with open('input.txt') as inputFile:
        for line in inputFile:
            (opcode, value) = line.split()[0], int(line.split()[1])
            input.append((opcode, value)) # Skip the newline character

    return input

def simulate(input):
    visited = []

    for instruction in input:
        visited.append(False)

    instructionNumber = 0
    accumulator = 0

    while True:
        if instructionNumber == len(input):
            return(accumulator, 0)
        elif visited[instructionNumber] == True:
            return(accumulator, 1)
        elif input[instructionNumber][0] == 'nop':
            visited[instructionNumber] = True
            instructionNumber += 1
        elif input[instructionNumber][0] == 'acc':
            visited[instructionNumber] = True
            accumulator += input[instructionNumber][1]
            instructionNumber += 1
        elif input[instructionNumber][0] == 'jmp':
            visited[instructionNumber] = True
            instructionNumber += input[instructionNumber][1]

def partOne(input):
    result, _ = simulate(input)

    print('Part one: ' + str(result))
    return(result)

def partTwo(input):
    for i in range(len(input)):
        if input[i][0] == 'jmp':
            # substitute and run
            tempInput = input.copy()
            tempInput[i] = ('nop', input[i][1])

            result, exitCode = simulate(tempInput)
            if exitCode == 0:
                break

        elif input[i][0] == 'nop':
            # substitute and run
            tempInput = input.copy()
            tempInput[i] = ('jmp', input[i][1])

            result, exitCode = simulate(tempInput)
            if exitCode == 0:
                break

    print("Part two: " + str(result))
    return(result)

def main():
    input = parseInput()

    partOne(input)
    partTwo(input)

if __name__ == "__main__":
    main()
