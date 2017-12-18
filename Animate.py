#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 17:49:28 2017

@author: oliverbeatson
"""

# All code derived from practicals given by Andy Evans at the University of Leeds
# http://www.geog.leeds.ac.uk/courses/computing/study/core-python-phd/

# Imports libraries used for code

import random
import operator
import matplotlib.pyplot
import matplotlib.animation 

# Defines Agents and iterations

num_of_agents = 10
num_of_iterations = 100
agents = []

# Generates table for agents to operate in

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Make the agents.
for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])

carry_on = True	
	
def update(frame_number):
 
    fig.clear()   
    global carry_on
 
# Defines movements of agents
# Coordinates set to random
    
    for i in range(num_of_agents):
        if random.random() < 0.5:
            agents[i][0]  = (agents[i][0] + 1) % 99 
        else:
            agents[i][0]  = (agents[i][0] - 1) % 99
        
        if random.random() < 0.5:
            agents[i][1]  = (agents[i][1] + 1) % 99 
        else:
            agents[i][1]  = (agents[i][1] - 1) % 99 
        
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
        
# Places agents within table
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i][0],agents[i][1])
        #print(agents[i][0],agents[i][1])


# Defines the visual content to include in graph
		
def gen_function(b = [0]):
    a = 0
    global carry_on 
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1


# Creates the movement animation within the table
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)


# Displays the table in seperete pop-up page

matplotlib.pyplot.show()