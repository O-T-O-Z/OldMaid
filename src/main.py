import sys

from game import Game

N_EXPERIMENTS = 1


def main():
    try:
        num_players = int(sys.argv[1])
    except:
        print("Give a number of players!")
        exit()

    loser_hist = [0] * num_players
    for _ in range(N_EXPERIMENTS):
        game = Game(num_players)
        loser_hist[game.run()] += 1

    print(loser_hist)


if __name__ == '__main__':
    main()

