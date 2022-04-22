def shuffled_anagrams(string):
    ans, n = list(string), len(string)
    sorted_string = sorted(((char, index) for index, char in enumerate(string)))

    for i, (char, index) in enumerate(sorted_string):
        new_char = sorted_string[(i + n // 2) % n][0]
        if char != new_char:
            ans[index] = new_char
        else:
            return "IMPOSSIBLE"

    return "".join(ans)


def main():
    for i in range(int(input())):
        print(f"Case #{i + 1}: {shuffled_anagrams(input())}")


if __name__ == "__main__":
    main()
