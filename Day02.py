# 2022 Advent of Code Challenges

# Day 2 Part 1
with open("input_files/day02.txt", "r") as f:
    data = f.read().split("\n")

    points = 0
    for hand in data:
        if hand == "A X":
            points = points + 4
        elif hand == "B Y":
            points = points + 5
        elif hand == "C Z":
            points = points + 6
        elif hand == "A Z":
            points = points + 3
        elif hand == "B X":
            points = points + 1
        elif hand == "C Y":
            points = points + 2
        elif hand == "A Y":
            points = points + 8
        elif hand == "B Z":
            points = points + 9
        elif hand == "C X":
            points = points + 7
        else:
            print("nothing")
    print(points)

    # Day 2 Part 2
    correctPoints = 0
    for hand in data:
        if hand == "A X":
            correctPoints = correctPoints + 3
        elif hand == "B Y":
            correctPoints = correctPoints + 5
        elif hand == "C Z":
            correctPoints = correctPoints + 7
        elif hand == "A Z":
            correctPoints = correctPoints + 8
        elif hand == "B X":
            correctPoints = correctPoints + 1
        elif hand == "C Y":
            correctPoints = correctPoints + 6
        elif hand == "A Y":
            correctPoints = correctPoints + 4
        elif hand == "B Z":
            correctPoints = correctPoints + 9
        elif hand == "C X":
            correctPoints = correctPoints + 2
        else:
            print("nothing")

    print(correctPoints)
