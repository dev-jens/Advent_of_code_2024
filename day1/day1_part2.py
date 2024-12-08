def main():
    file_path = './day1/input.txt'
    
    with open(file_path, 'r') as file:
        location_pairs = [line.strip().split("   ") for line in file.readlines()]

    left_ids = sorted(int(pair[0]) for pair in location_pairs)
    right_ids = sorted(int(pair[1]) for pair in location_pairs)

    sum_list= []
    for index, line in enumerate(left_ids):
        count_of_num = right_ids.count(left_ids[index])

        sum_list.append(left_ids[index] * int(count_of_num))

    print(sum(sum_list))


if __name__ == '__main__':
    main()