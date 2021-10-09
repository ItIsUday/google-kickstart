from math import ceil


def smaller_strings_count(size, k, string):
    mid = ceil(size / 2)
    mod = 10 ** 9 + 7

    count, k_powers = 0, 1
    for i in range(mid):
        count += (ord(string[mid - i - 1]) - 97) * k_powers
        k_powers *= k

    return (count + 1) % mod if string[size // 2 - 1::-1] < string[mid:] else count % mod


def main():
    for i in range(int(input())):
        n, k = map(int, input().split())
        s = input()
        print(f"Case #{i + 1}: {smaller_strings_count(n, k, s)}")


if __name__ == "__main__":
    main()
