import pygame as pg
import random as rnd

class TurnSys:
    def __init__(self, whos_turn, which_round, exhaustion):
        self.whos_turn = whos_turn
        self.which_round = which_round
        self.exhaustion = exhaustion

        self.turn_thing = None

        self.turn_order = []

    def endTurn(self,player,enemy, player_inv,enemy_inv):
        self.whosTurn += 1
        if self.whosTurn == 5:
            self.whosTurn = 0

        player.has_attacked = False
        enemy.has_attacked = False

        for item in player_inv:
            item.been_used = False
        for item in enemy_inv:
            item.been_used = False

    def makeTurnOrder(self,player, enemy1,enemy2,enemy3):
        if not self.turn_order:
            self.turn_order = [player,enemy1,enemy2,enemy3,player]
            return True
        else:
            print('why am i calling this function?')

        self.turn_thing = self.turn_order[self.whos_turn]