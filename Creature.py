# Author Name: Pratima Bankar, Shiva Raj Harinath Reddy , Preethi Gutha
# Date: 12/04/2023
# Description: Program gets ad sets the x and y coordinates for the creature.

from FieldInhabitant import FieldInhabitant


class Creature(FieldInhabitant):
    def __init__(self, x, y, symbol):
        super().__init__(symbol)
        self._x = x
        self._y = y

    # Getter and setter functions for x and y variable

    def getXY(self):
        return self._x, self._y

    def setXY(self, x, y):
        self._x = x
        self._y = y
