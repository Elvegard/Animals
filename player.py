class Player:
    playerName = None
    playerTry = 0
    playerWin = 0

    def __init__(self):
        playerName = raw_input('Name: ')
        if playerName == None or playerName == '':
            playerName = 'NN'
        self.playerName = playerName
        print

    def getPlayerName(self):
        return self.playerName
        
    def addPlayerTry(self):
        self.playerTry += 1

    def getPlayerTry(self):
        return self.playerTry

    def addPlayerWin(self):
        self.playerWin += 1

    def getPlayerTry(self):
        return self.playerWin

    def getPlayerStats(self):
        return (self.playerTry,
                self.playerWin,
                self.playerTry-self.playerWin)
