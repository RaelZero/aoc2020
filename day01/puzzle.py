input = []

with open('input.txt') as inputFile:
    for line in inputFile:
        input.append(int(line))

for number1 in input:
    for number2 in input:
        if (number1 +  number2 == 2020):
            res1 = number1 * number2
        for number3 in input:
            if (number1 + number2 + number3 == 2020):
                res2 = number1 * number2 * number3
                break

print("First part: " + str(res1))
print("Second part: " + str(res2))


