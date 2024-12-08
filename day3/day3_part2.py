import re

def main():
    file_path = './day3/input.txt'
    
    with open(file_path, 'r') as file:
        memory = file.read()
        
    matches = re.findall(r"(?:mul\((\d+),(\d+)\))|(do\(\)|don't\(\))", memory)
    print(matches)
    
    sum_of_matches = 0
    do_is_active = True
    
    for match in matches:
        if match[2] == "" and do_is_active:
            sum_of_matches += int(match[0]) * int(match[1])
        else:
            if match[2] == "do()":
                do_is_active = True
            else:
                do_is_active = False
        
        
    print(sum_of_matches)
                    
             
                

if __name__ == '__main__':
    main()