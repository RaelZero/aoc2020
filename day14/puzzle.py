import re

def parseInput():
    input = {}

    maskPattern = re.compile('([0-1]|X){36}')
    with open('input.txt') as inputFile:
        currentMask = ''
        for line in inputFile:
            if re.findall(maskPattern, line):
                currentMask = line[7:-1]
            elif re.findall('mem', line):
                address, value = re.findall('[0-9]+', line)
                input[address] = (int(value), currentMask)

    return input

def partOne(input):
    # Mask all values
    finalValues = []
    for _, value in input.items():
        finalValues.append(mask(value[0], value[1]))

    # Compute result
    result = 0
    for value in finalValues:
        result += value

    print("Part one: " + str(result))
    return(result)

def mask(value, mask):
    # Convert value to little-endian binary
    binValue = bin(value)[2:]

    # Pad value to 36 bits
    lenDiff = len(mask) - len(binValue)
    binValue = '0' * lenDiff + binValue

    newValue = ''
    for i in range(len(binValue)):
        if mask[i] == '0' or mask[i] == '1':
            newValue += mask[i]
        else:
            newValue += binValue[i]

    newValue = int(newValue, 2)

    return(newValue)

def partTwo(input):
    memory = {}

    for address, value in input.items():
        targets = genAddresses(bitmask(address, value[1]), [])

        for t in targets:
            target = int(t, 2)
            memory[target] = value[0]

        #print(address, value)

    result = 0
    for address, value in memory.items():
        result += value
        #print(address, value)

    print(len(input))
    print(len(memory))

    print("Part two: " + str(result))
    return(result)

def bitmask(value, mask):
    # Convert value to little-endian binary
    binValue = bin(int(value))[2:]

    # Pad value to 36 bits
    lenDiff = len(mask) - len(binValue)
    binValue = '0' * lenDiff + binValue

    newValue = ''
    for i in range(len(binValue)):
        if mask[i] == 'X' or mask[i] == '1':
            newValue += mask[i]
        else:
            newValue += binValue[i]

    return(newValue)

def genAddresses(addressBase, generated):
    if 'X' not in addressBase:
        generated.append(addressBase)
        return(generated)

    for i in range(len(addressBase)):
        if addressBase[i] == 'X':
            addressBase = list(addressBase)

            withZero = addressBase.copy()
            withZero[i] = '0'
            withZero = "".join(withZero)

            withOne = addressBase.copy()
            withOne[i] = '1'
            withOne = "".join(withOne)

            genAddresses(withZero, generated)
            genAddresses(withOne, generated)

            return(generated)

def main():
    input = parseInput()

    partOne(input)
    partTwo(input)

if __name__ == "__main__":
    main()
