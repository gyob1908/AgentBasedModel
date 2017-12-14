# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 15:53:59 2017

@author: oliverbeatson
"""

import random
import operator
import matplotlib.pyplot
import agentframework
import csv

def distance_between(agent0, agent1):
    return (((agent0.x - agent1.x)**2) + ((agent0.y - agent1.y)**2))**0.5

num_of_agents = 30
num_of_iterations = 100
neighbourhood = 20
agents = []
agent = []
rowlist = []
environment = []

f = open('Text.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:				# A list of rows
    rowlist = []
    #rowlist.append(row)
    for value in row:				# A list of value
        print(value) 				# Floats
        rowlist.append(value)           #add the value to the rowlist
    environment.append(rowlist)         #add the rowlist to the environment        

f.close() 	# Don't close until you are done with the reader;
		# the data is read on request.
#print(rowlist)

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

f2 = open('dataout.csv', 'w', newline='') 
writer = csv.writer(f2, delimiter=',')
for row in environment:		
	writer.writerow(row)		
f2.close()

storelist=[]

f2 = open('dataout.csv', 'w', newline='') 
writer = csv.writer(f2, delimiter=',')
for i in agents:		
	writer.writerow(row)		
f2.close()