---
layout: page
title: Game
permalink: /game/
---

## Introduction
The Old Maid is a card game that dates back to at least 1821[^1]. The goal of the game is to discard all the cards in one's hand by forming pairs of cards which can be discarded. However, there is one odd card, resulting from either removing a queen or jack of clubs or by adding a Joker card. The player that is left with the odd card at the end of the game is called the "old maid" and is the loser of the game. The game can be played with two or more players. 
![asd](/assets/img/cards.jpg)

## Research question
In our study we would then want to investigate whether adding epistemic announcements carries useful information for an agent to perform better in the game of Old Maid.

## Rules

The rules of the game are as follows:
- A deck of cards is shuffled and either one queen/king/random card is removed or a Joker card is added.
- The deck is distributed evenly accross all players.
- A player must discard pairs of cards, matching the number/type of the card.
- A player cannot discard more than two matching cards.
- Discarded pairs must be displayed face-up in front of the player, visible to other players.
- Each turn, a player must draw a random card from the player on the left.
- Players without cards in their game leave the game.
- The player left with the unmatchable card is the "old maid" and is the loser of the game.

## Simplifications
- We will focus on 3 players and 4 types of cards.
- We assume the cards are shuffled after each round. 
- We choose the player to pick from, rather than picking from a fixed player to implement strategy.

## Example
An example run is illustrated below.
1. Take a game with three types of cards (2, 3, and Queen), each card type being repeated four times, except the queen which is repeated three times.
2. Player 1 receives 1x2, 3x3 and 1xQueen, Player 2 receives 3x2, 1x3, and 2xQueen.
3. Player 1 discards their pair of 3's and is left with [2, 3, Queen].
4. Player 2 discards their pair of 2's and their pair of Queens, being left with [2, 3].
5. Player 1 presents their cards to Player 2, who randomly picks the Queen.
6. Both Players now know that the Queen is in Player 2's hand, and since both cannot form a pair, they know each other's full hand. Player 1 has [2, 3] and Player 2 has [2, 3, Queen].
7. Player 2 now presents their cards to Player 1, who randomly picks the 2.
8. Player 1 discards their pair of 2's, being left with [3].
9. Player 1 presents their cards to Player 2, who picks the remaining 3.
10. Player 2 discards their pair of 3's, being left with just the Queen. 
11. Player 1 has lost all their cards and leaves the game.
12. Player 2 is left with the unmatchable card and is thus the "Old Maid".


[^1]: [Old maid (card game) - Wikipedia](https://en.wikipedia.org/wiki/Old_maid_(card_game))