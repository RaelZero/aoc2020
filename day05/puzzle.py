def parseInput():
    input = []

    with open('input.txt') as inputFile:
        for line in inputFile:
            boardingPass = {}
            boardingPass['row'] = line[:7]
            boardingPass['column'] = line[7:-1]
            input.append(boardingPass)

    return input

def decodeRow(inputRow):
    inputRow = inputRow.replace('F',  '0')
    inputRow = inputRow.replace('B',  '1')

    decodedRow = int(inputRow, 2)

    return(decodedRow)

def decodeColumn(inputColumn):
    inputColumn = inputColumn.replace('L',  '0')
    inputColumn = inputColumn.replace('R',  '1')

    decodedColumn = int(inputColumn, 2)

    return(decodedColumn)

def partOne(input):
    ids = []

    for boardingPass in input:
        boardingPass['row'] = decodeRow(boardingPass['row'])
        boardingPass['column'] = decodeColumn(boardingPass['column'])
        boardingPass['id'] = boardingPass['row'] * 8 + boardingPass['column']
        ids.append(boardingPass['id'])

    input = sorted(input, key = lambda i: (i['row'], i['column']))

    ids = sorted(ids)

    print("Part one: " + str(ids[-1]))

    return ids

def partTwo(ids):
    ans = 0

    for i in range(1, len(ids)-1):
        if (ids[i+1] - ids[i-1]) != 2:
            ans = ids[i] + 1
            break

    print("Part two: " + str(ans))

def main():
    input = parseInput()

    passIDs = partOne(input)
    partTwo(passIDs)

if __name__ == "__main__":
    main()
