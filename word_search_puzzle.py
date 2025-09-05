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
    
    # All possible movement directions: right, down, down-right, left, up, up-left, down-left, up-right.
    directions = [
        (0, 1),   # right
        (1, 0),   # down
        (1, 1),   # down-right
        (0, -1),  # left
        (-1, 0),  # up
        (-1, -1), # up-left
        (1, -1),  # down-left
        (-1, 1)   # up-right
    ]

    # Try to place each word from the list into the grid
    for word in words:
        word_placed_successfully = False
        attempts = 0
        
        # Try up to 100 random starting points and directions to place this word
        while not word_placed_successfully and attempts < 100:
            attempts += 1
            
            # Pick a random starting cell and direction
            start_row = random.randint(0, size - 1)
            start_col = random.randint(0, size - 1)
            dx, dy = random.choice(directions)  # dx: row change, dy: col change per step
            
            # Calculate where the word would end
            end_row = start_row + dx * (len(word) - 1)
            end_col = start_col + dy * (len(word) - 1)
            
            # First, check if the end point is still inside the grid boundaries
            if end_row < 0 or end_row >= size or end_col < 0 or end_col >= size:
                continue  # It's out of bounds, try again
                
            # Now, check each cell along the path for conflicts
            valid_placement = True
            for i, letter in enumerate(word):
                current_row = start_row + dx * i
                current_col = start_col + dy * i
                current_cell = grid[current_row][current_col]
                
                # The cell must be either empty or already contain the correct letter
                if current_cell != '' and current_cell != letter:
                    valid_placement = False
                    break  # Found a conflict, no need to check further
                    
            # If the path is clear, we can write the word to the grid
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

