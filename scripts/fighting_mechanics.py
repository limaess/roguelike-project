import pygame as pg

class TurnSys:
    def __init__(self, whos_turn, which_round, exhaustion):
        self.whos_turn = whos_turn
        self.which_round = which_round
        self.exhaustion = exhaustion

        self.turnThingIdk = None

        self.turnOrder = []

    def makeTurnOrder(self,player, enemy1,enemy2,enemy3):
        if not self.turnOrder:
            self.turnOrder = [player,enemy1,enemy2,enemy3,player]
        else:
            print('why am i calling this function?')

        self.turnThingIdk = self.turnOrder[self.whosTurn]