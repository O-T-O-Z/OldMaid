# The Old Maid Logic Project
This is the GitHub repository of our Logical Aspects of Multi-Agent Systems project into the card game "The Old Maid".

This project is done by Andreea Tudor, Nora Majeris, and Ömer Tarik Özyilmaz (group 2).

## How to run
First, install the requirements:
```shell
pip install -r requirements.txt
```

To run the code, follow the example below.
```shell
python main.py [-h] [--num_players NUM_PLAYERS] [--condition CONDITION] [--num_experiments NUM_EXPERIMENTS]

options:
  -h, --help            show this help message and exit
  --num_players number of players to play the game with (>=3)
  --condition The game has 3 conditions:
    0: basic logical agent vs random agents
    1: epistemic agent vs random agents
    2: epistemic agent vs basic logical agents
  --num_experiments number of experiments to run
```