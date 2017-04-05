#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 17:52:54 2017

@author: pablo
"""

import random 
import numpy as np

class Player:
    def __init__(self,p=0.5):
        self.p_betray = p
    def move(self):
        r = random.uniform(0,1)
        if r < self.p_betray:
            my_move = 1 #'B'
        else:
            my_move = 0 # 'C'
        return my_move            

class Game:
    def __init__(self, player1, player2, pmat):
        self.players = [player1, player2]
        self.payoffmat = pmat
        self.history = []

    def run(self, n_iter = 10):
        p1, p2 = self.players
        
        for n in range(n_iter):
            new_moves = p1.move(), p2.move()
            self.history.append(new_moves)
            
    def payoff(self):
        payoffs = (self.payoffmat[m1][m2] for (m1, m2) in self.history)
        payoff_p1 = sum(p[0] for p in payoffs)
        payoff_p2 = sum(p[1] for p in payoffs)
        return payoff_p1, payoff_p2

# SHOW TIME
PAYOFFMAT = [[(3,3), (0,5)],[(5,0),(1,1)]]
georgi = Player(p=0.1)
matej = Player(p=0.7)

p_dilemma_game = Game(georgi, matej, PAYOFFMAT)
p_dilemma_game.run() 

payoff_georgi, payoff_matej = p_dilemma_game.payoff()
print("Georgi's payoff: ", payoff_georgi)
print("Matej's payoff: ", payoff_matej) 
           
            










            