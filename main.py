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

#used google AI to find this code to verify pygame is working
# import pygame
# pygame.init()
# screen = pygame.display.set_mode((400, 300))
# pygame.display.set_caption("Pygame in VS Code")
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
# pygame.quit()

import random
import time

#-----Class: Player-----
class Player:
    def __init__(self):
        self.coins = 10
        self.score = 0
    
    def add_coins(self, amount):
        self.coins += amount
    
    def add_score(self, amount):
        self.score += amount

#-----Class: Gumball-----
class Gumball:
    def __init__(self, color, effect):
        self.color = color
        self.effect = effect

#-----Class: GumballMachine-----
class Machine:
    def __init__(self):
        self.gumballs = [
            Gumball("Yellow", self.give_coins),
            Gumball("Blue", self.lose_coins),
            Gumball("Red", self.small_score),
            Gumball("Green", self.big_score)
        ]
    
    def dispense(self):
        return random.choice(self.gumballs)

#-----Effects-----
    def give_coins(self, player):
        player.add_coins(3)
        print("You gained 3 coins!")
    
    def lose_coins(self, player):
        player.add_coins(-2)
        print("You lost 2 coins!")
    
    def small_score(self, player):
        player.add_score(10)
        print("Score increased by 10!")

    def big_score(self, player):
        player.add_score(20)
        print("Score increased by 20!")

#-----File I/O----- (USED AI TO HELP FIX ERRORS I COULDNT SEE)
def load_high_score():
    try:
        with open("highscore.txt", "r") as f:
            return int(f.read())
    except:
        return 0
    
def save_high_score(score):
    with open("highscore.txt", "w") as f:
        f.write(str(score))

#-----UI and display / extra ideas-----
def show_title():
    print("=" * 50)
    print("TEST YOUR LUCK WITH THE GUMBALL GAME".center(50))
    print("=" * 50)
    print("Enter a coin to collect points,")
    print("but be weary of running out of coins!\n")

def show_stats(player, rounds):
    print("-" * 50)
    print(f"Coins: {player.coins}   Score: {player.score}   Round: {rounds}/20")
    print("-" * 50)

def show_gumball(color):
    print("\n The Machine is about to dispense a gumball!")
    time.sleep(1)
    print(f"A {color} gumball was dispensed!")














#------Game loop-----
def main():
    while True:

        player = Player()
        machine = Machine()
        rounds = 0
        high_score = load_high_score()

        print("Welcome to my Game!")
        print(f"High Score: {high_score}\n")

        while player.coins > 0 and rounds < 20:
            input("Press ENTER to play... COST: 1 coin")

            player.add_coins(-1) #have to pay coins to play
            gumball = machine.dispense()

            print(f"\nYou got a {gumball.color} gumball!")
            gumball.effect(player)

            print(f"Coins: {player.coins} - Score: {player.score}\n")

            rounds += 1

    #-----game over-----

        print("Game Over!")
        print(f"Final Sore: {player.score}")

        if player.score > high_score:
            print("NEW HIGH SCORE!!!")
            save_high_score(player.score)
        else:
            print(f"Current High Score is: {high_score}")

    #-----play again----- (HAD AI HELP ME FIX BROKEN LOOP WHERE ELSE: SECTION WOULD PRINT AND STILL RESTART THE GAME EVEN IF 'Y' OR 'N' WASNT INPUTTED)

        while True:
            choice = input("\nPlay Again? (y/n): ").lower()
            if choice in ['y', 'yes']:
                break
            elif choice in ['n', 'no']:
                print("Thanks for Playing!")
                exit()
            else:
                print("Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()