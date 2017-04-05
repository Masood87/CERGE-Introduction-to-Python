#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 20:38:07 2017

@author: pablo
"""

import matplotlib.pyplot as plt
import numpy as np
np.set_printoptions(precision=2)


class TitForTatPlayer():
    def __init__(self, first_move = 1):
        self.my_moves = []
        self.other_moves = []
        self.first_move = first_move
        
    def move(self):
        if len(self.other_moves) > 0 :
           if self.other_moves[-1] == 1:
               return 1
           else:
               return 0
        else:
            return self.first_move
    

if __name__ == "__main__":    
    payoff_matrix = [[(3,3),(0,5)], [(5,0), (1,1)]]
    
    n_rounds = 10
    
    p1 = TitForTatPlayer(first_move = 0 )
    p2 = TitForTatPlayer(first_move = 1)
    
    total_p1 = 0.0
    total_p2 = 0.0
    
    plt.ion()
    plt.axis([-0.1,n_rounds+0.1,-0.1,1.1])
    
    tot_payoff_p1 = 0.
    tot_payoff_p2 = 0.
    
    
    for n in range(1,n_rounds):
        m1 = p1.move()
        m2 = p2.move()
        
        # Players update the info of the moves
        p1.my_moves.append(m1)
        p1.other_moves.append(m2)    
        
        p2.my_moves.append(m2)
        p2.other_moves.append(m1)    
        
        ############################################
        ## Show payoffs
        ############################################
        tot_payoff_p1 += payoff_matrix[m1][m2][0]
        tot_payoff_p2 += payoff_matrix[m1][m2][1]
        
        avg_payoff_p1 = round(tot_payoff_p1/n,2)
        avg_payoff_p2 = round(tot_payoff_p2/n,2)
        
        print("-"*20)
        print("Average payoff for player 1: %f " % avg_payoff_p1)
        print("Average payoff for player 2: %f " % avg_payoff_p2)
        ############################################
        # Plot the moves
        plt.title("Playing prisonner's dilemma")
        plt.scatter(n,m1+0.05, color = "red")
        plt.scatter(n,m2-0.05, color = "blue")
        plt.show()
        plt.pause(1)
