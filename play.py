import pickle

from player import Player
from container import Container
from animal import Animal


class InitGame:
    animalContainer = None
    player = None
    
    
    def __init__(self):
        print 'Animal guessing game'

    def initContainer(self):
        self.animalContainer = Container()

    def addPlayer(self, player):
        self.player = player
    def getPlater(self):
        return self.player

    def getRootAnimal(self):
        # We need to add an animal by guessing
        if self.animalContainer.getRootNode() == None:
            self.animalContainer.initRoot()
        return self.animalContainer.getRootNode()
    def setRootAnimal(self, rootAnimal):
        self.animalContainer.setRootNode(rootAnimal)

    def loadGameData(self):
        try:
            gameFile = open('animals.dat', 'rb')
            self.animalContainer = pickle.load(gameFile)
            gameFile.close()
        except:
            print 'Creating new game data file'
            self.initContainer()
            self.animalContainer.initRoot()
            #self.saveGame()

    def saveGame(self):
        gameFile = open('animals.dat', 'wb')
        pickle.dump(self.animalContainer,
                    gameFile,
                    pickle.HIGHEST_PROTOCOL)
        gameFile.close()

    def isPlayerAnswerOK(self, playerAnswer):
        if playerAnswer == 'J':
            return True
        elif playerAnswer == 'Y':
            return True
        elif playerAnswer == 'N':
            return True
        else:
            return False

    def showInfo(self):
        print 'Answer questions with Y/N'

    def giveUp(self, userAnswer, currentAnimal):
        print 'Give up!'
        animalType = raw_input('What type of animal was it: ')
        animal = Animal(animalType)
        animalQuestion = raw_input('Give a question for the animal: ')
        animal.addQuestion(animalQuestion)
        if userAnswer == 'N':
            currentAnimal.setLeftLeaf(animal) # NO
        else:
            currentAnimal.setRightLeaf(animal) # YES

    def getPlayerAnswer(self, question):
        playerAnswer = raw_input(question + '? ').upper()
        inputOK = self.isPlayerAnswerOK(playerAnswer)
        while not (inputOK):
            self.showInfo()
            playerAnswer = raw_input(animal.getQuestion()).upper()
            inputOK = self.isPlayerAnswerOK(playerAnswer)
        return playerAnswer


            
#-------------------
# INIT GAME
#-------------------
player = Player()
game = InitGame()
game.loadGameData()
game.addPlayer(player)
animal = game.getRootAnimal()
inputOK = False

gameRunning = True
print 'Game running.'

while gameRunning:
    game.showInfo()

    # Ask question for current animal
    playerAnswer = game.getPlayerAnswer(animal.getQuestion())

    # Check answer
    previousAnimal = animal
    if playerAnswer == 'J' or playerAnswer == 'Y':
        animal = animal.getRightLeaf() # YES
    else:
        animal = animal.getLeftLeaf() # NO
    previousAnswer = playerAnswer

    # No more animals, we must guess
    if animal == None:
        gameRunning = False
        question = 'Is it ' + str(previousAnimal.getAnimalType())
        playerAnswer = game.getPlayerAnswer(question)

        if playerAnswer == 'N':
            print 'YOU WIN!'
            animalType = raw_input('What animal was it? ')
            animalQuestion = raw_input('Enter a question for ' + animalType + ': ')
            animal = Animal(animalType)
            animal.setQuestion(animalQuestion)

            if previousAnswer == 'N':
                previousAnimal.setLeftLeaf(animal)
            else:
                previousAnimal.setRightLeaf(animal)                
        else:
            print 'I WIN!'


#-------------------
# DONE
#-------------------
game.saveGame()
print 'Done'


