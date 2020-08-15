# File that holds the Sudoku class
import pygame
from time import sleep
from Board import Board


class Sudoku:
    def __init__(self):
        pygame.init()                                           # Initialize pygame

        pygame.display.set_caption("Sudoku")                    # Give the window a title
        self.window = pygame.display.set_mode((900, 900))       # Create a window

        self.font = pygame.font.Font("freesansbold.ttf", 64)    # Set the font to draw the numbers

        self.menu = True                                        # Start off by showing the menu and not the game
        self.player_won = False                                 # Start off by not showing the win screen
        self.level_select = False                               # Start off by not displaying the level select
        self.auto_solve_clicked = False                         # Auto_solve button flag

        self.highlighted_square = pygame.Surface((75, 75))      # Create a surface that will become the highlighted sqr
        self.highlighted_square.set_alpha(100)                  # Set the opacity of the square
        self.highlighted_square.fill((255, 223, 0))             # Set the color of the square
        self.highlight_xpos = -100                              # Initialize highlighted square to out of frame
        self.highlight_ypos = -100                              #
        self.selected_col = -1                                  # Initialize the col and row number of the highlighted
        self.selected_row = -1                                  # square to outside of the frame

        self.board = Board()                                    # Create the board object
        self.board.set_board(1)                                 # Set the board to board 1
        self.numbers = self.board.get_board()                    # Set self.numbers to the current board

        self.new_numbers = [[0]*9 for i in range(9)]            # Initialize the new_numbers and computer_numbers arrs
        self.computer_numbers = [[0]*9 for i in range(9)]       #

    def set_background(self):                                   # Method that sets the background of the game
        self.window.fill((102, 178, 255))                       # Uses RGB to set the background color to light blue
        if self.player_won:                                     # If the player has won
            self.win_screen()                                   # Display the win screen
        elif self.menu:                                         # Elif the user is still at the menu
            if not self.level_select:                           # If the level_select flag is false
                self.display_menu()                             # Display the menu
            else:                                               # Else, the level select flag must be true
                self.display_level_select()                     # Call method to display the level select
        else:                                                   # Otherwise
            self.draw_board()                                   # Call the method to draw the board
            self.draw_numbers()                                 # Call the method to put the numbers on the board

    def win_screen(self):                                       # Method that notifies the user that he/she won
        self.player_won = True                                  # Set player_won to true since user won

        win_text = self.font.render("YOU WIN!",                 # Print "YOU WIN!" to the screen
                                    True, (255, 255, 255))      #
        self.window.blit(win_text, (300, 200))                  #

        # Draw the back to menu button # # # # # # # # # # # # #
        pygame.draw.rect(self.window,                           # Draw the button
                         (255, 255, 255), [340, 400, 250, 50])  #
        pygame.draw.rect(self.window,                           # Give the button an outline
                         (0, 0, 0), [340, 400, 250, 50], 3)     #
        button_font = pygame.font.Font("freesansbold.ttf", 32)  # Set the font
        menu_button = button_font.render("Back to Menu",        # Put the text on the button
                                       True, (0, 0, 0))         #
        self.window.blit(menu_button, (357, 410))               #
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def display_menu(self):                                     # Method that displays the main menu to the user
        title = self.font.render("SUDOKU", True,                # Display a title to the screen
                                 (255, 255, 255))               #
        self.window.blit(title, (320, 70))                      #

        self.selected_col = -1                                  # Ensure the square is out of the way
        self.selected_row = -1                                  #

        # Draw the play game button # # # # # # # # # # # # # # #
        pygame.draw.rect(self.window,                           # Draw the button
                         (255, 255, 255), [360, 200, 200, 50])  #
        pygame.draw.rect(self.window,                           # Give the button an outline
                         (0, 0, 0), [360, 200, 200, 50], 3)     #
        button_font = pygame.font.Font("freesansbold.ttf", 32)  # Set the font
        play_game = button_font.render("Play Game",             # Put the text on the button
                                       True, (0, 0, 0))         #
        self.window.blit(play_game, (375, 210))                 #
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def display_level_select(self):
        title = self.font.render("Level Select", True,          # Display level select to the user
                                 (255, 255, 255))               #
        self.window.blit(title, (260, 70))                      #

        # Draw the easy board button # # # # # # # # # # # # # #
        pygame.draw.rect(self.window,                           # Draw the button
                         (255, 255, 255), [100, 300, 200, 200]) #
        pygame.draw.rect(self.window,                           # Give the button an outline
                         (0, 0, 0), [100, 300, 200, 200], 3)    #
        button_font = pygame.font.Font("freesansbold.ttf", 64)  # Set the font
        menu_button = button_font.render("Easy",                # Put the text on the button
                                         True, (0, 0, 0))       #
        self.window.blit(menu_button, (125, 375))               #
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

        # Draw the medium board button # # # # # # # # # # # # #
        pygame.draw.rect(self.window,                           # Draw the button
                         (255, 255, 255), [350, 300, 200, 200]) #
        pygame.draw.rect(self.window,                           # Give the button an outline
                         (0, 0, 0), [350, 300, 200, 200], 3)    #
        button_font = pygame.font.Font("freesansbold.ttf", 64)  # Set the font
        menu_button = button_font.render("Med",                 # Put the text on the button
                                         True, (0, 0, 0))       #
        self.window.blit(menu_button, (385, 375))               #
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

        # Draw the hard board button # # # # # # # # # # # # # #
        pygame.draw.rect(self.window,                           # Draw the button
                         (255, 255, 255), [600, 300, 200, 200]) #
        pygame.draw.rect(self.window,                           # Give the button an outline
                         (0, 0, 0), [600, 300, 200, 200], 3)    #
        button_font = pygame.font.Font("freesansbold.ttf", 64)  # Set the font
        menu_button = button_font.render("Hard",                # Put the text on the button
                                         True, (0, 0, 0))       #
        self.window.blit(menu_button, (625, 375))               #
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

        # Draw the main menu button # # # # # # # # # # # # # # #
        pygame.draw.rect(self.window,                           # Draw the button
                         (255, 255, 255), [350, 700, 200, 50])  #
        pygame.draw.rect(self.window,                           # Give the button an outline
                         (0, 0, 0), [350, 700, 200, 50], 3)     #
        button_font = pygame.font.Font("freesansbold.ttf", 32)  # Set the font
        play_game = button_font.render("Main Menu",             # Put the text on the button
                                       True, (0, 0, 0))         #
        self.window.blit(play_game, (365, 710))                 #
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def draw_board(self):                                       # A method that draws the board
        title = self.font.render("SUDOKU", True,                # Display a title to the screen
                                 (255, 255, 255))               #
        self.window.blit(title, (320, 25))                      #

        # Create auto solve and main menu buttons # # # # # # # # # #
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

        # Draw the lines for the board # # # # # # # # # # # # #
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
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def draw_numbers(self):                                     # A method that draws the numbers on the board
        for i in range(len(self.numbers)):                      # Iterate through the 2D array
            for j in range(len(self.numbers[i])):               #
                if self.numbers[i][j] != 0:                     # If the current number is not 0 (0 is no number)
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
                else:                                           #
                    continue                                    # Continue to skip below code and save time

                x_location = y_location = 0                     # Initialize the x and y locations to 0

                if j == 0:                                      # If the jth index is 0
                    y_location = 110                            # Set the y location
                elif j == 1:                                    # Elif the jth index is 1
                    y_location = 187.778                        # Set the y location
                elif j == 2:                                    # Elif the jth index is 2
                    y_location = 265.556                        # Set the y location
                elif j == 3:                                    # Elif the jth index is 3
                    y_location = 343.334                        # Set the y location
                elif j == 4:                                    # Elif the jth index is 4
                    y_location = 421.112                        # Set the y location
                elif j == 5:                                    # Elif the jth index is 5
                    y_location = 498.89                         # Set the y location
                elif j == 6:                                    # Elif the jth index is 6
                    y_location = 576.668                        # Set the y location
                elif j == 7:                                    # Elif the jth index is 7
                    y_location = 654.446                        # Set the y location
                elif j == 8:                                    # Elif the jth index is 8
                    y_location = 732.224                        # Set the y location

                if i == 0:                                      # If the ith index is 0
                    x_location = 122.5                            # Set the x location
                elif i == 1:                                    # Elif the ith index is 1
                    x_location = 200.278                        # Set the x location
                elif i == 2:                                    # Elif the ith index is 2
                    x_location = 278.056                        # Set the x location
                elif i == 3:                                    # Elif the ith index is 3
                    x_location = 355.834                        # Set the x location
                elif i == 4:                                    # Elif the ith index is 4
                    x_location = 433.612                        # Set the x location
                elif i == 5:                                    # Elif the ith index is 5
                    x_location = 511.39                         # Set the x location
                elif i == 6:                                    # Elif the ith index is 6
                    x_location = 589.168                        # Set the x location
                elif i == 7:                                    # Elif the ith index is 7
                    x_location = 666.946                        # Set the x location
                elif i == 8:                                    # Elif the ith index is 8
                    x_location = 744.724                        # Set the x location

                self.window.blit(number, (x_location, y_location))

    def check_events(self):                                     # A method that checks for events that occurred
        mouse_1, mouse_2, mouse_3 = pygame.mouse.get_pressed()  # Determine if the mouse buttons have been pressed
        x_pos, y_pos = pygame.mouse.get_pos()                   # Find the position of the cursor

        if not self.menu and not self.player_won:               # If the game is not at menu and the player didn't win
            for event in pygame.event.get():                    # Loop through the events that occurred
                if event.type == pygame.QUIT:                   # If the event is the exit button
                    return False                                # Return false

                if mouse_1:                                     # If the mouse1 button was pressed
                    self.selected_col = -1                      # Initialize the square selected to be -1, -1 (no sqr)
                    self.selected_row = -1                      #

                    # Determine which square was selected
                    if 100 < y_pos <= 177:
                        self.selected_col = 0
                    elif 179 < y_pos <= 255:
                        self.selected_col = 1
                    elif 257 < y_pos <= 332:
                        self.selected_col = 2
                    elif 336 < y_pos <= 410:
                        self.selected_col = 3
                    elif 413 < y_pos <= 487:
                        self.selected_col = 4
                    elif 490 < y_pos <= 564:
                        self.selected_col = 5
                    elif 568 < y_pos <= 643:
                        self.selected_col = 6
                    elif 646 < y_pos <= 721:
                        self.selected_col = 7
                    elif 724 < y_pos <= 797:
                        self.selected_col = 8
                    else:
                        self.selected_col = -1

                    # Determine which square was selected
                    if 100 < x_pos <= 177:
                        self.selected_row = 0
                    elif 179 < x_pos <= 255:
                        self.selected_row = 1
                    elif 257 < x_pos <= 332:
                        self.selected_row = 2
                    elif 336 < x_pos <= 410:
                        self.selected_row = 3
                    elif 413 < x_pos <= 487:
                        self.selected_row = 4
                    elif 490 < x_pos <= 564:
                        self.selected_row = 5
                    elif 568 < x_pos <= 643:
                        self.selected_row = 6
                    elif 646 < x_pos <= 721:
                        self.selected_row = 7
                    elif 724 < x_pos <= 797:
                        self.selected_row = 8
                    else:
                        self.selected_row = -1

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
                if mouse_1:                                     # If the auto_solve button was clicked
                    self.solve_board()                          # Solve the board using backtracking
                    self.auto_solve_clicked = True              # Set the auto_solve flag to true
            elif 490 <= x_pos <= 690 and 825 <= y_pos <= 875:
                highlight = pygame.Surface((200, 50))           # Create a surface the size of the button
                highlight.set_alpha(100)                        # Make the highlight see through
                highlight.fill((255, 223, 0))                   # Set the color of the surface to gold
                self.window.blit(highlight, (490, 825))         # Highlight the button
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
            for event in pygame.event.get():                    # Loop through the events that occurred
                if event.type == pygame.QUIT:                   # If the event is the exit button
                    return False                                # Return false

            if not self.level_select:                           # If the player is at main menu and not level select
                if 360 <= x_pos <= 560 and 200 <= y_pos <= 250:     # If the mouse is over the button
                    highlight = pygame.Surface((200, 50))           # Create a surface the size of the button
                    highlight.set_alpha(100)                        # Make the highlight see through
                    highlight.fill((255, 223, 0))                   # Set the color of the surface to gold
                    self.window.blit(highlight, (360, 200))         # Highlight the button

                    if mouse_1:                                     # If the mouse1 button has been clicked
                        if 360 <= x_pos <= 560 and 200 <= y_pos <= 250:  # If the mouse is over the button
                            self.level_select = True                # Set level select to true
                            for i in range(len(self.numbers)):      # Reset the player and computer arrays
                                for j in range(len(self.numbers[i])):
                                    self.new_numbers[i][j] = self.numbers[i][j]
                                    self.computer_numbers[i][j] = self.numbers[i][j]
            else:
                highlight = pygame.Surface((200, 200))          # Create a surface the size of the button
                highlight.set_alpha(100)                        # Make the highlight see through
                highlight.fill((255, 223, 0))                   # Set the color of the surface to gold

                if 100 <= x_pos <= 300 and 300 <= y_pos <= 500:     # If the cursor is on the easy button
                    self.window.blit(highlight, (100, 300))         # Highlight the button
                    if mouse_1:                                     # If the user left clicked
                        self.board.set_board(1)                     # Set the game board
                        self.level_select = False                   # Turn off level select
                        self.menu = False                           # Turn off the menu
                elif 350 <= x_pos <= 550 and 300 <= y_pos <= 500:   # Elif the cursor is on the med button
                    self.window.blit(highlight, (350, 300))         # Highlight the button
                    if mouse_1:                                     # If the user left clicked
                        self.board.set_board(2)                     # Set the game board
                        self.level_select = False                   # Turn off level select
                        self.menu = False                           # Turn off the menu
                elif 600 <= x_pos <= 800 and 300 <= y_pos <= 500:   # Elif the cursor is on the hard button
                    self.window.blit(highlight, (600, 300))         # Highlight the button
                    if mouse_1:                                     # If the user left clicked
                        self.board.set_board(3)                     # Set the game board
                        self.level_select = False                   # Turn off level select
                        self.menu = False                           # Turn off the menu
                elif 350 < x_pos <= 550 and 700 <= y_pos <= 750:    # Elif the cursor is on the main menu button
                    highlight = pygame.Surface((200, 50))           # Create a surface the size of the button
                    highlight.set_alpha(100)                        # Make the highlight see through
                    highlight.fill((255, 223, 0))                   # Set the color of the surface to gold
                    self.window.blit(highlight, (350, 700))         # Highlight the
                    if mouse_1:                                     # If the user left clicked
                        self.level_select = False                   # Return to the main menu

        else:                                                   # Otherwise, the player is on the win screen
            if 340 <= x_pos <= 590 and 400 <= y_pos <= 450:     # If the mouse is over the button
                highlight = pygame.Surface((250, 50))           # Create a surface the size of the button
                highlight.set_alpha(100)                        # Make the highlight see through
                highlight.fill((255, 223, 0))                   # Set the color of the surface to gold
                self.window.blit(highlight, (340, 400))         # Highlight the button

            for event in pygame.event.get():                    # Loop through the events that occurred
                if event.type == pygame.QUIT:                   # If the event is the exit button
                    return False                                # Return false

                if mouse_1:                                     # If the mouse1 button has been clicked
                    if 340 <= x_pos <= 590 and 400 <= y_pos <= 450:  # If the mouse is over the button
                        self.menu = True                        # Set self.menu to true to go to the menu
                        self.player_won = False                 # Set self.player_won to false

        return True                                             # Keep the game running

    def square_clicked(self):                                   # Method to update the highlighted squares location
        if self.selected_row != -1 and self.selected_col != -1:  # If the mouse has clicked a valid square
            self.highlight_xpos = self.selected_row * 77.75 + 103.0    # Update the highlighted squares position
            self.highlight_ypos = self.selected_col * 77.75 + 103.0
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
        # Check if there are still empty square # # # # # # # # #
        for i in range(len(self.new_numbers)):                  # Iterate through the 2D array
            for j in range(len(self.new_numbers[0])):           #
                if self.new_numbers[i][j] == 0:                 # If any of the numbers is still 0
                    return False                                # Return false, the game is not over
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

        # Check if each row is correct (ie has each num 1 to 9) #
        for i in range(9):                                      # Iterate through the columns
            current_row = self.new_numbers[i]                   # Create a variable for the current row
            hash_table = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]         # Create a hash table initialized to 0s
            for num in current_row:                             # For each number in the current column
                if hash_table[num] == 0:                        # if the hash table has a 0 still
                    hash_table[num] = 1                         # Set it to 1
                else:                                           # Otherwise, there is a collision
                    return False                                # Return false, the player has not won yet
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

        # Check if each col is correct (ie has each num 1 to 9) #
        for i in range(9):                                      # Iterate through the columns
            current_col = []                                    #
            for j in range(9):                                  # Create the row as a list/array
                current_col.append(self.new_numbers[i][j])      #
            hash_table = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]         # Create a hash table initialized to 0s
            for num in current_col:                             # For each number in the current column
                if hash_table[num] == 0:                        # if the hash table has a 0 still
                    hash_table[num] = 1                         # Set it to 1
                else:                                           # Otherwise, there is a collision
                    return False                                # Return false, the player has not won yet
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

        # Check if each square is correct # # # # # # # # # # # #
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
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

        return True                                             # If false has not yet been returned, the player won

    def solve_board(self):                                      # Solves the board if the auto_solve button is pressed
        row, col = self.next_empty()                            # Find the next empty square
        if row == -1 and col == -1:                             # If all squares are filled
            return True                                         # Return true (solved)

        for i in range(1, 10):                                  # We will try numbers 1 to 9
            # If the current num works in the row, col and square
            if self.__check_row(i, row) and self.__check_column(i, col) and self.__check_square(i, row, col):
                self.computer_numbers[row][col] = i             # Set the square to that number

                if self.solve_board():                          # Recursively call the function
                    return True                                 # If the next call worked, return true

                self.computer_numbers[row][col] = 0             # If the next call returned false, reset element to 0

        return False                                            # Return false (unsolved)

    def next_empty(self):                                       # Method that returns the next empty location of array
        for i in range(len(self.computer_numbers)):             # Iterate through 2D array
            for j in range(len(self.computer_numbers[i])):      #
                if self.computer_numbers[i][j] == 0:            # If the element is 0
                    return i, j                                 # Return its location
        return -1, -1                                           # If none are 0, return an impossible location

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
