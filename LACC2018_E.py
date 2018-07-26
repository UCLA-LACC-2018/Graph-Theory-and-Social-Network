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
    with open(filename, 'r') as f:
        a = f.readlines()
    mat = []
    for i in range(len(a)) :
        temp = []
        for j in range(len(a[i])) :
            if a[i][j] == '1' :
                temp.append(1)
            else :
                temp.append(0)
        mat.append(temp)
    f.close()
    return mat
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

def print_degrees(mat):
    for x in range(len(mat)) :
        degree = 0
        for y in range(len(mat[x])) :
            if(mat[x][y] == 1) :
                degree += 1
        print("Node " + str(x) + " has a degree of: " + str(degree) + "\n")
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
    alreadyvisited = [node1]
    curlist = []
    backpath = []
    allpaths = []
    nodeindexes = [0] * len(mat)
    nodeindexes[node1] = 1
    foundPath = False
    while not foundPath:
        curlist = []
        possiblenodes = 0
        for visited in alreadyvisited:
            for possible in range(len(mat)) :
                if(mat[visited][possible] == 1 and nodeindexes[possible] < 1) :
                    possiblenodes+=1
                    curlist.append(possible)
                    nodeindexes[possible] = nodeindexes[visited] + 1
        
        if node2 in curlist :
            foundPath = True
            print("The path is: ")
            count = nodeindexes[node2]
            backpath.append(node2)
            curnode = node2
            while count > 0 :
                for x in range(len(mat)) :
                    if (nodeindexes[x] == count - 1 and mat[x][curnode] == 1) :
                        
                        print("(" + str(curnode) + ", " + str(x) + ")")
                        curnode = x
                        backpath.append(x)
                        break
                count -= 1        
            return backpath
        elif possiblenodes == 0:
            print("No such path")
            foundPath = True
            return backpath
        else :
            alreadyvisited = curlist
        
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
    for i in range(len(mat)):
        path = recur_cycle(mat, i, [])
        if len(path) > 0:
            for i in range(len(path) - 1):
                print("(" + str(path[i]) + ", " + str(path[i+1]) + ")")
            return path
    print("No cycle")
    return path

def recur_cycle(mat, node, visited):
    if len(visited) > 2 and node == visited[0]:
        visited.append(node)
        return visited
    visited.append(node)
    for j in range(len(mat)):
        if mat[node][j] == 1 and (len(visited) < 2 or j != visited[-2]):
            return recur_cycle(mat, j, visited)
    return []
