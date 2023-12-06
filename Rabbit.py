# Author Name: Pratima Bankar, Shiva Raj Harinath Reddy , Preethi Gutha
# Date: 12/04/2023
# Description: Program defines the x and y coordinates for the rabbit.

from Creature import Creature


class Rabbit(Creature):
    def __init__(self, x, y):
        super().__init__(x, y, "R")
