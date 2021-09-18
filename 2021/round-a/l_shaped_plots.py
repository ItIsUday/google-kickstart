from dataclasses import dataclass


@dataclass
class Data:
    top: int = 0
    left: int = 0
    bottom: int = 0
    right: int = 0


def l_shapes(grid, r, c):
    ans = 0
    dp = calc_segments(grid, r, c)
    for i in range(r):
        for j in range(c):
            data = dp[i][j]
            ans += (
                    count(data.top, data.left)
                    + count(data.top, data.right)
                    + count(data.bottom, data.left)
                    + count(data.bottom, data.right)
            )

    return ans


def count(x, y):
    return max(min(x // 2, y) + min(y // 2, x) - 2, 0)


def calc_segments(grid, r, c):
    dp = [[Data() for i in range(c)] for j in range(r)]

    for i in range(r):
        for j in range(c):
            if grid[i][j]:
                dp[i][j].top = get_value_at(dp, i - 1, j).top + 1
                dp[i][j].left = get_value_at(dp, i, j - 1).left + 1

    for i in range(r - 1, -1, -1):
        for j in range(c - 1, -1, -1):
            if grid[i][j]:
                dp[i][j].bottom = get_value_at(dp, i + 1, j).bottom + 1
                dp[i][j].right = get_value_at(dp, i, j + 1).right + 1
    return dp


def get_value_at(dp, i, j):
    return dp[i][j] if 0 <= i < len(dp) and 0 <= j < len(dp[0]) else Data()


def main():
    for i in range(int(input())):
        r, c = map(int, input().split(" "))
        grid = [list(map(int, input().split(" "))) for _ in range(r)]
        print(f"Case #{i + 1}: {l_shapes(grid, r, c)}")


if __name__ == "__main__":
    main()
