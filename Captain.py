# Author Name: Pratima Bankar, Shiva Raj Harinath Reddy , Preethi Gutha
# Date: 12/04/2023
# Description: Program to get the list of veggie that captain harvests.

from Creature import Creature


class Captain(Creature):
    def __init__(self, x, y):
        super().__init__(x, y, "V")
        self._veggies = []

    # Function to addVeggies to List
    def addVeggie(self, v):
        self._veggies.append(v)

    # Getter function for the veggies list
    def getVeggie(self):
        return self._veggies
