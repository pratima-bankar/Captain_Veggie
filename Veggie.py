# Author Name: Pratima Bankar, Shiva Raj Harinath Reddy , Preethi Gutha
# Date: 12/04/2023
# Description: Program depicts the name and symbol of the vegetables and value representing them.

from FieldInhabitant import FieldInhabitant


class Veggie(FieldInhabitant):
    def __init__(self, name, symbol, points):
        super().__init__(symbol)
        self._name = name
        self._points = points

    # Getter and setter functions for name, points variable
    def getName(self):
        return self._name

    def getPoints(self):
        return self._points

    def setName(self, name):
        self._name = name

    def setPoints(self, points):
        self._points = points

    def __str__(self):
        return f"{super().getsymbol()}: {self.getName()} {self.getPoints()} points"
