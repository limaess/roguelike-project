import pygame as pg

class TurnSys:
    def __init__(self, whos_turn, which_round, exhaustion):
        self.whos_turn = whos_turn
        self.which_round = which_round
        self.exhaustion = exhaustion

        self.turnThingIdk = None

        self.isThereAList = False

        self.turnOrder = []