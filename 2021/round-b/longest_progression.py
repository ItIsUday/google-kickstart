def longest(arr, size):
    diff = [arr[i] - arr[i - 1] for i in range(1, size)]


def main():
    for i in range(int(input())):
        size = int(input())
        arr = list(map(int, input().split(" ")))
        print(f"Case #{i + 1}: {longest(arr, size)}")


if __name__ == "__main__":
    main()
