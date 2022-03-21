import zombiedice
import random

"""
Project task:
- A bot that, after the first roll, randomly decides
  if it will continue or stop
- A bot that stops rolling after it has rolled two brains
- A bot that stops rolling after it has rolled two shotguns
- A bot that innitially decides it'll roll the dice one
  to four times, but will stopearly if it rolls two shotguns
- A bot that stops rolling after it has rolled more shotguns
  than brains
"""

class MyZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class RandomStop:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        brains = 0
        shotguns = 0
        while diceRollResults is not None:
            rand=random.randint(0,1)
            if rand==0:
                break
            else:
                diceRollResults = zombiedice.roll()

class stopTwoBrains:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        brains = 0
        shotguns = 0
        rand=random.randint(1,2,3,4)
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if rand<=rand
class stopTwoShotguns:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        brains = 0
        shotguns = 0
        while diceRollResults is not None:
            shotguns += diceRollResults['shotguns']
            if shotguns >= 2:
                break
            else:
                diceRollResults = zombiedice.roll()

class oneFourTwoShot:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        brains = 0
        shotguns = 0
        while diceRollResults is not None:
            brain += diceRollResults['brains']
            if brains >= 2:
                break
            else:
                diceRollResults = zombiedice.roll()



zombies = (
    RandomStop(name='Stop at random'),
    stopTwoBrains(name='Stop at 2 brains'),
    stopTwoShotguns(name='Stop at 2 shotguns')
    MyZombie(name='My Zombie Bot'),
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)
