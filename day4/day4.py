import os.path

INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")

directions = [
    (-1, -1),  # diagonal left above
    (-1, 0),  # above current letter
    (-1, 1),  # diagonal right above
    (0, -1),  # go left
    (0, 1),  # go right
    (1, -1),  # left diagonal under
    (1, 0),  # under
    (1, 1),  # right diagonal under
]


def main():

    with open(INPUT_PATH, "r") as file:
        lines = file.read().strip().split("\n")

    ans = 0
    col_len = len(lines)
    row_len = len(lines[0])  # every line is same lenght
    
    for col in range(col_len):
        for row in range(row_len):
            for dir in directions:
                if check_xmas(col,row,dir,lines):
                    ans += 1
    print(ans)

def check_xmas(col, row, direction, lines):
    
    word_to_check = "XMAS"
    dir_col = direction[0]
    dir_row = direction[1]
    col_len = len(lines)
    row_len = len(lines[0])
    
    for index, letter in enumerate(word_to_check):
        curr_col = col + index * dir_col
        curr_row = row + index * dir_row
        
        if  not ( 0 <= curr_col < col_len  and 0 <= curr_row <  row_len):    
            return False
        
        if lines[curr_col][curr_row] is not letter:
           return False
             
    return True
    
        
    
    
    
    

if __name__ == "__main__":
    main()
