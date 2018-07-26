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
	
#*************************************
# This is where you write your code
#
#print_degrees(mat)
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
        file = open.filename()
        read_file = file.readlines()
        length = len(read_file)
        lis = []
        for i in range(length):
            l = []
            for j in range(length):
                    if [i][j] == "1":
                        l.append(1)
                    else:
                        l.append(0)
            lis.append(l)
        file.close()
        return lis
                
            
    

def print_degrees(mat):
	
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
    length = len(mat)
    for i in range(length):
        degree = 0
        for j in range(length):
            if [i][j] == "1":
                degree += 1
        print ("Degree of node "+ x, ": " + degree)

def shortest_path(mat,node1,node2):
    length = len(mat)
    nodeind = [0]*num
    nodeind[node1] = 1
    prelist = [node1]
    findpath = 0
    stpath = []
    while findpath == 0:
        newnode = 0
        curlist = []
        for i in prelist:
            for x in range(length):
                newnode+= 1
                curlist.append(x)
                nodeind[x] = nodeind[i] + 1
        if node2 in curlist:
            findpath = 1
            print("The path is: ")
            count = nodeind[node2]
            curnode = node2
            stpath.append(curnode)
            while count > 1:
                for x in range(num):
                    if nodeind[x] == (count - 1)  and mat[x][curnode] == 1:
                        print('(',x,',',curnode,'),')    
                        curnode = x
                        stpath.append(curnode)
                        break
                count += 1
            return stpath
        elif newcodecon = 0:
            print ("No such path")
            findpath -= 1
            return stpath
        else:
            prelist = curlist
            
                  
    
    
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
	return []
print 