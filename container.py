from animal import Animal

class Container:
    'Animal container'
    game = False
    rootNode = None

    def __init__(self):
        self.game = True

    def getRootNode(self):
        return self.rootNode

    def setRootNode(self, rootNode):
        self.rootNode = rootNode

    def initRoot(self):
        newAnimalName = raw_input('New animal: ')
        newAnimal = Animal(newAnimalName)
        newQuestion = raw_input('New [Yes/No] question: ')
        newAnimal.setQuestion(newQuestion)
        newQuestionAnswer = raw_input('Answer [Y/N]: ')
        newAnimal.setAnswer(newQuestionAnswer)
        self.rootNode = newAnimal

        
