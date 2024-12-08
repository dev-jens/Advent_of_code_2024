import re

def main():
    file_path = './day4/input.txt'
    
    with open(file_path, 'r') as file:
        lines = file.read().strip().split("\n")
   
    for line in lines:
        print(line)
                    
             
                

if __name__ == '__main__':
    main()