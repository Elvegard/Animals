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
        return self.question + ': '

    def checkAndFixAnswer(self, userAnswer):
        answer = userAnswer.upper()
        if answer == 'JA':
            answer = 'Y'
        elif answer == 'YES':
            answer = 'Y'
        elif answer == 'NEI':
            answer = 'N'
        elif answer == 'NO':
            answer = 'N'
        return answer
            
    def setAnswer(self, answer):
        self.answer = self.checkAndFixAnswer(answer)

    def isAnswerCorrect(self, userAnswer):
        answer = self.checkAndFixAnswer(userAnswer)
        if answer == self.answer:
            return True
        else:
            return False
            
    def getLeftLeaf(self):
        return self.leftLeaf

    def setLeftLeaf(self, leftLeaf):
        self.leftLeaf = leftLeaf

    def getRightLeaf(self):
        return self.rightLeaf

    def setRightLeaf(self, rightLeaf):
        self.rightLeaf = rightLeaf
