#!/usr/bin/python3.6

# Graph Theory easy exercises for Social Networks module
# LACC 2018

#*************************************
# This is where you write your code
#
# matrix_load()
#
# Loads an adjacency matrix for a graph from a file
#
# input: none
# output: matrix containing each node 
# 
# Note: You can open a file using open(filename)
# 
# You can get a list containing each line with file.readlines()
#
#*************************************
def matrix_load(filename):
    file = open(filename)
    listlines = file.readlines()
    matrix = []
    for x in range(len(listlines)):
        line = []
        for y in range(len(listlines)):
            if listlines[x][y] == "1":
                line.append(1)
            else: 
                line.append(0)
        matrix.append(line)
    file.close()
    return matrix
        
#*************************************
# This is where you write your code
#
# print_degrees(mat)
#
# Prints the degrees of all nodes in a graph given an adj. matrix 
#
# input: the adjacency matrix of the graph
# output: none
# 
# Note: You don't need to return anything. 
#
# Effectively, you'll need to count the number of 1s in each row 
# (or each column) and print this. Use a nested loop (for or while)
#*************************************

def print_degrees(matrix):
    num=len(matrix)
    for x in range(num):
        degree=0
        for y in range(num):
            if matrix[x][y]==1:
                degree+=1
    print('Degree of Node ',x,': ',degree,'\n')

#*************************************
# This is where you write your code
#
# shortest_path(mat,node1,node2)
#
# Find the shortest path from node1 to node2 of all nodes in a graph given an adj. matrix 
#
# input: the adjacency matrix of the graph,node1,node2
# output: 'The path is: ' appended with all edges on the path if there is one, otherwise print out 'No such path'
# Note: at the same time, return a list containing all the nodes on the path if there is one, otherwise return []
#
#*************************************

def shortest_path(mat,node1,node2):
    count = 0
    nodelist = []
    for i in range(len(matrix):
        for j in range(len(matrix[i]):
            tempnode = []
            if matrix[i][j] == 1:
                tempnode.append(count+1)
                count= count + 1
            else:
                tempnode.append(0)

#*************************************
# This is where you write your code
#
# detect_cycle(mat)
#
# Detect the in a graph given an adj. matrix 
#
# input: the adjacency matrix of the graph
# output: 'Find a cycle, the first edge is: ' appended with an arbitrary edge on the cycle if there is one, otherwise print out 'No cycle in the graph'
# 
# Note: at the same time, return a list containing all the nodes on the cycle if there is one, otherwise return []
#
#*************************************

def detect_cycle(mat):
    return[]
	
