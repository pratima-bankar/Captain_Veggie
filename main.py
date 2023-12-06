# Author Name: Pratima Bankar, Shiva Raj Harinath Reddy , Preethi Gutha
# Date: 12/04/2023
# Description: The program below depicts the main file where all the classes are initialized.

from GameEngine import GameEngine


def main():
    game_system = GameEngine()
    game_system.initializeGame()
    game_system.intro()
    remain_veg = game_system.remainingVeggies()
    while remain_veg != 0:
        print(f"{remain_veg} veggies remaining. Current Score: {game_system.getScore()}")
        game_system.printField()
        game_system.moveRabbits()
        game_system.moveCaptain()
        game_system.moveSnake()
        remain_veg = game_system.remainingVeggies()
    game_system.gameOver()
    game_system.highScore()


main()
