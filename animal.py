class Animal:
    'Animal type description and next leaf'
    animalType = None
    leftLeaf = None
    rightLeaf = None
    answer = None
    
    def __init__(self, animalType):
        self.animalType = animalType
    def getAnimalType(self):
        return self.animalType
        
    def setQuestion(self, question):
        self.question = question
    def getQuestion(self):
        return self.question

    def getLeftLeaf(self):
        # If user answer to question is NO
        return self.leftLeaf
    def setLeftLeaf(self, leftLeaf):
        self.leftLeaf = leftLeaf

    def getRightLeaf(self):
        # If user answer to question is YES
        return self.rightLeaf
    def setRightLeaf(self, rightLeaf):
        self.rightLeaf = rightLeaf
