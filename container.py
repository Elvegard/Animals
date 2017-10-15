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
        newAnimal = Animal('dog')
        newAnimal.setQuestion('does it have a tale')
        self.rootNode = newAnimal

        
