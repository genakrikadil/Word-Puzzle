#############################################
# this code finds words in the word puzzle.
# rows - the puzzle itself
# word_to_find- these words need to be found
##############################################

def solve():
    rows = [
        "NEPMVPIQUUTD",  
        "TRABAJADORAE",  
        "ASOIDUTSEDGS",  
        "LAKUXMALEARO",  
        "EMDICZPPOCAR",
        "NTPAOXOJZICD",
        "TIUMNRUFFTIE",
        "OQKITEITESON",
        "SMXIETDGPISA",
        "AOSLURMRYTOD",
        "PTLAEUUJORHO",
        "ASOCIABLEAET"
    ]

    word_to_find = [
        "artistic", "atrevid", "buen", "deportist", "desordenad", 
        "estudios", "gracios", "impaciente", "inteligente", "ordenad", 
        "paciente", "perezoso", "reservado", "serio", "simpatico", 
        "sociable", "talentos", "trabajador"
    ]

    # Find the length of the shortest word
    shortest_length = min(len(word) for word in word_to_find)
    #initiate array where we will store all words generated from the puzzle
    all_words = []  # List to store all generated words
    
    # Horizontal words (Row-wise)
    for row_idx, row in enumerate(rows):
        for i in range(len(row)):  # Column-wise within the row
            word = row[i]
            if len(word) >= shortest_length:  # Only add word if it meets length requirement
                all_words.append((word, row_idx, i, "Horizontal"))  # Store word with its position and direction
            
            # Going across horizontally
            for k in range(i + 1, len(row)):  # Column-wise
                word += row[k]
                if len(word) >= shortest_length:  # Only add word if it meets length requirement
                    all_words.append((word, row_idx, i, "Horizontal"))  # Store word with its position and direction
                    all_words.append((word[::-1], row_idx, i, "Horizontal Reverse"))  # Reverse word generation here

    # Vertical words (Column-wise)
    for i in range(len(rows[0])):  # Column-wise
        for j in range(len(rows)):  # Row-wise
            word = rows[j][i]
            if len(word) >= shortest_length:  # Only add word if it meets length requirement
                all_words.append((word, j, i, "Vertical"))  # Store word with its position and direction
            
            # Going down vertically
            for k in range(j + 1, len(rows)):  # Row-wise
                word += rows[k][i]
                if len(word) >= shortest_length:  # Only add word if it meets length requirement
                    all_words.append((word, j, i, "Vertical"))  # Store word with its position and direction
                    all_words.append((word[::-1], j, i, "Vertical Reverse"))  # Reverse word generation here

    # Diagonal words (Left Up to Right Down)
    for i in range(len(rows[0])):  # Column-wise
        for j in range(len(rows)):  # Row-wise
            word = rows[j][i]
            if len(word) >= shortest_length:  # Only add word if it meets length requirement
                all_words.append((word, j, i, "Diagonal (Left-Up to Right-Down)"))  # Store word with its position and direction
            curr_column = i + 1
            curr_row = j + 1

            while curr_row < len(rows) and curr_column < len(rows[0]):
                word += rows[curr_row][curr_column]
                if len(word) >= shortest_length:  # Only add word if it meets length requirement
                    all_words.append((word, j, i, "Diagonal (Left-Up to Right-Down)"))  # Store word with its position and direction
                    all_words.append((word[::-1], j, i, "Diagonal (Left-Up to Right-Down)"))  # Reverse word generation here

                curr_column += 1
                curr_row += 1

    # Diagonal words (Left Down to Right Up)
    for i in range(len(rows[0])):  # Column-wise
        for j in range(len(rows)):  # Row-wise
            word = rows[j][i]
            if len(word) >= shortest_length:  # Only add word if it meets length requirement
                all_words.append((word, j, i, "Diagonal (Left-Down to Right-Up)"))  # Store word with its position and direction
            curr_column = i + 1
            curr_row = j - 1

            while curr_row >= 0 and curr_column < len(rows[0]):
                word += rows[curr_row][curr_column]
                if len(word) >= shortest_length:  # Only add word if it meets length requirement
                    all_words.append((word, j, i, "Diagonal (Left-Down to Right-Up)"))  # Store word with its position and direction
                    all_words.append((word[::-1], j, i, "Diagonal (Left-Down to Right-Up)"))  # Reverse word generation here

                curr_column += 1
                curr_row -= 1

    # Print Word Puzzle
    print ("\n\nWord Puzzle\n")

    # Print Column Headers (numbered 1 to N)
    print("  ", end="")  # For row numbers indentation
    for i in range(len(rows[0])):  # Loop through columns
        print(f" {i + 1:3d} ", end="")  # Print column numbers 3-digit width
    print("\n")  

    # print the matrix
    for i in range(len(rows[0])):  # Column-wise
        print(f"{i + 1:2d} ", end="")  # Print row number with 2-digit width
        for j in range(len(rows)):  # Row-wise
            print (" ",rows[i][j]," ",end="")
        print ("\n")    

    print("\n\nSolution:\nHere are the words found in the puzzle, Position is (ROW:COL):\n")
    for word, start_row, start_col, direction in all_words:
        if word.lower() in word_to_find:
            print(f"Word: {word} | Direction: {direction} | Start Position: ({start_row+1}, {start_col+1})")
    print("\n\n")
    
# Call solve function
solve()
