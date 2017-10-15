import pickle

from player import Player
from container import Container
from animal import Animal


class InitGame:
    animalContainer = None
    player = None
    
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
            print('Creating a new database file for the game.')
            self.initContainer()
            self.animalContainer.initRoot()
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
        print('Answer with Y/N')

    def getPlayerAnswer(self, question):
        playerAnswer = raw_input(question + '?').upper()
        inputOK = self.isPlayerAnswerOK(playerAnswer)
        while not (inputOK):
            self.showInfo()
            playerAnswer = raw_input(animal.getQuestion() + '?').upper()
            inputOK = self.isPlayerAnswerOK(playerAnswer)
        return playerAnswer

    def giveUp(self, previousAnimal, previousAnswer, player):
        player.addPlayerWin()
        animalType = raw_input('What animal was it? ')
        animalQuestion = raw_input('Enter a quiesting for the ' + animalType + ': ')
        animal = Animal(animalType)
        animal.setQuestion(animalQuestion)
        if previousAnswer == 'N':
            previousAnimal.setLeftLeaf(animal)
        else:
            previousAnimal.setRightLeaf(animal)                



    
            
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

print '-----------------------------------'
print '      Starting Animal Game'
print '-----------------------------------'
game.showInfo()


while gameRunning:
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
        player.addPlayerTry()
        gameRunning = False

        if previousAnswer == 'N':
            print 'I give up! :( '
            game.giveUp(previousAnimal, previousAnswer, player)
        else:
            question = 'Is the anwer ' + str(previousAnimal.getAnimalType())
            playerAnswer = game.getPlayerAnswer(question)
            if playerAnswer == 'N':
                game.giveUp(previousAnimal, previousAnswer, player)
            else:
                print 'I win!'

        game.saveGame()
        playerAnswer = game.getPlayerAnswer('Play again?')
        if playerAnswer == 'J' or playerAnswer == 'Y':
            gameRunning = True
            game.loadGameData()
            animal = game.getRootAnimal()
        else:
            gameRunning = False;
            (playerTry, playerWin, playerLose) = player.getPlayerStats()
            print
            print '--------------------------------'
            print player.getPlayerName() + ' your results:'
            print 'Tries: ' + str(playerTry)
            print 'You win: ' + str(playerWin)
            print 'Compuer win: ' + str(playerLose)
            print
                




