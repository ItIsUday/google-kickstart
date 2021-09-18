def goodness(s, n, k):
    g = sum(1 for i in range(n // 2) if s[i] != s[n - i - 1])
    return abs(g - k)


if __name__ == "__main__":
    for i in range(int(input())):
        n, k = map(int, input().split(" "))
        s = input()
        print(f"Case #{i + 1}: {goodness(s, n, k)}")
