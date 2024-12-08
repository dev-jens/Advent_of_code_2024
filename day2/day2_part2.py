def is_seq_safe(data):
        increasing = None
        for index in range(len(data) - 1): 
            
            diffrence = data[index] - data[index + 1]
            
            if(abs(diffrence) not in {1, 2, 3}):
                return False
            
            #increase
            if diffrence > 0:
                if (increasing is False):
                    return False
                increasing = True
            #decrease  
            elif diffrence < 0:                
                if (increasing is True):
                    return False
                increasing = False      
        return True

def is_seq_safe_with_damper(data):
    
    for i in range(len(data)):
        modified_data = data[:i] + data[i+1:]
        if is_seq_safe(modified_data):
            return True
    return False
    


def main():
    file_path = './day2/input.txt'
    
    with open(file_path, 'r') as file:
        unusual_data = [[int(num) for num in line.strip().split()] for line in file.readlines()]
     
        count_of_safe = 0

        for data in unusual_data:

            if (is_seq_safe(data) or is_seq_safe_with_damper(data)):
                count_of_safe += 1
                
            print(f"data {data}: {is_seq_safe(data)}")
    print(f"Count of safe values: {count_of_safe}")

    
                    
             
                

if __name__ == '__main__':
    main()