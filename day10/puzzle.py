def parseInput():
    input = []

    with open('input.txt') as inputFile:
        for line in inputFile:
            input.append(int(line))

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

# Commenting this function extensively to explain the solution, in case someone is curious. This is quite a good exercise about a technique called "Dynamic Programming" — look it up!
def partTwo(input):
    # We start with some setup...
    # Sort the input array so that we can test Part 2 even if we didn't run Part 1
    input.sort()

    # We append the device voltage (max adapter + 3) and the zero
    input.append(input[-1] + 3)
    input.append(0)

    # Sort again to make everything orderly
    input.sort()

    # In Dynamic Programming, we solve complex problems by breaking them down into the smallest possible problem with the same structure, and solving this simple problem. Once we have this answer, we keep adding one more element to it, and solve the problem again, until we are able to solve our original problem.
    # If it sounds a bit like recursion, it's because it is like recursion!
    # Except, in this case, we "annotate" (or, as we say in this context, "memoise") the results that we had on the simpler problems, and reuse them later.

    # In this case, we need to find the number of possible arrangements for a long chain of adapters, starting from the power plug and ending with our device.
    # To solve this problem, we will build our solution gradually by finding the arrangements that go from the plug to one of the adapters in the middle, and then adding adapters to the end of the line one by one.

    # To "memoise" our results, we will use an array.
    # This array will be as long as the input array. Each item arrangements[i] will contain the number of all possible arrangements from the plug (the 0) to the i-th adapter (and, eventually, our device).
    arrangements = []

    # Since the maximum step in voltage is 3 and each step increases the voltage by at least 1, we will need to manually initialise the first three steps.
    # These are our simplest possible problemz — they're somewhat like base cases in recursion.

    # To go from zero to zero there's only one possible arrangement: no adapters at all.
    arrangements.append(1)

    # To go from zero to the first adapter, again, only one possible arrangement: zero, and then first adapter.
    arrangements.append(1)

    # To go from zero to the second adapter, we can have up to two paths: from the first adapter (0 -> 1 -> 2) or, if the voltage difference is small enough, directly from the zero, skipping the first (0 -> 2)
    # If we can connect the second adapter to the zero directly, then we could for sure also connect to the first, so we'd have two paths
    if input[2] - input[0] <= 3:
        arrangements.append(2)
    # If the difference is too high, then we will need to connect to the first adapter, so there'll only be one possible path (0 -> first -> second)
    else:
        arrangements.append(1)

    # And with our base cases defined, here's where the magic happens.
    # For each adapter after the second, we can deduce how many configurations are possible by looking at the possible configurations for the ones that connect to it.
    # We start from the third adapter, because we manually wrote the first two adapters (and the zero)
    for i in range(3, len(input)):
        # Again, some setup: we add a zero to the arrangements array, so that we can assign values to arrangements[i]
        arrangements.append(0)

        # Depending on the actual values, we can attach the i-th adapter to up to three adapters...
        # At the very least, we can attach the i-th adapter to the one immediately before it. Therefore, all paths that lead to i-1 also lead to i.
        arrangements[i] = arrangements[i-1]

        # If we are lucky, we can also attach the i-th adapter to the one that was two positions before. If this happens, all the arrangements that got us from zero to i-2 are also good for i.
        if input[i] - input[i-2] <= 3:
            arrangements[i] += arrangements[i-2]

        # And if we are extremely lucky, we can even attach i to the adapter that was three positions before!
        if input[i] - input[i-3] <= 3:
            arrangements[i] += arrangements[i-3]

    # And once we're out of the loop, the deed is done!
    # The last element of the arrangements array will contain all possible arrangements to get to our device.
    print("Part two: " + str(arrangements[-1]))
    return(arrangements[-1])

def main():
    input = parseInput()

    partOne(input)
    partTwo(input)

if __name__ == "__main__":
    main()
