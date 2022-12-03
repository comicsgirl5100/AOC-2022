# 2022 Advent of Code Challenges

# Day 1 Part 1
with open("input_files/day01.txt", "r") as f:
    data = f.read().split("\n")

    cals = 0
    totalCals = []
    for line in data:
        if line != "":
            cals = cals + int(line)

        else:
            totalCals.append(cals)
            cals = 0

    print(max(totalCals))
# Day 1 Part 2
    totalCals.sort(reverse = True)
    topCals = totalCals[:3]
    total = sum(topCals)
    print(total)