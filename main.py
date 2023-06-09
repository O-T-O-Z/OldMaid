import sys

from game import Game


def main():
    try:
        num_players = int(sys.argv[1])
    except:
        print("Give a number of players!")
        exit()

    game = Game(num_players)
    game.run()


if __name__ == '__main__':
    main()

