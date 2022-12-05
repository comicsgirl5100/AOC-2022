import utils

day = "04"
test1Solution = 2
test2Solution = 4


def elvesStringSplit(elves):
    elf1, elf2 = elves.split(",")
    elf1SectStart, elf1SectEnd = elf1.split("-")
    elf2SectStart, elf2SectEnd = elf2.split("-")
    return ((int(elf1SectStart), int(elf1SectEnd)), (int(elf2SectStart), int(elf2SectEnd)))


def sectionsFullyOverlap(elvesPaired):
    (s1, e1), (s2, e2) = elvesPaired
    return s1 <= s2 and e1 >= e2 or s1 >= s2 and e1 <= e2


def part1(input):
    overlapCount = 0
    for elves in input:
        elvesSplit = elvesStringSplit(elves)
        overlap = sectionsFullyOverlap(elvesSplit)
        if overlap:
            overlapCount += 1

    return overlapCount


def sectionsOverlap(elvesPaired):
    (s1, e1), (s2, e2) = elvesPaired
    return \
            s1 <= s2 and s2 <= e1 or \
            s2 <= s1 and s1 <= e2


def part2(input):
    overlapCount = 0
    for elves in input:
        elvesSplit = elvesStringSplit(elves)
        overlap = sectionsOverlap(elvesSplit)
        if overlap:
            overlapCount += 1

    return overlapCount


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
