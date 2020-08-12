# File that holds the Sudoku class
import pygame
from time import sleep


class Sudoku:
    def __init__(self):
        pygame.init()                                           # Initialize pygame

        pygame.display.set_caption("Sudoku")                    # Give the window a title
        self.window = pygame.display.set_mode((900, 900))       # Create a window

        self.font = pygame.font.Font("freesansbold.ttf", 64)    # Set the font to draw the numbers

        self.menu = True                                        # Start off by showing the menu and not the game
        self.player_won = False                                 # Start off by not showing the win screen

        self.highlighted_square = pygame.Surface((75, 75))      # Create a surface that will become the highlighted sqr
        self.highlighted_square.set_alpha(100)                  # Set the opacity of the square
        self.highlighted_square.fill((255, 223, 0))             # Set the color of the square
        self.highlight_xpos = -100                              # Initialize highlighted square to out of frame
        self.highlight_ypos = -100                              #
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
        self.new_numbers = [[0]*9 for i in range(9)]
        self.computer_numbers = [[0]*9 for i in range(9)]
        self.auto_solve_clicked = False

    def set_background(self):                                   # Method that sets the background of the game
        self.window.fill((102, 178, 255))                       # Uses RGB to set the background color to light blue
        if self.player_won:                                     # If the player has won
            self.win_screen()                                   # Display the win screen
        elif self.menu:                                         # Elif the user is still at the menu
            self.display_menu()                                 # Display the menu
        else:                                                   # Otherwise
            self.draw_board()                                   # Call the method to draw the board
            self.draw_numbers()                                 # Call the method to put the numbers on the board

    def display_menu(self):                                     # Method that displays the main menu to the user
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

        # Create auto solve and main menu buttons
        pygame.draw.rect(self.window,                               # Draw auto solve button
                             (255, 255, 255), [230, 825, 200, 50])  #
        pygame.draw.rect(self.window,                               # Give the button an outline
                             (0, 0, 0), [230, 825, 200, 50], 3)     #
        button_font = pygame.font.Font("freesansbold.ttf", 32)      # Set the font
        auto_solve = button_font.render("Auto Solve",               # Put the text on the button
                                             True, (0, 0, 0))       #
        self.window.blit(auto_solve, (245, 835))                    #

        pygame.draw.rect(self.window,                               # Draw main menu button
                             (255, 255, 255), [490, 825, 200, 50])  #
        pygame.draw.rect(self.window,                               # Give the button an outline
                             (0, 0, 0), [490, 825, 200, 50], 3)     #
        button_font = pygame.font.Font("freesansbold.ttf", 32)      # Set the font
        auto_solve = button_font.render("Main Menu",                # Put the text on the button
                                            True, (0, 0, 0))        #
        self.window.blit(auto_solve, (505, 835))                    #
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
        for i in range(len(self.numbers[0])):                   # Iterate through the 2D array
            for j in range(len(self.numbers)):                  #
                if not self.numbers[i][j] == 0:                 # If the current number is not 0 (0 is no number)
                    number = self.font.render(                  # Create the image of the number to draw to the screen
                        str(self.numbers[i][j]), True,          #
                        (255, 255, 255))                        #
                elif self.auto_solve_clicked:                   # Elif the player clicked the auto solve button
                    if self.new_numbers[i][j] != self.computer_numbers[i][j]:  # If the player was wrong or had no num
                        number = self.font.render(                             # Display the num in red
                                str(self.computer_numbers[i][j]),              #
                                     True, (255, 0, 0))                        #
                    else:                                                      # Otherwise the player was right
                        number = self.font.render(                             # So, display the num in green
                            str(self.computer_numbers[i][j]),                  #
                            True, (0, 255, 0))                                 #
                elif self.new_numbers[i][j] != 0:               # If the user has typed a number into this square
                    number = self.font.render(                  # Create the image of the number to draw to the screen
                            str(self.new_numbers[i][j]), True,  #
                            (0, 0, 0))                          #
                else:
                    continue

                x_location = y_location = 0                     # Initialize the x and y locations to 0

                if j == 0:                                      # If the jth index is 0
                    x_location = 122.5                          # Set the x location to 122.5
                elif j == 1:                                    # Elif the jth index is 1
                    x_location = 200.278                        # Set the x location to 200.278
                elif j == 2:                                    # Elif the jth index is 2
                    x_location = 278.056                        # Set the x location to 278.056
                elif j == 3:                                    # Elif the jth index is 3
                    x_location = 355.834                        # Set the x location to 355.834
                elif j == 4:                                    # Elif the jth index is 4
                    x_location = 433.612                        # Set the x location to 433.612
                elif j == 5:                                    # Elif the jth index is 5
                    x_location = 511.39                         # Set the x location to 511.39
                elif j == 6:                                    # Elif the jth index is 6
                    x_location = 589.168                        # Set the x location to 589.168
                elif j == 7:                                    # Elif the jth index is 7
                    x_location = 666.946                        # Set the x location to 666.946
                elif j == 8:                                    # Elif the jth index is 8
                    x_location = 744.724                        # Set the x location to 744.724

                if i == 0:                                      # If the ith index is 0
                    y_location = 110                            # Set the y location to 110
                elif i == 1:                                    # Elif the ith index is 1
                    y_location = 187.778                        # Set the y location to 187.778
                elif i == 2:                                    # Elif the ith index is 2
                    y_location = 265.556                        # Set the y location to 265.556
                elif i == 3:                                    # Elif the ith index is 3
                    y_location = 343.334                        # Set the y location to 343.334
                elif i == 4:                                    # Elif the ith index is 4
                    y_location = 421.112                        # Set the y location to 421.112
                elif i == 5:                                    # Elif the ith index is 5
                    y_location = 498.89                         # Set the y location to 498.89
                elif i == 6:                                    # Elif the ith index is 6
                    y_location = 576.668                        # Set the y location to 576.668
                elif i == 7:                                    # Elif the ith index is 7
                    y_location = 654.446                        # Set the y location to 654.446
                elif i == 8:                                    # Elif the ith index is 8
                    y_location = 732.224                        # Set the y location to 732.224

                self.window.blit(number, (x_location, y_location))

    def check_events(self):                                     # A method that checks for events that occurred
        if not self.menu and not self.player_won:               # If the game is not at menu and the player didn't win
            x_pos, y_pos = pygame.mouse.get_pos()               # Find the position of the cursor
            for event in pygame.event.get():                    # Loop through the events that occurred
                if event.type == pygame.QUIT:                   # If the event is the exit button
                    return False                                # Return false

                mouse_1, \
                    mouse_2, \
                    mouse_3 = pygame.mouse.get_pressed()        # Determine if the mouse buttons have been pressed
                if mouse_1:                                     # If the mouse1 button was pressed
                    self.selected_col = -1                      # Initialize the square selected to be -1, -1 (no sqr)
                    self.selected_row = -1                      #

                    # Determine which square was selected
                    if 100 < y_pos <= 177:
                        self.selected_row = 0
                    elif 179 < y_pos <= 255:
                        self.selected_row = 1
                    elif 257 < y_pos <= 332:
                        self.selected_row = 2
                    elif 336 < y_pos <= 410:
                        self.selected_row = 3
                    elif 413 < y_pos <= 487:
                        self.selected_row = 4
                    elif 490 < y_pos <= 564:
                        self.selected_row = 5
                    elif 568 < y_pos <= 643:
                        self.selected_row = 6
                    elif 646 < y_pos <= 721:
                        self.selected_row = 7
                    elif 724 < y_pos <= 797:
                        self.selected_row = 8
                    else:
                        self.selected_row = -1

                    # Determine which square was selected
                    if 100 < x_pos <= 177:
                        self.selected_col = 0
                    elif 179 < x_pos <= 255:
                        self.selected_col = 1
                    elif 257 < x_pos <= 332:
                        self.selected_col = 2
                    elif 336 < x_pos <= 410:
                        self.selected_col = 3
                    elif 413 < x_pos <= 487:
                        self.selected_col = 4
                    elif 490 < x_pos <= 564:
                        self.selected_col = 5
                    elif 568 < x_pos <= 643:
                        self.selected_col = 6
                    elif 646 < x_pos <= 721:
                        self.selected_col = 7
                    elif 724 < x_pos <= 797:
                        self.selected_col = 8
                    else:
                        self.selected_col = -1

                if event.type == pygame.KEYDOWN and not self.auto_solve_clicked:  # If a key was pressed down
                    if event.key == pygame.K_BACKSPACE:         # If the key was the backspace button
                        self.number_pressed(0)                  # Call number_pressed and pass 0 to delete the num
                    if event.key == pygame.K_DELETE:            # If the key was the delete button
                        self.number_pressed(0)                  # Call number_pressed and pass 0 to delete the num
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

            # Create the auto solve and main menu highlights, and controls
            if 230 <= x_pos <= 430 and 825 <= y_pos <= 875:     # If the mouse is over the button
                highlight = pygame.Surface((200, 50))           # Create a surface the size of the button
                highlight.set_alpha(100)                        # Make the highlight see through
                highlight.fill((255, 223, 0))                   # Set the color of the surface to gold
                self.window.blit(highlight, (230, 825))         # Highlight the button
                mouse_1, mouse_2, mouse_3 = pygame.mouse.get_pressed()
                if mouse_1:                                     # If the auto_solve button was clicked
                    self.solve_board()                          # Solve the board using backtracking
                    self.auto_solve_clicked = True              # Set the auto_solve flag to true
            elif 490 <= x_pos <= 690 and 825 <= y_pos <= 875:
                highlight = pygame.Surface((200, 50))           # Create a surface the size of the button
                highlight.set_alpha(100)                        # Make the highlight see through
                highlight.fill((255, 223, 0))                   # Set the color of the surface to gold
                self.window.blit(highlight, (490, 825))         # Highlight the button
                mouse_1, mouse_2, mouse_3 = pygame.mouse.get_pressed()
                if mouse_1:                                     # If the auto_solve button was clicked
                    self.auto_solve_clicked = False             #
                    self.menu = True                            # Set the auto_solve flag to true
            # # # # # # # # # # # # # # # # # # # # # # # # # # #

            self.square_clicked()                               # Call a method to update the highlighted square

            if self.check_solution():                           # Check if the player has won
                self.draw_numbers()                             # Ensure that the last number typed is drawn
                self.update_display()                           #
                sleep(0.25)                                     # Pause the game for 1/4 second
                self.win_screen()                               # Call a method to display the win screen
        elif self.menu and not self.player_won:                 # Elif the player is at the menu and hasn't just won
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
                    if 360 <= x_pos <= 560 and 200 <= y_pos <= 250:  # If the mouse is over the button
                        self.menu = False                       # Set self.menu to false to play the game
                        for i in range(len(self.numbers)):      # Reset the player and computer arrays
                            for j in range(len(self.numbers[i])):
                                self.new_numbers[i][j] = self.numbers[i][j]
                                self.computer_numbers[i][j] = self.numbers[i][j]
        else:                                                   # Otherwise, the player is on the win screen
            x_pos, y_pos = pygame.mouse.get_pos()               # Get the mouse's position
            if 340 <= x_pos <= 590 and 400 <= y_pos <= 450:     # If the mouse is over the button
                highlight = pygame.Surface((250, 50))           # Create a surface the size of the button
                highlight.set_alpha(100)                        # Make the highlight see through
                highlight.fill((255, 223, 0))                   # Set the color of the surface to gold
                self.window.blit(highlight, (340, 400))         # Highlight the button

            for event in pygame.event.get():                    # Loop through the events that occurred
                if event.type == pygame.QUIT:                   # If the event is the exit button
                    return False                                # Return false

                mouse_1, \
                    mouse_2, \
                    mouse_3 = pygame.mouse.get_pressed()        # Determine if the mouse buttons have been pressed
                if mouse_1:                                     # If the mouse1 button has been clicked
                    if 340 <= x_pos <= 590 and 400 <= y_pos <= 450:  # If the mouse is over the button
                        self.menu = True                        # Set self.menu to true to go to the menu
                        self.player_won = False                 # Set self.player_won to false

        return True                                             # Keep the game running

    def square_clicked(self):                                   # Method to update the highlighted squares location
        if self.selected_col != -1 and self.selected_row != -1:  # If the mouse has clicked a valid square
            self.highlight_xpos = self.selected_col * 77.75 + 103.0    # Update the highlighted squares position
            self.highlight_ypos = self.selected_row * 77.75 + 103.0
        else:
            self.highlight_xpos = -100
            self.highlight_ypos = -100

        self.window.blit(self.highlighted_square,               # Put the highlighted square on the screen
                         (self.highlight_xpos, self.highlight_ypos))

    def number_pressed(self, num):                              # Method puts num typed on screen, if it is a valid spot
        if self.selected_col != -1 and self.selected_row != -1:
            if self.numbers[self.selected_row][self.selected_col] == 0:
                self.new_numbers[self.selected_row][self.selected_col] = num

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
            for num in current_row:                             # For each number in the current row
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

    def win_screen(self):                                       # Method that notifies the user that he/she won
        self.player_won = True                                  # Set player_won to true since user won

        win_text = self.font.render("YOU WIN!",                 # Print "YOU WIN!" to the screen
                                    True, (255, 255, 255))      #
        self.window.blit(win_text, (300, 200))                  #

        pygame.draw.rect(self.window,                           # Draw the button
                         (255, 255, 255), [340, 400, 250, 50])  #
        pygame.draw.rect(self.window,                           # Give the button an outline
                         (0, 0, 0), [340, 400, 250, 50], 3)     #
        button_font = pygame.font.Font("freesansbold.ttf", 32)  # Set the font
        menu_button = button_font.render("Back to Menu",        # Put the text on the button
                                       True, (0, 0, 0))         #
        self.window.blit(menu_button, (357, 410))               #

    def solve_board(self):
        row, col = self.next_empty()
        if row == -1 and col == -1:
            return True

        for i in range(1, 10):
            if self.__check_row(i, row) and self.__check_column(i, col) and self.__check_square(i, row, col):
                self.computer_numbers[row][col] = i

                if self.solve_board():
                    return True

                self.computer_numbers[row][col] = 0

        return False

    def next_empty(self):
        for i in range(len(self.computer_numbers)):
            for j in range(len(self.computer_numbers[i])):
                if self.computer_numbers[i][j] == 0:
                    return i, j
        return -1, -1

    def __check_row(self, new_num, row_num):                    # Method that checks the row
        for j in range(9):                                      # For all numbers in the row
            if self.computer_numbers[row_num][j] == new_num:    # If there already exists the num we wish to add
                return False                                    # We cannot add it, so return False
        return True                                             # Return True, the num can be in the row

    def __check_column(self, new_num, col_num):                 # Method that checks the column
        for i in range(9):                                      # For each number in the column
            if self.computer_numbers[i][col_num] == new_num:    # If there already exists the num we wish to add
                return False                                    # We cannot add it, so return false
        return True                                             # Return True, the num can be added to the col

    def __check_square(self, new_num, row_num, col_num):        # Method that checks the square
        curr_square = []                                        # Create a list to represent the square
        # Fill the list with the numbers in the square
        if 0 <= row_num <= 2:
            if 0 <= col_num <= 2:
                for i in range(3):
                    for j in range(3):
                        curr_square.append(self.computer_numbers[i][j])
            elif 3 <= col_num <= 5:
                for i in range(3):
                    for j in range(3, 6):
                        curr_square.append(self.computer_numbers[i][j])
            elif 6 <= col_num <= 8:
                for i in range(3):
                    for j in range(6, 9):
                        curr_square.append(self.computer_numbers[i][j])
        elif 3 <= row_num <= 5:
            if 0 <= col_num <= 2:
                for i in range(3, 6):
                    for j in range(3):
                        curr_square.append(self.computer_numbers[i][j])
            elif 3 <= col_num <= 5:
                for i in range(3, 6):
                    for j in range(3, 6):
                        curr_square.append(self.computer_numbers[i][j])
            elif 6 <= col_num <= 8:
                for i in range(3, 6):
                    for j in range(6, 9):
                        curr_square.append(self.computer_numbers[i][j])
        elif 6 <= row_num <= 8:
            if 0 <= col_num <= 2:
                for i in range(6, 9):
                    for j in range(3):
                        curr_square.append(self.computer_numbers[i][j])
            elif 3 <= col_num <= 5:
                for i in range(6, 9):
                    for j in range(3, 6):
                        curr_square.append(self.computer_numbers[i][j])
            elif 6 <= col_num <= 8:
                for i in range(6, 9):
                    for j in range(6, 9):
                        curr_square.append(self.computer_numbers[i][j])

        for num in curr_square:                                 # For each number in the square
            if num == new_num:                                  # If the new number is already in the square
                return False                                    # The new number is invalid

        return True                                             # Return True, the square is good
