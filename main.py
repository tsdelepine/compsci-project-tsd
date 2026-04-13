'''
#NOTES: feedback from class
Smart decision to scale down from the roguelike concept. The gumball machine game has clear, achievable mechanics and a well-defined scope.
Pygame is a good choice for this kind of visual, interactive project. The color-based gumball effects (yellow for coins, blue for 
losing coins, red/green for points) give you clear game logic to implement.

To strengthen your scope, incorporate classes (Gumball, Machine, Player), file I/O for high score persistence, and organize your code with 
functions for each game mechanic (dispensing, scoring, coin management).

The 20-round structure gives you a clear game loop to work with. Consider adding visual polish (animations, sound effects) as stretch goals 
after the core mechanics work.
'''

import random

#Class: Player
class Player:
    def __init__(self):
        self.coins = 10
        self.score = 0
    
    def add_coins(self, amount):
        self.coins += amount
    
    def add_score(self, amount):
        self.score += amount