def have_dogs_eaten(animals, d_count, c_count, extra):
    for animal in animals:
        if animal == "D":
            if d_count <= 0 or c_count < 0:
                return False
            d_count, c_count = d_count - 1, c_count + extra
        else:
            c_count -= 1
    return True


def main():
    for i in range(int(input())):
        n, d, c, m = map(int, input().split())
        s = input()
        print(f"Case #{i + 1}: {'YES' if have_dogs_eaten(s, d, c, m) else 'NO'}")


if __name__ == '__main__':
    main()
