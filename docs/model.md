---
layout: page
title: Model
permalink: /model/
---

## Knowledge representation
### All legal worlds
Each legal world is defined by all possible combination of cards in the hands of the players.
A player cannot possess two instances of the same card without discarding them.
For instance, in a game state where there are three players, 5 cards in the game,
namely two Jacks, two Kings and a Queen, and 
Player 1 has two cards, Player 2 has two cards, and Player 3 has one card, the following
worlds are legal:

- Player 1 has a Jack and a Queen, Player 2 has a Jack and a King, Player 3 has a King
- Player 1 has a King and a Queen, Player 2 has a Jack and a King, Player 3 has a Jack
- Player 1 has a Jack and a King, Player 2 has a Jack and a King, Player 3 has a Queen
- Player 1 has a Jack and a King, Player 2 has a Jack and a Queen, Player 3 has a King
- Player 1 has a Jack and a King, Player 2 has a King and a Queen, Player 3 has a Jack

### Possible worlds per player
From each world, each player has a set of accessible worlds, which are the worlds 
that the player considers possible if the first world was the true state. 
Possible worlds are defined as the set of legal worlds in which the player has the same cards as in their hand.
An agent cannot differentiate between two worlds in which they have the same hand without
additional knowledge. However, since they know their own hand, the model can be restricted
to only the worlds in which the player has the same hand. The player's goal is to reason about the true state. They know what their hand is in the true state, meaning they can narrow down the set of possible worlds by only considering those in which their hand is correct.

By these means, assuming the true hand of Player 1 in the example above is a Jack and a King,
the possible worlds for Player 1 are:
- Player 1 has a Jack and a King, Player 2 has a Jack and a King, Player 3 has a Queen
- Player 1 has a Jack and a King, Player 2 has a Jack and a Queen, Player 3 has a King
- Player 1 has a Jack and a King, Player 2 has a King and a Queen, Player 3 has a Jack

However, in the same example, if the hand of Player 2 is a Jack and a Queen, then the possible worlds for Player 2 are:
- Player 1 has a Jack and a King, Player 2 has a Jack and a Queen, Player 3 has a King


### Accessibility relations
Every player knows in every state the number of cards in the hands of every player 
(including themselves). Therefore, only worlds in which the number of cards in the
hands of the players is the same, are accessible.

The players also know their own cards. Hence, only the worlds in which the cards in 
their own hands are the same are accessible. 

Once a player draws a card, both the player who drew the card and the player who gave 
the card know the card that was drawn. Hence, only worlds in which the player who drew 
the card has the card in their hand are accessible for the drawing player and the giving player.

Lastly, when a card is discarded, all players know the card that was discarded. 
Hence, only worlds in which the discarded cards are not part of the hand of the player that discarded the card, are accessible.

## Incorporating knowledge
At each step of the game, the agents use the knowledge they have to infer new knowledge. 
For instance, if there is an accessible world in which another player has two Queens, 
but the cards are not discarded, then that world is not legal. Hence, the agent can 
infer that the other player does not have two Queens. Moreover, whenever a set of cards
is discarded, the legal worlds are updated to exclude those cards from the hands of the players.
By these means, discarding cards is implemented as a public announcement[^2].

When an agent announces what pair of cards is discarded, which is always truthful,
the Kripke model is updated to exclude those cards from the hands of the players.
Moreover, the other agents can infer that the agent who discarded the cards does not have
that type of card in their hand. For instance, consider a game state where
Player 1 draws a card from Player 2, and the other players do not have any knowledge about
the cards in the hands of Player 1 and Player 2. If Player 1 discards a pair of Kings, 
then the other players now know that neither Player 1 nor Player 2 have a King in their hands anymore. 


We define two types of knowledge that different agents can use, namely basic logical knowledge
and epistemic knowledge. 

### Basic Logical Knowledge
The basic logical knowledge is the knowledge that can be inferred
from the game rules, as described above. It is different for each player, and it is inferred
whenever a player is involved in a game action. For instance, if a Player B draws a card from a Player A and does not discard those 
in the next step, then Player A, who gave the card, knows not only that Player B 
has the card, but also that they only have one of that type. At the same time, Player B also now knows
that Player A does not have the card that was drawn in their hand, otherwise it would have
already been discarded. However, in a future round, 
if another player draws a card from Player B, Player A will not know which of them 
has the card that was drawn from A, hence the knowledge is updated, while new worlds become possible for Player A.

### Epistemic Knowledge
The epistemic knowledge is the knowledge that is inferred from the actions of the other players.
The agents using this knowledge type can infer the knowledge of the other players, even when
they are not involved in a game action. For instance, if a Player A draws a card from Player B,
another Player C can infer the knowledge both Player A and Player B have about the card that was drawn.
Since the card type is unknown, the knowledge about the other agents' new knowledge is 
represented by a set of disjunctions, one for each possible card type. To this end, we make use of the $K_i$ operator, as well as the disjunction connective to represent epistemic sentences. Whenever a card trade happens between two agents, and the drawing player does not discard the card, every player not involved in the trade is able to determine that the giving player knows that the receiving player has that card, and that the receiving player knows that the giving player does not have that card. Combined with other knowledge, it may be possible that these facts may help narrow down the list of possible worlds, as well as allow the agents to make use of the full Kripke model.

## Agents and strategies
### Random Player
A random player always chooses another random player, and a random card is drawn from their hand.
This player does not use any knowledge about the game, and is used as a baseline for the other players.

### Logic Player
This player type follows a logical approach during the game. Namely, it uses the basic logical knowledge
it has about the game, as described above, to make decisions about which player to choose when its turn comes.
The strategy involved is to choose the player that is most likely to have the most number of cards in their hand
that the agent currently has in the hand. This way, the agent maximizes the chances of drawing a card
such that a pair can be immediately discarded. This is implemented by counting the number of common cards
of each agent in each possible world, and choosing the agent with the highest number of common cards.
If there are multiple agents with the same number of common cards, then the agent chooses the one with the
highest number of cards in their hand. A random card is then drawn from this chosen player.

### Epistemic Player
This type of player follows the same approach as the Logic Player, but it also uses the epistemic knowledge
described above to make decisions. Namely, it uses the knowledge of the other players to infer new knowledge,
and then further uses it when it is time to choose a player to draw a card from. A random card is then drawn from this chosen player.

## Game run
Let us consider a game with 3 players, 4 card types, as follows:
- Player 1 is an Epistemic Player
- Players 2 and 3 are a Logic Player
- the deck contains 4 Aces, 4 Jacks, 3 Queens, and 4 Kings

As the game starts, the deck is shuffled, and the cards are dealt to the players.
Then, the players can immediately discard any pairs they have in their hands:
```
Player 2 discarded a pair of J
Player 1 discarded a pair of K
Player 0 discarded a pair of Q
Player 1 discarded a pair of A
Player 2 discarded a pair of A
```
Since two pairs of Aces were discarded, this card type is no longer in the deck.
Then, the game starts, and the players take turns in drawing a card from another player.
The order of the players is determined randomly at the beginning of the game, 
and Player 2 is the first to draw a card:
```
Accessible worlds: [{0: {'K', 'Q', 'J'}, 1: {'J'}, 2: {'K'}}]
All worlds:
{0: {'K', 'Q', 'J'}, 1: {'J'}, 2: {'K'}}
{0: {'K', 'Q', 'J'}, 1: {'K'}, 2: {'J'}}
Cards common with: {0: 1, 1: 0}
Target player: 0
Player 2 received a J from player 0
Knowledge of player 0:
2 has J
Knowledge of player 1:
Knowledge of player 2:
~(0 has J)
```
The accessible worlds are restricted by the number of cards in each player's hand,
as well as the number of each card type in the deck. Player 0 has 3 cards,
and there are only 3 different card types in the game, hence the hand of player 0 
is known to be {K, Q, J}. While player 0 cannot yet distinguish between the worlds
in which Player 1 has a King and Player 2 has a King, Players 1 and 2 can, as they know 
their own hand. Hence, Player 2 chooses player 0 to draw a card from, as they have 
a higher chance of drawing a card that is in their hand. The card drawn is a Jack.

Then, the knowledge of the players is updated, as Player 0 now knows that Player 2 has a Jack,
and Player 2 knows that Player 0 does not have a Jack. Player 1 is a Logic Player, hence
they do not use the epistemic knowledge, and their knowledge remains unchanged.

The game continues, and it's player 0's turn to draw a card:
```
Accessible worlds: [{0: {'K', 'Q'}, 1: {'J'}, 2: {'K', 'J'}}]
All worlds:
{0: {'K', 'Q'}, 1: {'J'}, 2: {'K', 'J'}}
{0: {'K', 'J'}, 1: {'Q'}, 2: {'K', 'J'}}
{0: {'K', 'J'}, 1: {'K'}, 2: {'Q', 'J'}}
{0: {'K', 'J'}, 1: {'J'}, 2: {'K', 'Q'}}
{0: {'Q', 'J'}, 1: {'K'}, 2: {'K', 'J'}}
Cards common with: {1: 0, 2: 1}
Target player: 2
Player 0 received a K from player 2
Player 0 discarded a pair of K
Knowledge of player 0:
2 has J
~(2 has K)
Knowledge of player 1:
~(0 has K)
~(2 has K)
Knowledge of player 2:
~(0 has J)
~(0 has K)
```
At this state of the game, there are 2 Jacks, two Kings, and one Queen left. Since
Player 0 has a King and a Queen, and Player 2 has one card, while Player 1 has two cards,
it is known to Player 0 that Player 2 has a King and a Jack, and Player 1 has a Jack
(Player 2 would have discarded the cards if they were two Jacks). Given that there 
is only one accessible world for Player 0, they choose Player 2 to draw a card from,
as they have one type of card in common, while Player 1 has none.

Then, the knowledge of the players is updated. After receiving the King from Player 2,
Player 0 can now infer that Player 2 does not have a King anymore. Player 1 can observe
the action of Player 0 (discarding a pair of Kings), and infer that Player 2 does not have a King anymore, as well as Player 0.
Player 2 can infer that Player 0 does not have a King anymore as well.

The game continues until two of the three players have no cards left in their hands.
Then, the game ends, and the player left with the Queen (Old Maid) loses the game.

## Experimental setup
In order to test whether the epistemic knowledge is useful in the game, we run a series of experiments.
Namely, each experiment consists of 5000 games, and the number of wins for each player type is recorded.
Each experiment is repeated 5 times for randomness (different seeds).

The conditions of the experiments are the following:
- a basic logical player against two random players
- an epistemic player against two random players
- an epistemic player against two logical players

The cards are shuffled before each game, and the starting player is determined randomly.

## Tools
### Code Structure
The model is implemented in Python 3.10, and the code can be found under the `src` directory. 
The world in the Kripke model is defined in the `World` class, in the `logic_utils/world.py` file,
and the implementation of the logical sentences, atomic sentences, and the logical operators can be found
in the `logic_utils/formulas.py` file. 

The `players` directory contains the implementation of the three player types, as well as the `Player` class.
The remaining files in the `src` directory contain the implementation of the game and model, and the code for running
the experiments. More information on running the code, can be found in the README of the [GitHub repository](https://github.com/O-T-O-Z/OldMaid).

### Communication Tools
The communication between the team members was done via Discord, and the code was shared via GitHub.
The CodeWithMe extension was used for pair programming in Microsoft Visual Studio Code.

[^2]: [Ditmarsch, Hans van, et al. *Dynamic Epistemic Logic*. Springer, 2007.](https://rug.on.worldcat.org/oclc/187994683)