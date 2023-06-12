---
layout: page
title: Model
permalink: /model/
---


## Simplifications
There are a couple of simplifications that have to be considered when modeling the Old Maid card game in the context of epistemic logic. To investigate whether the use of higher-order knowledge can be advantageous to not using this knowledge, we assume the following:
- Knowledge agents can keep track of the hands of the players in the game.
- Agents will not shuffle their hand, so each agent will be able to keep track of a unique card identifier for each card, even if they do not know its value.
- We will focus on 3 players and 3 types of cards first.

## Knowledge representation
We intend to represent an agent's knowledge by first-order sentences which connect to a unique card identifier to its value. Therefore, an atomic sentence in our model would take the form Is(x, y), where x is a card identifier, and y is a card value. The number of atomic sentences in our model would therefore be _n_*_m_, where _n_ is the number of cards, and _m_ is the number of card values. Unique combinations of these atoms being true would then define unique worlds. However, due to how the decks are constructed, not all combinations are possible, reducing the number of possible worlds significantly.

Agents would also be able to know composite sentences based on events that happen during the course of the game.

## How we use inference
Our current idea is for agents to remember knowledge of atoms, together with some complex sentences, and use these to infer other relevant sentences. Our current intention is to consider relevant atomic sentences the agent does not yet know, and put their negation along with the known sentences, and solve for satisfiability via the tableaux method.

### Example:
Consider a game with 2 card types: Jack and Queen (formally, for all card identifiers x: Is(x, queen) v Is(x, jack)). Player 1 has a Jack, and must draw another one to win the game. They do not know any of the other players' cards. They then observe that PLayer 2 draws a card from Player 3, and subsequently discards two queens. Player 2 still has a card, specifically one with card identifier 1. The discard declares that it is not the case that Is(1, Queen).

Player 1 is curious to know where it can find a Jack, so it will inquire for card IDs it does not know the value of, whether the card is a Jack. It will want to know if it is the case that Is(1, jack). It will put its knowledge, and the negation of its goal in a conjunction, and see if the sentence is satisfiable. In other words, it will solve the tableau with the initial list:
- Is(1, Queen) v Is(1, Jack)
- not Is(1, Queen)
- not Is(1, Jack)

It will see that the conjunction is not satisfiable, and conclude that Is(1, Jack), draw that card, and win the game.

Epistemic sentences can be announced as well. For example, when an agent takes a card from another agent, that agent will know that the other agent also knows that card.

## Research question
In our study we would then want to investigate whether adding epistemic announcements carries useful information for an agent to perform better in the game of Old Maid.


## Experiments
We will perform multiple experiments in which we play epistemic agents against random players, as well as against non-epistemic logical agents.
