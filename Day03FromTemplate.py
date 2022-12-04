import utils

day = "03"
test1Solution = 157
test2Solution = 70

def letterToNumber(letter):
    if letter.isupper():
        return ord(letter) - ord('A') + 27
    else:
        return ord(letter) - ord('a') + 1

def getSameLetterInSack(sack):
    sackLength = int(len(sack) / 2)
    comp1 = sack[:sackLength]
    comp2 = sack[sackLength:]

    for letter in comp1:
        if letter in comp2:
            return letter

def part1(input):
    sameLetters = list(map(getSameLetterInSack, input))
    number = list(map(letterToNumber, sameLetters))
    total = sum(number)
    return total


def elfBadge(elf1, elf2, elf3):
    for letter in elf1:
        if letter in elf2:
            if letter in elf3:
                return letter
def part2(input):
    badgeTotal = 0
    for groupIndex in range(0, len(input), 3):
        elf1 = input[groupIndex - 3]
        elf2 = input[groupIndex - 2]
        elf3 = input[groupIndex - 1]
        badge = elfBadge(elf1, elf2, elf3)
        score = letterToNumber(badge)
        badgeTotal += score

    return badgeTotal



if __name__ == "__main__":
    try:
        testData = utils.readTestData(day)
        test1Answer = part1(testData)
        if test1Answer == test1Solution:
            print("Test 1 pass")
        else:
            print(f"got {test1Answer}, but expected {test1Solution}")

        test2Answer = part2(testData)
        if test2Answer == test2Solution:
            print("Test 2 pass")
        else:
            print(f"got {test2Answer}, but expected {test2Solution}")


    except FileNotFoundError:
        print("No test data")

    try:
        data = utils.readData(day)
        part1Solution = part1(data)
        print(f"part1: {part1Solution}")

        part2Solution = part2(data)
        print(f"part2: {part2Solution}")

    except FileNotFoundError:
        print("No problem input")
