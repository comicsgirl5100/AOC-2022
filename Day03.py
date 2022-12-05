# 2022 Advent of Code Challenges

# Day 3 Part 1
with open("input_files/day03.txt", "r") as f:
    sackList = f.read().split("\n")
    print(sackList)

sackTest = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw"]

# Day 3 Part 1
def getSameLetterInSack(sack):
    sackLength = int(len(sack) / 2)
    comp1 = sack[:sackLength]
    comp2 = sack[sackLength:]

    for letter in comp1:
        if letter in comp2:
            return letter

sameLetter = list(map(getSameLetterInSack, sackList))

def letterToNumber(letter):
    if letter.isupper():
        return ord(letter) - ord('A') + 27
    else:
        return ord(letter) - ord('a') + 1

number = list(map(letterToNumber, sameLetter))
total = sum(number)
print(total)

#Day 03 Part 2

def elfBadge(elf1, elf2, elf3):
    for letter in elf1:
        if letter in elf2:
            if letter in elf3:
                return letter


badgeTotal = 0

for groupIndex in range(0, len(sackList), 3):
    elf1 = sackList[groupIndex - 3]
    elf2 = sackList[groupIndex - 2]
    elf3 = sackList[groupIndex - 1]
    badge = elfBadge(elf1, elf2, elf3)
    score = letterToNumber(badge)
    badgeTotal += score

print(badgeTotal)




