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
                if has_xmas(col,row,dir,lines):
                    ans += 1
    print(ans)

def has_xmas(col, row, direction, lines):
    
    if not (1 <= col < col - 1 and 1 <= row< row - 1):
        return False
    if lines[col][row] != "A":
        return False

    # Check both diagonals
    diag_1 = f"{lines[col-1][row-1]}{lines[col+1][row+1]}"
    diag_2 = f"{lines[col-1][row+1]}{lines[col+1][row-1]}"

    return diag_1 in ["MS", "SM"] and diag_2 in ["MS", "SM"]
    
        
    
    
    
    

if __name__ == "__main__":
    main()
