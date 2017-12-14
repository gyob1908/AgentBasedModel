# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 15:53:59 2017

@author: oliverbeatson
"""

# Imports all libraries needed for the model

import random
import operator
import matplotlib.pyplot
import agentframework
import csv

# Defines distance between the agents

def distance_between(agent0, agent1):
    return (((agent0.x - agent1.x)**2) + ((agent0.y - agent1.y)**2))**0.5

# Sets out the number of agents being defined as well as the number of iterations and how big the area in which they will operate is

num_of_agents = 30
num_of_iterations = 100
neighbourhood = 20
agents = []
agent = []
rowlist = []
environment = []

# Opens text file (CSV) and reads in the data contained

f = open('Text.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:				# A list of rows
    rowlist = []
    #rowlist.append(row)
    for value in row:				# A list of value
        print(value) 				# Floats
        rowlist.append(value)           #add the value to the rowlist
    environment.append(rowlist)         #add the rowlist to the environment        

f.close() 	# the data is read on request

#print(rowlist)

# Brings through the plot chart that will show the agents actions

matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agent))

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
            
# Plots the agents on to the environment and displays them
            
matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

for agent0 in agents:
    for agent1 in agents:
        distance = distance_between(agent0, agent1)
     
#print (neighbourhood)     
print (agents)

# Imports the data from the CSV file

f2 = open('dataout.csv', 'w', newline='') 
writer = csv.writer(f2, delimiter=',')
for row in environment:		
	writer.writerow(row)		
f2.close()

storelist=[]

# Saves data into a CSV file

f2 = open('dataout.csv', 'w', newline='') 
writer = csv.writer(f2, delimiter=',')
for i in agents:		
	writer.writerow(row)		
f2.close()
