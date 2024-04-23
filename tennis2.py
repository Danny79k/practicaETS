# -*- coding: utf-8 -*-

class TennisGame2:
    def __init__(self, player1Name, player2Name):
        self.server = player1Name
        self.receiver = player2Name
        self.serverScore = 0
        self.receiverScore = 0

    def won_point(self, playerName):
        if self.server == playerName:
            self.serverScore += 1
        else:
            self.receiverScore += 1

    def score(self):
        result = NotDefault(self,DefaultResult(self)).getResult()
        return result.format()


#quizas inutil
class TennisResult:
    def __init__(self, serverScore, receiverScore):
        self.serverScore = serverScore
        self.receiverScore = receiverScore

    def format(self):
        if "" == self.receiverScore:
            return self.serverScore
        if self.serverScore == self.receiverScore:
            return self.serverScore + "-All"
        return self.serverScore + "-" + self.receiverScore

class NotDefault:
    def __init__(self, game, nextResult):
        self.game = game
        self.nextResult = nextResult
    def getResult(self):
        if (self.isDeuce()): 
            return TennisResult("Deuce","")
        if (self.HasWon()): 
            return TennisResult("Win for " + self.HasWon(),"")
        if (self.HasAdvantage()):
            return TennisResult("Advantage " + self.HasAdvantage(),"")
        return self.nextResult.getResult()    
    
    def HasAdvantage(self):
        if self.game.serverScore >= 4 and (self.game.serverScore - self.game.receiverScore) == 1:
            return self.game.server
        elif self.game.receiverScore >= 4 and (self.game.receiverScore - self.game.serverScore) == 1:
            return self.game.receiver

    def HasWon(self):
        if self.game.serverScore >= 4 and (self.game.serverScore - self.game.receiverScore) >= 2:
            return self.game.server
        elif self.game.receiverScore >= 4 and (self.game.receiverScore - self.game.serverScore) >= 2:
            return self.game.receiver
        
    def isDeuce(self):
        return self.game.serverScore >= 3 and self.game.receiverScore >= 3 and (self.game.serverScore == self.game.receiverScore)


class DefaultResult:
    def __init__(self, game):
        self.game = game
        self.scores = ["Love", "Fifteen", "Thirty", "Forty"]

    def getResult(self):
        return TennisResult(self.scores[self.game.serverScore], self.scores[self.game.receiverScore])
