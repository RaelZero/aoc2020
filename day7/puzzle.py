import re
import sys

def parseInput():
    input = []

    with open('input.txt') as inputFile:
        for line in inputFile:
            contentsMatch = re.findall('[0-9] \w+ \w+', line)

            contents = []
            if contentsMatch != []:
                for match in contentsMatch:
                    m = match.split()
                    item = (m[1] + ' ' + m[2], m[0])
                    contents.append(item)

            l = line.split()
            bagType = l[0] + ' ' + l[1]

            input.append([bagType, contents])

    return input

def partOne(rules, bagType):
    possibleContainers = 0

    for bagRule in rules:
        if canContain(bagRule[0], bagType, [], rules):
            #print(bagRule[0] + " can contain " + bagType)
            possibleContainers += 1

    print("Part one: " + str(possibleContainers))
    return(possibleContainers)

def canContain(sourceBag, targetBag, scanQueue, rules):
    #print(sourceBag + str(scanQueue))
    bagRule = [r for r in rules if r[0] == sourceBag][0]
    #print(bagRule)

    for b in bagRule[1]:
        scanQueue.append(b[0])

    while len(scanQueue) > 0:
        if targetBag in scanQueue:
            return True
        elif sourceBag == targetBag:
            return False
        else:
            nextBag = scanQueue.pop()
            return(canContain(nextBag, targetBag, scanQueue, rules))

def partTwo(rules, bagType):
    #totalBags = countBags(bagType, [], 0, rules)

    totalBags = 0
    bags = [bagType]

    while bags != []:
        currentBag = bags.pop()
        totalBags += 1

        bagRule = [r for r in rules if r[0] == currentBag][0]
        for (bag, count) in bagRule[1]:
            for i in range(int(count)):
                bags.append(bag)

    print("Part two: " + str(totalBags))
    return(totalBags)

def countBags(currentBag, nextBags, currentCount, rules):
    bagRule = [r for r in rules if r[0] == currentBag][0]

    for (bag, count) in bagRule[1]:
        for i in range(int(count)):
            nextBags.append(bag)

    if nextBags == []:
        return(0)
    else:
        nextBag = nextBags.pop()
        return(1 + countBags(nextBag, nextBags, currentCount, rules))

def main():
    rules = parseInput()

    sys.setrecursionlimit(20000)

    partOne(rules, 'shiny gold')
    partTwo(rules, 'shiny gold')

if __name__ == "__main__":
    main()
