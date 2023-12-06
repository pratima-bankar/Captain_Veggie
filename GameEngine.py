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