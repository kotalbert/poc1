"""
Merge function for 2048 game.
"""

def shift_left(line):
    """
    Function for moving line items left
    """
    line_len = len(line)
    shifted_line = [0] * line_len
    # iterator - indexing the shifted_line elements
    iterator = 0
    
    # Assign non-zero element of input list to 
    # sequential elements of new shifted list
    for item in line:
        if item != 0:
            shifted_line[iterator] = item
            iterator += 1
            
    return shifted_line
    

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    
    line_len = len(line)
    
    # iterator - indexing the items of line, in order to merge elements
    iterator = 0
    
    # Line shifted left for the first time
    shftl = shift_left(line)
    
    while iterator < line_len - 1:
        if shftl[iterator] == shftl[iterator+1]:
            shftl[iterator] *= 2
            shftl[iterator+1] = 0
            shftl = shift_left(shftl)
        iterator += 1

    return shftl
