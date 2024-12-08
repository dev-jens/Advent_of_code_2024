import re

def main():
    file_path = './day3/input.txt'
    
    with open(file_path, 'r') as file:
        memory = file.read()
    matches = re.findall(r"mul\((\d+),(\d+)\)", memory)
    sum_of_matches = 0
    for match in matches:
        sum_of_matches += int(match[0]) * int(match[1])
    
    print(sum_of_matches)
                    
             
                

if __name__ == '__main__':
    main()