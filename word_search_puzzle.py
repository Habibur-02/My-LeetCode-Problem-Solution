import random

def create_crossword(words):
    """
    Creates a 10x10 word search puzzle, weaving the given words into the grid.
    
    Words are placed in random directions (including diagonals). Any remaining
    spaces are filled with random letters to complete the puzzle.
    
    Args:
        words (list): A list of strings (words) to hide in the grid.
        
    Returns:
        list: A 10x10 grid (list of lists) representing the puzzle.
    """
    size = 10
    # Start with an empty 10x10 grid
    grid = [['' for _ in range(size)] for _ in range(size)]
    
    directions = [
        (0, 1),   
        (1, 0),   
        (1, 1),   
        (0, -1),  
        (-1, 0),  
        (-1, -1), 
        (1, -1),  
        (-1, 1)  
    ]

    for word in words:
        word_placed_successfully = False
        attempts = 0
        
        while not word_placed_successfully and attempts < 100:
            attempts += 1
            
            start_row = random.randint(0, size - 1)
            start_col = random.randint(0, size - 1)
            dx, dy = random.choice(directions)  
            
            end_row = start_row + dx * (len(word) - 1)
            end_col = start_col + dy * (len(word) - 1)
            
            if end_row < 0 or end_row >= size or end_col < 0 or end_col >= size:
                continue  
                
            valid_placement = True
            for i, letter in enumerate(word):
                current_row = start_row + dx * i
                current_col = start_col + dy * i
                current_cell = grid[current_row][current_col]
                
                if current_cell != '' and current_cell != letter:
                    valid_placement = False
                    break  
                    
            if valid_placement:
                for i, letter in enumerate(word):
                    current_row = start_row + dx * i
                    current_col = start_col + dy * i
                    grid[current_row][current_col] = letter
                word_placed_successfully = True
                

    for row in range(size):
        for col in range(size):
            if grid[row][col] == '':
                grid[row][col] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
                
    return grid

