# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 15:53:59 2017

@author: oliverbeatson
"""

# All code derived from practicals given by Andy Evans at the University of Leeds
# http://www.geog.leeds.ac.uk/courses/computing/study/core-python-phd/

import random

# Defines agent class within the environment

class Agent():
    def __init__(self, environment, agent):
        self.environment = environment
        self.agent = agent
        self.store =0
        self.x = random.randint(0,1000)
        self.y = random.randint(0,1000)    

# Defines the movement of the agents
# Coordinates of each agent set to random
        
    def move (self):
        
        if random.random() < 0.5:
           self.x = (self.x + 1) % 300
        
        else:
           self.x = (self.x - 1) % 300
        
        if random.random () < 0.5:
            self.y = (self.y + 1) % 300
        
        else:
           self.y = (self.y - 1) % 300

# Defines agents to change the environment around them (eat) by a factor of ten
# Represented by change of colour in the immediate surrounding of the environment 
           
    def eat(self): 
        if self.environment[self.y][self.x] > 10:
           self.environment[self.y][self.x] -= 10
           self.store += 10

# Pythagorian equation to set distance between agents
           
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5        
        

# This section defines an equal sharing of stores previously 
# gained between agents from eat function
          
    def share_with_neighbours(self, neighbourhood):
     for agent in self.agent:
         dist = self.distance_between(agent) 
         if dist <= neighbourhood:
            sum = self.store + agent.store
            ave = sum /2
            self.store = ave
            agent.store = ave
         print("sharing " + str(dist) + " " + str(ave))
     