def substring(string, size):
    max_ = 1
    yield max_
    for i in range(1, size):
        if string[i - 1] < string[i]:
            max_ += 1
        else:
            max_ = 1
        yield max_


def main():
    for i in range(int(input())):
        size = int(input())
        string = input()
        print(f"Case #{i + 1}: {' '.join(map(str, substring(string, size)))}")


if __name__ == "__main__":
    main()
