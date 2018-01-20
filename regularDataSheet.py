# Author: Rajeev Ravi

import math


# This is the class regularsData. In this class the various variables, dictionaries and
# functions required for the regular data sheet will be defined
# An object of this class will then be created based on user input.

class RegularData:
    # First, major character stats will be defined.
    currentFloor = 0  # The current floor the character is on.
    pocketGrade = 'E'  # The current grade of the player pocket.
    pocketMod = 0  # The pocket modifier, based on the pocket Grade
    health = 0  # The Max HP of the character
    maxBang = 0  # Bang count
    pRes = 0  # Physical Resist
    pTouch = 0  # Physical Touch
    shinRes = 0  # Shinsoo Resist
    shinTouch = 0  # Shinsoo Touch
    shinControl = 0  # Shinsoo Control
    corePosition = "Dunce"  # The Main Position of the character. Note: Dunce is not a real position.

    name = "Paracule the Almighty"  # The name of the character.

    # Next,important dictionaries will be created holding values related to the positions.

    # The Dictionary that lists the characters rank in each position.
    positionTiers = {
        "Fisherman": 0,
        "Spear Bearer": 0,
        "Scout": 0,
        "Light Bearer": 0,
        "Wave Controller": 0
    }

    # The Dictionary that lists the characters core stats. Note: The Stats rn are just a test build.
    charStats = {
        "STR": 8,
        "DEX": 8,
        "CON": 5,
        "INT": 6,
        "WIS": 6,
        "CHA": 8,
        "SHN": 6
    }

    charStatTypes = list(charStats.keys())  # This variable is a list of the stats.

    # The Dictionary that lists the position health point multipliers.
    positionMultipliers = {
        "Fisherman": 10,
        "Spear Bearer": 8,
        "Scout": 8,
        "Light Bearer": 6,
        "Wave Controller": 8
    }

    # The Dictionary listing the correspondence between pocket grade and pocket mod.
    pocketModCorrespondence = {
        "E": 0,
        "D": 1,
        "C": 2,
        "B": 3,
        "A": 5,
        "S": 10
    }

    # Define the methods used in the constructor to instantiate default values.

    # Return the pocket mod based on the correspondence. This function is probably useless, but it's here anyways.
    def pocket_power(self):
        return self.pocketModCorrespondence[self.pocketGrade]

    # Calculate the appropriate modifier based on the value of the characters statvar
    # Argument: statvar - The character stat for which the modifier will be calculated.
    def mod_calc(self, statvar):
        if statvar >= 5:
            return math.ceil((math.floor(statvar - 5)) / 2) + self.pocket_power()
        else:
            return math.floor(statvar - 5 + self.pocket_power())

    # Calculate the health boost based on the user's core position.
    def positional_health(self):

        print(self.corePosition)
        print(self.positionTiers[self.corePosition])
        print(self.positionMultipliers[self.corePosition])
        return self.positionTiers[self.corePosition] * self.positionMultipliers[self.corePosition]

    # Calculate the users health based on the positional health, the current floor, pocket rank and CON.
    # Could probably be combined into one method with positional health.
    def calc_health(self):
        return self.positional_health() + (self.mod_calc(self.charStats["CON"]) - self.pocket_power() * 3) \
               + (math.floor(self.currentFloor / 20) * 3)

    # Time for bangs... and not the fun kind.
    # Calculate the maximum number of bangs the user can generate.
    def calc_max_bang(self):
        # First check that the user is on a high enough floor to utilize the number of bangs.
        if 5 - int((self.currentFloor - 2) / 13) <= 0:
            floor_max_bang = 1
        else:
            floor_max_bang = 5 - int((self.currentFloor - 2) / 13)

        # Now, the real bang calculations.

        bang_calc = 1 + int((self.charStats["INT"]
                            - (int(7 - ((self.currentFloor - 10) / 15)))) / floor_max_bang)

        if bang_calc <= 0:
            return 1
        else:
            return bang_calc

    # Calculates the shinsoo control of the character.
    def calc_shn_control(self):
        if self.charStats["WIS"] + 5 < 10:
            return 10
        else:
            return int(self.charStats["WIS"] + 5)

    # Calculates players resistances. Returns a list [Phys Res, Phys touch, Shinsoo Res, Shinsoo Touch]
    def calc_resistances(self):
        resistances = list()

        # Calculate Physical Resistance
        resistances.append(10 + int((self.mod_calc(self.charStats["DEX"])
                                     + self.mod_calc(self.charStats["STR"]) / 2) / 1.5)
                           + int(self.currentFloor / 20))

        # Calculates Physical Touch Resistance
        resistances.append(10 + int((self.mod_calc(self.charStats["DEX"])
                                     + self.mod_calc(self.charStats["STR"]) / 2) / 1.5) + int(
            self.currentFloor / 20))

        # Calculates Shinsoo Resistance
        resistances.append(10 + int(
            (self.mod_calc(self.charStats["INT"]) / 2 + self.mod_calc(self.charStats["SHN"])) / 1.5) + int(
            self.currentFloor / 20))
        # Calculates Shinsoo Touch Resistance
        resistances.append(10 + int(
            (self.mod_calc(self.charStats["INT"]) / 2 + self.mod_calc(self.charStats["WIS"])) / 1.5) + int(
            self.currentFloor / 20))

        return resistances

    # Constructor with character name, position, tier and current floor.
    # c is for constructor
    def __init__(self, c_name, c_core_position, c_current_floor, c_tier):
        self.corePosition = c_core_position
        self.positionTiers[core_position] = c_tier
        self.currentFloor = c_current_floor
        self.name = c_name

        self.pocketMod = self.pocket_power()
        self.health = self.calc_health()
        self.maxBang = self.calc_max_bang()

        reslist = self.calc_resistances()
        self.pRes = reslist[0]
        self.pTouch = reslist[1]
        self.shinRes = reslist[2]
        self.shinTouch = reslist[3]

        self.shinControl = self.calc_shn_control()

        # Print out the values.
        print("\nHealth: ", self.health)

        for x in range(len(self.charStats)):
            print("\n%s modifier: " % (self.charStatTypes[x]), self.mod_calc(self.charStats[self.charStatTypes[x]]))

        print("\n\n")
        print("\nMax Bang: ", self.maxBang)
        # print("Max Surface: ",)
        # print("Max Density: ",)
        print("\nShinsoo Control: ", self.shinControl)
        print("\nPhysical Resistance: ", self.pRes)
        print("\nShinsoo Resistance: ", self.shinRes)
        print("\nPhysical Touch Resistance: ", self.pTouch)
        print("\nShinsoo Touch Resistance: ", self.shinTouch)


# Main Method Begins Here. The User will be prompted to input class and rank, then object will
# be generated and all the main values will be printed out.
print("Suck my dick Hoaquin\n")

name = input("Input your character's name: ")

core_position = input("Input your character's core position: ")  # WARNING, MUST ENTER NAME EXACTLY FIRST LETTER CAPS AND SPACE.

current_floor = 20

tier = 3

object1 = RegularData(name, core_position, current_floor, tier)
