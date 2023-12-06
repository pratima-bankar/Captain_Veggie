# Author Name: Pratima Bankar, Shiva Raj Harinath Reddy , Preethi Gutha
# Date: 12/04/2023
# Description: Program that controls the main gaming and movement of rabbit, captain , snake and veggies.

# Importing all the files required

from Veggie import Veggie
from Captain import Captain
from Rabbit import Rabbit
from Snake import Snake
import os
import csv
import random
import pickle


class GameEngine:
    __NUMBEROFVEGGIES = 30
    __NUMBEROFRABBITS = 5
    __HIGSCOREFILE = "highscore.data"

    def __init__(self):
        self._field_matrix = []
        self._rabbits = []
        self._captain = None
        self._snake = None
        self._veg = []
        self._score = 0

    def initVeggies(self):
        """
        Function to get the name of veggie file, field size, and Veggie objects
        :return:
        """

        # Inputting file name and check if the file exists if not prompt user for correct file name
        while True:
            file_name = input("Please enter the name of the vegetable point file: ")
            if os.path.exists(file_name):
                break
            else:
                print(f"{file_name} does not exist!", end=" ")

        # Opening a file and reading in the lines.
        with open(file_name, 'r') as file:
            file = csv.reader(file)

            line = next(file)
            rows = int(line[1])
            cols = int(line[2])

            # Setting field 2D list
            self._field_matrix = [[None] * cols for i in range(rows)]

            # Getting veggies list
            for row in file:
                new_veggie = Veggie(row[0], row[1], int(row[2]))
                self._veg.append(new_veggie)
            max_veg = len(self._veg)

            # Randomly choosing location for veggie object.
            for i in range(self.__NUMBEROFVEGGIES):
                random_veg = random.randint(0, max_veg - 1)
                temp = True
                while temp:
                    random_field_r = random.randint(0, rows - 1)
                    random_field_c = random.randint(0, cols - 1)
                    if self._field_matrix[random_field_r][random_field_c] is None:
                        self._field_matrix[random_field_r][random_field_c] = self._veg[random_veg]
                        temp = False

    def initCaptain(self):
        """
        Function to randomly assign location to Captain object
        """
        temp = True
        while temp:
            random_field_r = random.randint(0, len(self._field_matrix) - 1)
            random_field_c = random.randint(0, len(self._field_matrix[0]) - 1)

            if self._field_matrix[random_field_r][random_field_c] is None:
                new_captain = Captain(random_field_r, random_field_c)
                self._field_matrix[random_field_r][random_field_c] = new_captain
                self._captain = new_captain
                temp = False

    def initRabbits(self):
        """
        Function for choosing random location for NUMBEROFRABBITS
        """
        for i in range(self.__NUMBEROFRABBITS):
            temp = True
            while temp:
                random_field_r = random.randint(0, len(self._field_matrix) - 1)
                random_field_c = random.randint(0, len(self._field_matrix[0]) - 1)

                if self._field_matrix[random_field_r][random_field_c] is None:
                    new_rabbit = Rabbit(random_field_r, random_field_c)
                    self._field_matrix[random_field_r][random_field_c] = new_rabbit
                    self._rabbits.append(new_rabbit)
                    temp = False

    def initSnake(self):
        """
        Function to initiate Snake object and assign a random slot to the snake object
        """
        temp = True
        while temp:
            random_field_r = random.randint(0, len(self._field_matrix) - 1)
            random_field_c = random.randint(0, len(self._field_matrix[0]) - 1)
            if self._field_matrix[random_field_r][random_field_c] is None:
                x = Snake(random_field_r, random_field_c)
                self._field_matrix[random_field_r][random_field_c] = x
                self._snake = x
                temp = False

    def initializeGame(self):
        """
        Function for initializing the fame and calling the Veggies, Captain, rabbits and Snake function
        """
        self.initVeggies()
        self.initCaptain()
        self.initRabbits()
        self.initSnake()

    def remainingVeggies(self):
        """
        Function to count number of veggies still remaining in the game
        :return: Number of veggies still remaining in the game
        """
        veggie_count = 0
        for row in self._field_matrix:
            for cell in row:
                if cell is not None:
                    if cell.getsymbol() not in ["R", "V", "S"]:
                        veggie_count += 1
        return veggie_count

    def intro(self):
        """
        Function to display Introduction in the start of the game.
        """
        print('''Welcome to Captain Veggie!
The rabbits have invaded your garden and you must harvest
as many vegetables as possible before the rabbits eat them
all! Each vegetable is worth a different number of points
so go for the high score!

The vegetables are:''')
        for i in self._veg:
            print(i)

        print(f"\nCaptain Veggie is {self._captain.getsymbol()}, and the rabbits are R's.")
        print("\nGood Luck!")

    def printField(self):
        """
        Function to print the field in dimension
        """
        border = "#" * (len(self._field_matrix[0]) * 3 + 2)

        print(border)

        for row in self._field_matrix:
            print("#", end="")
            for item in row:
                print(f"{item.getsymbol():^3}" if item is not None else "   ", end="")
            print("#")

        print(border)

    def getScore(self):
        """
        Function to get the score
        """
        return self._score

    def moveRabbits(self):
        """
        Function to randomly move rabbit
        :return:
        """
        for rabbit in self._rabbits:
            rows = len(self._field_matrix)
            cols = len(self._field_matrix[0])
            row, col = rabbit.getXY()
            action = random.randint(0, 3)

            new_row = 0
            new_col = 0
            if action == 0:
                new_row = max(row - 1, 0)
                new_col = col
            elif action == 1:
                new_row = min(row + 1, rows - 1)
                new_col = col
            elif action == 2:
                new_col = max(col - 1, 0)
                new_row = row
            elif action == 3:
                new_col = min(col + 1, cols - 1)
                new_row = row

            if row != new_row or col != new_col:
                if self._field_matrix[new_row][new_col] is None or self._field_matrix[new_row][new_col].getsymbol() not in ["V", "R", "S"]:
                    rabbit.setXY(new_row, new_col)
                    self._field_matrix[row][col] = None
                    self._field_matrix[new_row][new_col] = rabbit

    def moveCptVertical(self, move):
        """
        Function to move captain C vertical in an empty slot
        :param move: variable representing the vertical movement of captain
        """
        x, y = self._captain.getXY()
        max_row = len(self._field_matrix)

        new_row = 0

        if move.lower() == "w":
            new_row = max(x - 1, 0)
        elif move.lower() == "s":
            new_row = min(x + 1, max_row - 1)

        if x != new_row:
            if self._field_matrix[new_row][y] is None:
                self._captain.setXY(new_row, y)
                self._field_matrix[x][y] = None
                self._field_matrix[new_row][y] = self._captain
            elif self._field_matrix[new_row][y].getsymbol() != "R" and self._field_matrix[new_row][y].getsymbol() != "S":
                self._captain.setXY(new_row, y)
                self._field_matrix[x][y] = None
                self._score += self._field_matrix[new_row][y].getPoints()
                print(f'Yummy! A delicious {self._field_matrix[new_row][y].getName()}')
                self._captain.addVeggie(self._field_matrix[new_row][y])
                self._field_matrix[new_row][y] = self._captain
            else:
                if self._field_matrix[new_row][y].getsymbol() == "R":
                    print("Don't step on the bunnies!")
                else:
                    print("Don't step on the Snake!")
        else:
            print("You can't move that way!")

    def moveCptHorizontal(self, move):
        """
        Function to move the captain horizontal in an empty slot
        :param move: variable representing the horizontal movement of captain
        """
        x, y = self._captain.getXY()
        max_col = len(self._field_matrix[0])

        new_col = 0

        if move == "A" or move == "a":
            new_col = max(y - 1, 0)
        elif move == "d" or move == "D":
            new_col = min(y + 1, max_col - 1)
        if y != new_col:
            if self._field_matrix[x][new_col] is None:
                self._captain.setXY(x, new_col)
                self._field_matrix[x][y] = None
                self._field_matrix[x][new_col] = self._captain
            elif self._field_matrix[x][new_col].getsymbol() != "R" and self._field_matrix[x][new_col].getsymbol() != "S":
                self._captain.setXY(x, new_col)
                self._field_matrix[x][y] = None
                self._score += self._field_matrix[x][new_col].getPoints()
                print(f'Yummy! A delicious {self._field_matrix[x][new_col].getName()}')
                self._captain.addVeggie(self._field_matrix[x][new_col])
                self._field_matrix[x][new_col] = self._captain
            else:
                if self._field_matrix[x][new_col].getsymbol() == "R":
                    print("Don't step on the bunnies!")
                else:
                    print("Don't step on the Snake!")
        else:
            print("You can't move that way!")

    def moveCaptain(self):
        """
        Function to get user input in which direction Captain object should move
        """
        move = input("Would you like to move up(W), down(S), left(A), or right(D):")

        if move in ["W", "w", "S", "s"]:
            self.moveCptVertical(move)
        elif move in ["A", "a", "D", "d"]:
            self.moveCptHorizontal(move)
        else:
            print(f"{move} is not a valid option.")

    def moveSnake(self):
        """
        Function to move snake object in random direction
        """
        captain_x, captain_y = self._captain.getXY()
        snake_x, snake_y = self._snake.getXY()
        move = random.randint(0, 1)

        new_snake_x = 0
        new_snake_y = 0

        # Condition that the snakes always tries to move towards the captain
        if move == 0:
            if captain_x > snake_x:
                new_snake_x = snake_x + 1
                new_snake_y = snake_y
            elif captain_x < snake_x:
                new_snake_x = snake_x - 1
                new_snake_y = snake_y
            else:
                move = 1

        if move == 1:
            if captain_y > snake_y:
                new_snake_y = snake_y + 1
                new_snake_x = snake_y
            else:
                new_snake_y = snake_y - 1
                new_snake_x = snake_y

        if new_snake_x == captain_x and new_snake_y == captain_y:
            for i in range(min(len(self._captain._veggies), 5)):
                v = self._captain._veggies.pop()
                if v is not None:
                    self._score -= v.getPoints()
            self._field_matrix[snake_x][snake_y] = None
            print("Snake Bite! You Lost 5 Veggies")
            self.initSnake()
        elif self._field_matrix[new_snake_x][new_snake_y] is None:
            self._field_matrix[snake_x][snake_y] = None
            self._snake.setXY(new_snake_x, new_snake_y)
            self._field_matrix[new_snake_x][new_snake_y] = self._snake

    def gameOver(self):
        """
        Function to print the score and print that the game is completed
        """
        print("GAME OVER!")
        print("You managed to harvest the following vegetables:")
        for i in self._captain.getVeggie():
            print(i.getName())
        print(f'Your score was: {self._score}')

    def highScore(self):
        """
        Function to get the users high score and store it in this highscore.data file and display high scores to users
        """
        high_scores = []

        if os.path.exists(self.__HIGSCOREFILE):
            with open(self.__HIGSCOREFILE, 'rb') as file:
                high_scores = pickle.load(file)

        # Getting user input for player initials

        player_initials = input("Please enter your three initials to go on the scoreboard: ")[:3]
        player = (player_initials, self._score)

        # Checking for high_scores and appending it to high_score tuple
        if not high_scores:
            high_scores.append(player)
        else:
            index = 0
            while index < len(high_scores) and self._score <= high_scores[index][1]:
                index += 1
            high_scores.insert(index, player)

        # Displaying the high scores to user and storing it in the file.

        print("HIGH SCORES")
        # print("Name    Score")
        print("{:<8}{}".format("Name", "Score"))

        for initial, score in high_scores:
            # print(f"{initial}     {score}")
            print("{:<8}{}".format(initial, score))

        with open(self.__HIGSCOREFILE, 'wb') as file:
            pickle.dump(high_scores, file)

