from game import game
from game_assist import game_assist


def main():
    selection = input("Input a to play game: ") 
    if selection == 'a':
        game()

if __name__ == "__main__":
    main()
