# File that holds the Sudoku class
import pygame


class Sudoku:
    def __init__(self):
        pygame.init()                                           # Initialize pygame

        pygame.display.set_caption("Sudoku")                    # Give the window a title
        self.window = pygame.display.set_mode((900, 900))       # Create a window

        self.font = pygame.font.Font("freesansbold.ttf", 64)    # Set the font to draw the numbers

        self.menu = True                                        # Start off by showing the menu and not the game

        self.highlighted_square = pygame.Surface((75, 75))      # Create a surface that will become the highlighted sqr
        self.highlighted_square.set_alpha(100)                  # Set the opacity of the square
        self.highlighted_square.fill((255, 223, 0))             # Set the color of the square
        self.x_start = -100                                     # Initialize highlighted square to out of frame
        self.y_start = -100                                     #
        self.selected_col = -1                                  # Initialize the col and row number of the highlighted
        self.selected_row = -1                                  # square to outside of the frame

        self.numbers = [[7,8,0,4,0,0,1,2,0],                    # Sample game for testing
                        [6,0,0,0,7,5,0,0,9],
                        [0,0,0,6,0,1,0,7,8],
                        [0,0,7,0,4,0,2,6,0],
                        [0,0,1,0,5,0,9,3,0],
                        [9,0,4,0,6,0,0,0,5],
                        [0,7,0,3,0,0,0,1,2],
                        [1,2,0,0,0,7,4,0,0],
                        [0,4,9,2,0,6,0,0,7]]
        self.new_numbers = [[7,8,0,4,0,0,1,2,0],
                            [6,0,0,0,7,5,0,0,9],
                            [0,0,0,6,0,1,0,7,8],
                            [0,0,7,0,4,0,2,6,0],
                            [0,0,1,0,5,0,9,3,0],
                            [9,0,4,0,6,0,0,0,5],
                            [0,7,0,3,0,0,0,1,2],
                            [1,2,0,0,0,7,4,0,0],
                            [0,4,9,2,0,6,0,0,7]]

    def set_background(self):                                   # Method that sets the background of the game
        if self.menu:                                           # If the user is still at the menu
            self.display_menu()                                 # Display the menu
        else:                                                   # Otherwise
            self.window.fill((102, 178, 255))                   # Uses RGB to set the background color to light blue
            self.draw_board()                                   # Call the method to draw the board
            self.draw_numbers()                                 # Call the method to put the numbers on the board

    def display_menu(self):
        self.window.fill((102, 178, 255))                       # Uses RGB to set the background color to light blue
        title = self.font.render("SUDOKU", True,                # Display a title to the screen
                                 (255, 255, 255))               #
        self.window.blit(title, (320, 70))                      #

        pygame.draw.rect(self.window,                           # Draw the button
                         (255, 255, 255), [360, 200, 200, 50])  #
        pygame.draw.rect(self.window,                           # Give the button an outline
                         (0, 0, 0), [360, 200, 200, 50], 3)     #
        button_font = pygame.font.Font("freesansbold.ttf", 32)  # Set the font
        play_game = button_font.render("Play Game",             # Put the text on the button
                                       True, (0, 0, 0))         #
        self.window.blit(play_game, (375, 210))                 #

    def draw_board(self):                                       # A method that draws the board
        title = self.font.render("SUDOKU", True,                # Display a title to the screen
                                 (255, 255, 255))               #
        self.window.blit(title, (320, 25))                      #

        counter = 0                                             # Initialize a counter to 0
        x_location = 100.0                                      # Initialize the x location to where the board starts
        while counter < 9:                                      # While the counter is less than 9
            x_location += 77.778                                # Increase the x position by the size of the board / 9
            pygame.draw.line(self.window,                       # Draw a black vertical line
                             (0, 0, 0),                         #
                             (x_location, 100),                 #
                             (x_location, 800), 2)              #
            counter += 1                                        # Increment the counter

        counter = 0                                             # Reset the counter to 0
        y_location = 100.0                                      # Initialize the y location to where the board starts
        while counter < 9:                                      # While the counter is less than 9
            y_location += 77.778                                # Increase the y position by the size of the board / 9
            if counter == 2 or counter == 5:                    # If the counter is 1/3 or 2/3 across the board
                pygame.draw.line(self.window,                   # Draw a white horizontal line
                                 (255, 255, 255),               #
                                 (100, y_location),             #
                                 (800, y_location), 4)          #
            else:                                               # Otherwise
                pygame.draw.line(self.window,                   # Draw a black horizontal line
                                 (0, 0, 0),                     #
                                 (100, y_location),             #
                                 (800, y_location), 2)          #
            counter += 1                                        # Increment the counter

        pygame.draw.line(self.window,                           # Redraw vertical lines that were drawn over by
                         (255, 255, 255),                       # horizontal lines
                         (333.334, 100),                        #
                         (333.334, 800), 4)                     #
        pygame.draw.line(self.window,                           #
                         (255, 255, 255),                       #
                         (566.668, 100),                        #
                         (566.668, 800), 4)                     #

        pygame.draw.rect(                                       # Draw the outer rectangle of the sudoku board
            self.window, (255, 255, 255),                       #
            [100, 100, 702, 702], 4)                            #

    def draw_numbers(self):                                     # A method that draws the numbers on the board
        for i in range(len(self.numbers)):                      # Iterate through the 2D array
            for j in range(len(self.numbers[0])):               #
                if not self.numbers[i][j] == 0:                 # If the current number is not 0 (0 is no number)
                    number = self.font.render(                  # Create the image of the number to draw to the screen
                        str(self.numbers[i][j]), True,          #
                        (255, 255, 255))                        #
                elif self.new_numbers[i][j] != 0:               # If the user has typed a number into this square
                    number = self.font.render(                  # Create the image of the number to draw to the screen
                            str(self.new_numbers[i][j]), True,  #
                            (0, 0, 0))                          #
                else:
                    continue

                x_location = y_location = 0                     # Initialize the x and y locations to 0

                if i == 0:                                      # If the ith index is 0
                    x_location = 122.5                          # Set the x location to 122.5
                elif i == 1:                                    # Elif the ith index is 1
                    x_location = 200.278                        # Set the x location to 200.278
                elif i == 2:                                    # Elif the ith index is 2
                    x_location = 278.056                        # Set the x location to 278.056
                elif i == 3:                                    # Elif the ith index is 3
                    x_location = 355.834                        # Set the x location to 355.834
                elif i == 4:                                    # Elif the ith index is 4
                    x_location = 433.612                        # Set the x location to 433.612
                elif i == 5:                                    # Elif the ith index is 5
                    x_location = 511.39                         # Set the x location to 511.39
                elif i == 6:                                    # Elif the ith index is 6
                    x_location = 589.168                        # Set the x location to 589.168
                elif i == 7:                                    # Elif the ith index is 7
                    x_location = 666.946                        # Set the x location to 666.946
                elif i == 8:                                    # Elif the ith index is 8
                    x_location = 744.724                        # Set the x location to 744.724

                if j == 0:                                      # If the jth index is 0
                    y_location = 110                            # Set the y location to 110
                elif j == 1:                                    # Elif the jth index is 1
                    y_location = 187.778                        # Set the y location to 187.778
                elif j == 2:                                    # Elif the jth index is 2
                    y_location = 265.556                        # Set the y location to 265.556
                elif j == 3:                                    # Elif the jth index is 3
                    y_location = 343.334                        # Set the y location to 343.334
                elif j == 4:                                    # Elif the jth index is 4
                    y_location = 421.112                        # Set the y location to 421.112
                elif j == 5:                                    # Elif the jth index is 5
                    y_location = 498.89                         # Set the y location to 498.89
                elif j == 6:                                    # Elif the jth index is 6
                    y_location = 576.668                        # Set the y location to 576.668
                elif j == 7:                                    # Elif the jth index is 7
                    y_location = 654.446                        # Set the y location to 654.446
                elif j == 8:                                    # Elif the jth index is 8
                    y_location = 732.224                        # Set the y location to 732.224

                self.window.blit(number, (x_location, y_location))

    def check_events(self):                                     # A method that checks for events that occurred
        if not self.menu:
            for event in pygame.event.get():                    # Loop through the events that occurred
                if event.type == pygame.QUIT:                   # If the event is the exit button
                    return False                                # Return false

                mouse_1, \
                    mouse_2, \
                    mouse_3 = pygame.mouse.get_pressed()        # Determine if the mouse buttons have been pressed
                if mouse_1:                                     # If the mouse1 button was pressed
                    x_pos, y_pos = pygame.mouse.get_pos()       # Find the position of the cursor when it was pressed

                    self.x_start = -100                         # Initialize the square to out of the screen
                    self.y_start = -100                         #
                    self.selected_col = -1                      # Initialize the square selected to be -1, -1 (no sqr)
                    self.selected_row = -1                      #

                    # Determine which square was selected
                    if 100 < y_pos <= 177:
                        self.y_start = 100
                        self.selected_row = 0
                    elif 179 < y_pos <= 255:
                        self.y_start = 179
                        self.selected_row = 1
                    elif 257 < y_pos <= 332:
                        self.y_start = 257
                        self.selected_row = 2
                    elif 336 < y_pos <= 410:
                        self.y_start = 336
                        self.selected_row = 3
                    elif 413 < y_pos <= 487:
                        self.y_start = 413
                        self.selected_row = 4
                    elif 490 < y_pos <= 564:
                        self.y_start = 490
                        self.selected_row = 5
                    elif 568 < y_pos <= 643:
                        self.y_start = 568
                        self.selected_row = 6
                    elif 646 < y_pos <= 721:
                        self.y_start = 646
                        self.selected_row = 7
                    elif 724 < y_pos <= 797:
                        self.y_start = 724
                        self.selected_row = 8

                    # Determine which square was selected
                    if 100 < x_pos <= 177:
                        self.x_start = 100
                        self.selected_col = 0
                    elif 179 < x_pos <= 255:
                        self.x_start = 179
                        self.selected_col = 1
                    elif 257 < x_pos <= 332:
                        self.x_start = 257
                        self.selected_col = 2
                    elif 336 < x_pos <= 410:
                        self.x_start = 336
                        self.selected_col = 3
                    elif 413 < x_pos <= 487:
                        self.x_start = 413
                        self.selected_col = 4
                    elif 490 < x_pos <= 564:
                        self.x_start = 490
                        self.selected_col = 5
                    elif 568 < x_pos <= 643:
                        self.x_start = 568
                        self.selected_col = 6
                    elif 646 < x_pos <= 721:
                        self.x_start = 646
                        self.selected_col = 7
                    elif 724 < x_pos <= 797:
                        self.x_start = 724
                        self.selected_col = 8

                if event.type == pygame.KEYDOWN:                # If a key was pressed down
                    if event.key == pygame.K_0:                 # If the key was the #0 key
                        self.number_pressed(0)                  # Call number_pressed method and pass 0
                    if event.key == pygame.K_1:                 # If the key was the #1 key
                        self.number_pressed(1)                  # Call number_pressed method and pass 1
                    if event.key == pygame.K_2:                 # If the key was the #2 key
                        self.number_pressed(2)                  # Call number_pressed method and pass 2
                    if event.key == pygame.K_3:                 # If the key was the #3 key
                        self.number_pressed(3)                  # Call number_pressed method and pass 3
                    if event.key == pygame.K_4:                 # If the key was the #4 key
                        self.number_pressed(4)                  # Call number_pressed method and pass 4
                    if event.key == pygame.K_5:                 # If the key was the #5 key
                        self.number_pressed(5)                  # Call number_pressed method and pass 5
                    if event.key == pygame.K_6:                 # If the key was the #6 key
                        self.number_pressed(6)                  # Call number_pressed method and pass 6
                    if event.key == pygame.K_7:                 # If the key was the #7 key
                        self.number_pressed(7)                  # Call number_pressed method and pass 7
                    if event.key == pygame.K_8:                 # If the key was the #8 key
                        self.number_pressed(8)                  # Call number_pressed method and pass 8
                    if event.key == pygame.K_9:                 # If the key was the #9 key
                        self.number_pressed(9)                  # Call number_pressed method and pass 9

            self.square_clicked()                               # Call a method to update the highlighted square

            if self.check_solution():                           # Check if the player has won
                return False                                    # If the player has won, stop the program
            else:                                               # Otherwise the player has not won and the exit button
                return True                                     # has not been pressed, so keep the program running
        else:                                                   # Else (The player is still at the menu)
            x_pos, y_pos = pygame.mouse.get_pos()               # Get the mouse's position
            if 360 <= x_pos <= 560 and 200 <= y_pos <= 250:     # If the mouse is over the button
                highlight = pygame.Surface((200, 50))           # Create a surface the size of the button
                highlight.set_alpha(100)                        # Make the highlight see through
                highlight.fill((255, 223, 0))                   # Set the color of the surface to gold
                self.window.blit(highlight, (360, 200))         # Highlight the button

            for event in pygame.event.get():                    # Loop through the events that occurred
                if event.type == pygame.QUIT:                   # If the event is the exit button
                    return False                                # Return false

                mouse_1, \
                    mouse_2, \
                    mouse_3 = pygame.mouse.get_pressed()        # Determine if the mouse buttons have been pressed
                if mouse_1:                                     # If the mouse1 button has been clicked
                    if 360 <= x_pos <= 560 and 200 <= y_pos <= 250: # If the mouse is over the button
                        self.menu = False                       # Set self.menu to false to play the game

            return True                                         # Keep the game running

    def square_clicked(self):                                   # Method to update the highlighted squares location
        if self.selected_col != -1 and self.selected_row != -1: # If the mouse has clicked a valid square
            self.x_start = self.selected_col * 77.75 + 103.0    # Update the highlighted squares position
            self.y_start = self.selected_row * 77.75 + 103.0    #

        self.window.blit(self.highlighted_square,               # Put the highlighted square on the screen
                         (self.x_start, self.y_start))          #

    def number_pressed(self, num):                              # Method puts num typed on screen
        if self.selected_col != -1 and self.selected_row != -1:
            self.new_numbers[self.selected_col][self.selected_row] = num

    def update_display(self):                                   # Method to update the game's display
        pygame.display.update()                                 # Update the screen to reflect any changes

    def check_solution(self):                                   # Method that checks if the user's solution is correct
        for i in range(len(self.new_numbers)):                  # Iterate through the 2D array
            for j in range(len(self.new_numbers[0])):           #
                if self.new_numbers[i][j] == 0:                 # If any of the numbers is still 0
                    return False                                # Return false, the game is not over

        for i in range(9):                                      # Iterate through the columns
            current_col = self.new_numbers[i]                   # Create a variable for the current column
            hash_table = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]         # Create a hash table initialized to 0s
            for num in current_col:                             # For each number in the current column
                if hash_table[num] == 0:                        # if the hash table has a 0 still
                    hash_table[num] = 1                         # Set it to 1
                else:                                           # Otherwise, there is a collision
                    return False                                # Return false, the player has not won yet

        for i in range(9):                                      # Iterate through the rows
            current_row = []                                    #
            for j in range(9):                                  # Create the row as a list/array
                current_row.append(self.new_numbers[j][i])      #
            hash_table = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]         # Create a hash table initialized to 0s
            for num in current_row:                             # For each number in the current column
                if hash_table[num] == 0:                        # if the hash table has a 0 still
                    hash_table[num] = 1                         # Set it to 1
                else:                                           # Otherwise, there is a collision
                    return False                                # Return false, the player has not won yet

        for count in range(9):                                  # For each of the 9 squares
            if count == 0:                                      # If it is the first square
                current_square = []                             # Create a list for the current square
                for i in range(3):                              # Append all of the numbers in the square to the list
                    current_square.append(                      #
                        self.new_numbers[0][i])                 #
                for i in range(3):                              #
                    current_square.append(                      #
                        self.new_numbers[1][i])                 #
                for i in range(3):                              #
                    current_square.append(                      #
                        self.new_numbers[2][i])                 #
                hash_table = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]     # Create a hash table initialized to 0s
                for num in current_square:                      # Iterate through the current square
                    if hash_table[num] == 0:                    # if the hash table has a 0 still
                        hash_table[num] = 1                     # Set it to 1
                    else:                                       # Otherwise, there is a collision
                        return False                            # Return false, the player has not won yet
            elif count == 1:                                    # Elif it is the second square
                current_square = []                             # Create a list for the current square
                for i in range(3):                              # Append all of the numbers in the square to the list
                    current_square.append(                      #
                        self.new_numbers[3][i])                 #
                for i in range(3):                              #
                    current_square.append(                      #
                        self.new_numbers[4][i])                 #
                for i in range(3):                              #
                    current_square.append(                      #
                        self.new_numbers[5][i])                 #
                hash_table = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]     # Create a hash table initialized to 0s
                for num in current_square:                      # Iterate through the current square
                    if hash_table[num] == 0:                    # if the hash table has a 0 still
                        hash_table[num] = 1                     # Set it to 1
                    else:                                       # Otherwise, there is a collision
                        return False                            # Return false, the player has not won yet
            elif count == 2:                                    # Elif it is the third square
                current_square = []                             # Create a list for the current square
                for i in range(3):                              # Append all of the numbers in the square to the list
                    current_square.append(                      #
                        self.new_numbers[6][i])                 #
                for i in range(3):                              #
                    current_square.append(                      #
                        self.new_numbers[7][i])                 #
                for i in range(3):                              #
                    current_square.append(                      #
                        self.new_numbers[8][i])                 #
                hash_table = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]     # Create a hash table initialized to 0s
                for num in current_square:                      # Iterate through the current square
                    if hash_table[num] == 0:                    # if the hash table has a 0 still
                        hash_table[num] = 1                     # Set it to 1
                    else:                                       # Otherwise, there is a collision
                        return False                            # Return false, the player has not won yet
            elif count == 3:                                    # Elif it is the fourth square
                current_square = []                             # Create a list for the current square
                for i in range(3, 6):                           # Append all of the numbers in the square to the list
                    current_square.append(                      #
                        self.new_numbers[0][i])                 #
                for i in range(3, 6):                           #
                    current_square.append(                      #
                        self.new_numbers[1][i])                 #
                for i in range(3, 6):                           #
                    current_square.append(                      #
                        self.new_numbers[2][i])                 #
                hash_table = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]     # Create a hash table initialized to 0s
                for num in current_square:                      # Iterate through the current square
                    if hash_table[num] == 0:                    # if the hash table has a 0 still
                        hash_table[num] = 1                     # Set it to 1
                    else:                                       # Otherwise, there is a collision
                        return False                            # Return false, the player has not won yet
            elif count == 4:                                    # Elif it is the fifth square
                current_square = []                             # Create a list for the current square
                for i in range(3, 6):                           # Append all of the numbers in the square to the list
                    current_square.append(                      #
                        self.new_numbers[3][i])                 #
                for i in range(3, 6):                           #
                    current_square.append(                      #
                        self.new_numbers[4][i])                 #
                for i in range(3, 6):                           #
                    current_square.append(                      #
                        self.new_numbers[5][i])                 #
                hash_table = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]     # Create a hash table initialized to 0s
                for num in current_square:                      # Iterate through the current square
                    if hash_table[num] == 0:                    # if the hash table has a 0 still
                        hash_table[num] = 1                     # Set it to 1
                    else:                                       # Otherwise, there is a collision
                        return False                            # Return false, the player has not won yet
            elif count == 5:                                    # Elif it is the sixth square
                current_square = []                             # Create a list for the current square
                for i in range(3, 6):                           # Append all of the numbers in the square to the list
                    current_square.append(                      #
                        self.new_numbers[6][i])                 #
                for i in range(3, 6):                           #
                    current_square.append(                      #
                        self.new_numbers[7][i])                 #
                for i in range(3, 6):                           #
                    current_square.append(                      #
                        self.new_numbers[8][i])                 #
                hash_table = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]     # Create a hash table initialized to 0s
                for num in current_square:                      # Iterate through the current square
                    if hash_table[num] == 0:                    # if the hash table has a 0 still
                        hash_table[num] = 1                     # Set it to 1
                    else:                                       # Otherwise, there is a collision
                        return False                            # Return false, the player has not won yet
            elif count == 6:                                    # Elif it is the seventh square
                current_square = []                             # Create a list for the current square
                for i in range(6, 9):                           # Append all of the numbers in the square to the list
                    current_square.append(                      #
                        self.new_numbers[0][i])                 #
                for i in range(6, 9):                           #
                    current_square.append(                      #
                        self.new_numbers[1][i])                 #
                for i in range(6, 9):                           #
                    current_square.append(                      #
                        self.new_numbers[2][i])                 #
                hash_table = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]     # Create a hash table initialized to 0s
                for num in current_square:                      # Iterate through the current square
                    if hash_table[num] == 0:                    # if the hash table has a 0 still
                        hash_table[num] = 1                     # Set it to 1
                    else:                                       # Otherwise, there is a collision
                        return False                            # Return false, the player has not won yet
            elif count == 7:                                    # Elif it is the eighth square
                current_square = []                             # Create a list for the current square
                for i in range(6, 9):                           # Append all of the numbers in the square to the list
                    current_square.append(                      #
                        self.new_numbers[3][i])                 #
                for i in range(6, 9):                           #
                    current_square.append(                      #
                        self.new_numbers[4][i])                 #
                for i in range(6, 9):                           #
                    current_square.append(                      #
                        self.new_numbers[5][i])                 #
                hash_table = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]     # Create a hash table initialized to 0s
                for num in current_square:                      # Iterate through the current square
                    if hash_table[num] == 0:                    # if the hash table has a 0 still
                        hash_table[num] = 1                     # Set it to 1
                    else:                                       # Otherwise, there is a collision
                        return False                            # Return false, the player has not won yet
            elif count == 8:                                    # Elif it is the nineth square
                current_square = []                             # Create a list for the current square
                for i in range(6, 9):                           # Append all of the numbers in the square to the list
                    current_square.append(                      #
                        self.new_numbers[6][i])                 #
                for i in range(6, 9):                           #
                    current_square.append(                      #
                        self.new_numbers[7][i])                 #
                for i in range(6, 9):                           #
                    current_square.append(                      #
                        self.new_numbers[8][i])                 #
                hash_table = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]     # Create a hash table initialized to 0s
                for num in current_square:                      # Iterate through the current square
                    if hash_table[num] == 0:                    # if the hash table has a 0 still
                        hash_table[num] = 1                     # Set it to 1
                    else:                                       # Otherwise, there is a collision
                        return False                            # Return false, the player has not won yet

        return True                                             # If false has not yet been returned, the player won

    def __get_solution(self):
        pass
