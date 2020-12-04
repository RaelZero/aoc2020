import re

def parseInput():
    input = []

    with open('input.txt') as inputFile:
        currentPassport = ""
        for line in inputFile:
            if line == "\n":
                input.append(currentPassport[:-1])
                currentPassport = ""
            else:
                currentPassport = currentPassport + line[:-1] + ' '

    return input

def extractFields(passport, fieldPattern):
    fields = fieldPattern.findall(passport)

    for f in range(len(fields)):
        fields[f] = fields[f][:-1]

    fields.sort()

    return(fields)


def partOne(input):
    fieldPattern = re.compile('[a-z]{3}\:')
    allFields = ['byr', 'cid', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']
    missingCid = ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']

    valid = []

    for p in input:
        pFields = extractFields(p, fieldPattern)

        if pFields == allFields or pFields == missingCid:
            valid.append(p)

    print("Part one: " + str(len(valid)))

    return(valid)

def partTwo(input):
    for i in range(len(input)):
        input[i] = re.split('\s', input[i])
        input[i].sort()
        for f in range(len(input[i])):
            input[i][f] = re.split('\:', input[i][f])
        input[i] = {f[0]: f[1] for f in input[i]}

    valid = 0
    for passport in input:
        # drop cid, if present
        if 'cid' in passport:
            del passport['cid']

        # check byr: should be btw 1920 and 2002
        if not (re.match('[0-9]{4}', passport['byr']) and int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002):
            print("bad byr: " + passport['byr'])
            continue

        # check iyr: should be btw 2010 and 2020
        if not (re.match('[0-9]{4}', passport['iyr']) and int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020):
            print("bad iyr: " + passport['iyr'])
            continue

        # check eyr: should be btw 2020 and 2030
        if not (re.match('[0-9]{4}', passport['eyr']) and int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030):
            print("bad eyr: " + passport['eyr'])
            continue

        # check hgt
        if not re.match('([0-9]{3}(cm))|([0-9]{2}(in))', passport['hgt']):
            print("bad hgt: " + passport['hgt'])
            continue
        else:
            if passport['hgt'][-2:] == 'cm':
                if not (int(passport['hgt'][:-2]) >= 150 and int(passport['hgt'][:-2]) <= 193):
                    print("bad hgt: " + passport['hgt'])
                    continue
            elif passport['hgt'][-2] == 'in':
                if not (int(passport['hgt'][:-2]) >= 59 and int(passport['hgt'][:-2]) <= 76):
                    print("bad hgt: " + passport['hgt'])
                    continue

        # check hcl: should be hex-color
        if not re.match('\#[0-9a-f]{6}', passport['hcl']):
            print("bad hcl: " + passport['hcl'])
            continue

        # check ecl: should be one of a specific list
        eclValidation = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if not passport['ecl'] in eclValidation:
            print("bad ecl: " + passport['ecl'])
            continue

        # check pid: should be string of 9 numbers
        if not (len(passport['pid']) == 9 and re.match('[0-9]{9}', passport['pid'])):
            print("bad pid: " + passport['pid'])
            continue

        valid += 1
        print('Valid: '  + str(passport))

    print("Part two: " + str(valid))

def main():
    input = parseInput()

    firstCheck = partOne(input)
    partTwo(firstCheck)

if __name__ == "__main__":
    main()
