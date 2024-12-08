def main():
    file_path = './day1/input.txt'
    
    with open(file_path, 'r') as file:
        location_pairs = [line.strip().split("   ") for line in file.readlines()]

    left_ids = sorted(int(pair[0]) for pair in location_pairs)
    right_ids = sorted(int(pair[1]) for pair in location_pairs)

    distance= []

    for index, line in enumerate(left_ids):
        location_sum = left_ids[index] - right_ids[index]
        distance.append(location_sum)

    distance = sum([abs(locaction) for locaction in distance])

    print(distance)



if __name__ == '__main__':
    main()