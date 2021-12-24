from math import ceil


def initial_gold_count(total_gold):
    count = 0
    day1_gold_count, curr_total_gold, day = 1, 1, 1
    while curr_total_gold < total_gold:
        day += 1
        curr_total_gold += day
    days = day
    while day1_gold_count <= total_gold:
        if curr_total_gold == total_gold:
            count += 1
            days -= 1
            curr_total_gold -= day1_gold_count
            day1_gold_count += 1
        if days <= 0:
            break
        steps = ceil((total_gold - curr_total_gold) / days)
        day1_gold_count += steps
        curr_total_gold += steps * days
        if curr_total_gold > total_gold:
            days -= 1
            curr_total_gold -= day1_gold_count
            day1_gold_count += 1
    return count


def main():
    for i in range(int(input())):
        total_gold = int(input())
        print(f"Case #{i + 1}: {initial_gold_count(total_gold)}")


if __name__ == "__main__":
    main()
