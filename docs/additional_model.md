---
layout: page
title: Additional Model
permalink: /additional_model/
---

## Simplifications
- We will focus on 3 players and 3 types of cards.

Compared to the model in **Model**, here we don't keep track of the position of the cards in the deck,
and we assume the cards are shuffled after each round. 

## Knowledge representation
### Possible worlds
Each possible world is defined by all possible combination of cards in the hands of the players. For instance, the following worlds are possible:

- Player 1 has a Jack, Player 2 has a Queen, Player 3 has a King
- Player 1 has a Jack, Player 2 has a King, Player 3 has a Queen
- Player 1 has a Queen and a King, Player 2 has 2 Jacks, Player 3 has a Queen
- etc.

### Accessibility relations
Every player knows in every state the number of cards in the hands of every player 
(including themselves). Therefore, only worlds in which the number of cards in the hands of the players is the same are accessible.

The players also know their own cards. Hence, only the worlds in which the cards in their own hands are the same are accessible. 

Once a player draws a card, both the player who drew the card and the player who gave the card know the card that was drawn. Hence, only worlds in which the player who drew the card has the card in their hand are accessible.

Lastly, when a card is discarded, all players know the card that was discarded. Hence, only worlds in which the discarded cards are not part of the hands of the players are accessible.

## Inference
At each step of the game, the agents will use the knowledge they have to infer new knowledge. For instance, if there is an accessible world in which another player has two Queens, but the cards are not discarded, then that world is not possible. Hence, the agent can infer that the other player does not have two Queens.

Similarly, if a player B draws a card from a player A and does not discard those in the next step, then player A, who gave the card, knows not only that player B has the card, but also that they only have one of that type. However, in a future round, if another player draws a card from player B, player A will not know which them has the card that was drawn from A, hence new worlds will be accessible for player A.

## Research question
In our study we would then want to investigate whether adding epistemic announcements carries useful information for an agent to perform better in the game of Old Maid.


## Experiments
We will perform multiple experiments in which we play epistemic agents against random players, as well as against non-epistemic logical agents.
