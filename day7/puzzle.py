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

    #Recursive awesomeness Python can't handle
    for bagRule in rules:
        if canContain(bagRule[0], bagType, [], rules):
            #print(bagRule[0] + " can contain " + bagType)
            possibleContainers += 1

    '''
    class containerFound(Exception): pass

    for bagRule in rules:
        try:
            for (color, count) in bagRule[1]:
                bags = [color]

                while bags:
                    currentBag = bags.pop()

                    nextBagRule = [r for r in rules if r[0] == currentBag][0]
                    #print(str(nextBagRule))
                    for (bag, count) in nextBagRule[1]:
                        #print(nextBagRule[1])
                        if bagType == bag:
                            possibleContainers += 1
                            bags = []
                            raise containerFound()
                        else:
                            bags.append(bag)
                    #print(bags)
        except containerFound:
            continue
    '''

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
    # Recursive awesomeness - Python can't handle it
    #totalBags = countBags(bagType, [], 0, rules)

    totalBags = 0
    bags = [bagType]

    while bags:
        currentBag = bags.pop()
        totalBags += 1

        bagRule = [r for r in rules if r[0] == currentBag][0]
        for (bag, count) in bagRule[1]:
            for i in range(int(count)):
                bags.append(bag)

    # Remove the bag itself from the count !!horrible hax
    totalBags -= 1

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
