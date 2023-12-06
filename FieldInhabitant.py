# Author Name: Pratima Bankar, Shiva Raj Harinath Reddy , Preethi Gutha
# Date: 12/04/2023
# Description: The program below stores the
# parameter representing a text symbol for the field inhabitant
# (vegetable, rabbit, captain, etc)

class FieldInhabitant:
    def __init__(self, symbol):
        self._symbol = symbol

    # Getter and setter functions for symbol variable

    def getsymbol(self):
        return self._symbol

    def setsymbol(self, symbol):
        self._symbol = symbol
