import utils

day = "00"
testSolution = 0


def part1(input):
    return 0


def part2(input):
    return 0


if __name__ == "__main__":
    try:
        testData = utils.readTestData(day)
        testAnswer = part1(testData)
        if testAnswer == testSolution:
            print("Test pass")
        else:
            print(f"got {testAnswer}, but expected {testSolution}")

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
