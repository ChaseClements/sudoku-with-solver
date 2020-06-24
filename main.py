from Sudoku import Sudoku


def main():
    game = Sudoku()
    play(game)


def play(game):
    running = True
    while running:
        game.set_background()                                   # Set the background
        running = game.check_events()                           # Check if an event has occurred
        game.update_display()                                   # Update the display

main()
