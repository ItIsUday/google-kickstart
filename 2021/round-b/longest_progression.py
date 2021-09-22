def longest(arr, size):
    diff = [arr[i] - arr[i - 1] for i in range(1, size)]
    chunks, max_chunk = chunkify(diff), float("-inf")
    for index, chunk in enumerate(chunks):
        i, k, d = chunk
        new_chunk_size = k
        if i + k + 2 < len(diff):
            if diff[i + k] + diff[i + k + 1] == 2 * d:
                new_chunk_size = k + 2 + chunks[index + 3][1] if diff[i + k + 2] == d else k + 2
            else:
                new_chunk_size = k + 1
        elif i + k + 1 < len(diff):
            new_chunk_size = k + 2 if diff[i + k] + diff[i + k + 1] == 2 * d else k + 1
        elif i + k < len(diff):
            new_chunk_size = k + 1
        max_chunk = max(max_chunk, new_chunk_size)

    return max_chunk + 1


def chunkify(diff):
    table = []
    chunk_index, chunk_size = 0, 1
    for i in range(1, len(diff)):
        if diff[i] == diff[i - 1]:
            chunk_size += 1
        else:
            table.append((chunk_index, chunk_size, diff[i - 1]))
            chunk_size = 1
            chunk_index = i

    table.append((chunk_index, chunk_size, diff[-1]))
    return table if table else [(0, 1, diff[0])]


def main():
    for i in range(int(input())):
        size = int(input())
        arr = list(map(int, input().split(" ")))
        ans = max(longest(arr, size), longest(arr[::-1], size))
        print(f"Case #{i + 1}: {ans}")


if __name__ == "__main__":
    main()
