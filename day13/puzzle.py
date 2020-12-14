def parseInput():
    with open('sampleinput.txt') as inputFile:
        startTime = int(inputFile.readline())
        buses = []
        schedule = []

        for b in str.split(inputFile.readline()[:-1], ','):
            if b != 'x':
                schedule.append(int(b))
                buses.append(int(b))
            else:
                schedule.append(b)

    input = (startTime, buses, schedule)

    return input

def partOne(input):
    arrivalTime = input[0]
    buses = input[1]
    nextDepartures = {bus: (arrivalTime//bus + 1) * bus for bus in buses}

    firstBus, nextDeparture = sorted(nextDepartures.items(), key = lambda i: i[1])[0]

    delta = nextDeparture - arrivalTime

    result = firstBus * delta

    print("Part one: " + str(result))
    return(result)

def partTwo(input):
    schedule = input[2]


    pass

def main():
    input = parseInput()

    partOne(input)
    partTwo(input)

if __name__ == "__main__":
    main()
