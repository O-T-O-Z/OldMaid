import argparse
from tqdm import tqdm

from game import Game

PROGRESS_PERIOD = 50

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--num_players", type=int, default=3)
    parser.add_argument("--condition", type=int, default=0)
    parser.add_argument("--num_experiments", type=int, default=1)
    
    return parser.parse_args()


def main():
    args = parse_args()
    assert args.num_players >= 3, "Must have at least 3 players"
    print(f"Playing {args.num_experiments} games with {args.num_players} players in condition {args.condition}")

    loser_hist = [0] * args.num_players
    # we do not wish to print too much if we do many experiments
    verbose = True if args.num_experiments == 1 else False
    for exp in tqdm(range(args.num_experiments)):
        game = Game(args.num_players, condition=args.condition, verbose=verbose)
        loser_hist[game.run()] += 1

    print(f"Main player loss rate: {loser_hist[0] / float(args.num_experiments)}")
    print(f"Loser histogram: {loser_hist}")


if __name__ == '__main__':
    main()

