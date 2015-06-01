"""
Merge function for 2048 game.
"""

def shift_left(line):
    """
    Function for moving line items left
    """
    line_shifted = list(line)
    for i in range(len(line)):
        if lin
    return line

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    line_shifted = list(line)
    
    for i in line_shifted:
        line_shifted = shift_left(line)
    
    
    
    return line
