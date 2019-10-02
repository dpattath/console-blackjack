# Basic blackjack for console

This project was meant to quickly highlight a simple card game done in approximately 2 hours.

The card game is single player and starts the player off with a balance of $100, which can be fine tuned.

It follows the major rules of blackjack, but does not go too deeply into splitting pairs, doubling down, etc.

# Design

Before writing any of the code, I decided how I wanted to choose cards randomly and assign cards their values.

The main game loop would be deciding a betting value, determining whether there are immediate wins from the dealt hands, and then, going through the player's hits or stand.

I didn't require any extensive data structure usages, most of the logic was translated into checks and cards were represented in lists with their values in a dict.

# Future plans

I would like to go into the deeper features of blackjack, specifically splitting pairs, doubling down, and insurance. Finer details such as the actual randomization of cards could be slightly different if we followed the six deck style many casinos use.

I would like to ideally have this as a multiplayer game so that multiple people could go against the dealer on their own.
