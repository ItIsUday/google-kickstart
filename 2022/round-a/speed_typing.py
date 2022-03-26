def letters_to_remove(string1, string2):
    len1, len2 = len(string1), len(string2)
    i, j, count = 0, 0, 0
    while i < len1 and j < len2:
        if string1[i] == string2[j]:
            i, j = i + 1, j + 1
        else:
            j += 1
            count += 1

    return count + len2 - j if i == len1 else "IMPOSSIBLE"


def main():
    for i in range(int(input())):
        print(f"Case #{i + 1}: {letters_to_remove(input(), input())}")


if __name__ == "__main__":
    main()
