def challenge_nine(num):
    digit, index = str((9 - (sum(map(int, num)) % 9)) % 9), len(num)

    for i, char in enumerate(num):
        if char > digit:
            index = i
            break
    index = index + 1 if index == 0 and digit == "0" else index

    return "".join((num[:index], digit, num[index:]))


def main():
    for i in range(int(input())):
        print(f"Case #{i + 1}: {challenge_nine(input())}")


if __name__ == "__main__":
    main()
