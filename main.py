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
#####################################################
# Resources Used:
#https://python-text-adventure.readthedocs.io/en/latest/part3.html#next-up
#https://www.youtube.com/watch?v=FfWpgLFMI7w
#https://chatgpt.com/
#https://www.youtube.com/watch?v=Qj3GlL5ckQA
#https://www.w3schools.com/python/
#https://www.youtube.com/watch?v=dpioxiTTAeo
#####################################################

import random
import time

#-----COLORS FOR TERMINAL----- USED VIDEO IN THE RESOURCE SECTION FOR THIS

class Colors:
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

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
        print(f"{Colors.GREEN} You gained 3 coins!{Colors.RESET}")
    
    def lose_coins(self, player):
        player.add_coins(-2)
        print(f"{Colors.RED} You lost 2 coins!{Colors.RESET}")
    
    def small_score(self, player):
        player.add_score(10)
        print(f"{Colors.YELLOW} Score increased by 10!{Colors.RESET}")

    def big_score(self, player):
        player.add_score(20)
        print(f"{Colors.BLUE} Score increased by 20!{Colors.RESET}")

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
    print(Colors.BOLD + "=" * 50)
    print("TEST YOUR LUCK WITH THE GUMBALL GAME".center(50))
    print("=" * 50 + Colors.RESET)
    print("Enter a coin to collect points,")
    print("but be weary of running out of coins!\n")

def show_stats(player, rounds):
    print("-" * 50)
    print(f"Coins: {player.coins}   Score: {player.score}   Round: {rounds}/20")
    print("-" * 50)

def show_gumball(color):
    print("\n The Machine is about to dispense a gumball!")
    time.sleep(1)

    if color == "Yellow":
        print(f"{Colors.YELLOW} A Yellow gumball was dispensed!{Colors.RESET}")
    elif color == "Blue":
        print(f"{Colors.BLUE} A Blue gumball was dispensed!{Colors.RESET}")
    elif color == "Red":
        print(f"{Colors.RED} A Red gumball was dispensed!{Colors.RESET}")
    elif color == "Green":
         print(f"{Colors.GREEN} A Green gumball was dispensed!{Colors.RESET}")

def game_over(player, high_score):
    print("\n" + "=" * 50)
    print("GAME OVER".center(50))
    print("=" * 50)
    print(f"Final Score: {player.score}")

    if player.score > high_score:
        print("NEW HIGHSCORE!!!")
    else:
        print(f"High Score: {high_score}")

#------Game loop part 1-----

def main():
    playing = True

    while playing:
        player = Player()
        machine = Machine()
        rounds = 0
        high_score = load_high_score()

        show_title()
        print(f"High Score: {high_score}\n")

    #------GAME LOOP part 2-----

        while player.coins > 0 and rounds < 20:
            input("Press ENTER to play... COST: 1 coin")

            player.add_coins(-1) #have to pay coins to play
            gumball = machine.dispense()

            show_gumball(gumball.color)
            gumball.effect(player)

            rounds += 1
            show_stats(player, rounds)

    #-----THE END-----

        game_over(player, high_score)

        if player.score > high_score:
            save_high_score(player.score)

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