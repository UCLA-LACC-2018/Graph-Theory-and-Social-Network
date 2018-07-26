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
    file = open(filename);
    matrix_str = file.readlines();
    matrix_len = len(matrix_str);
    matrix = [];
    for x in range(matrix_len):
        temp = [];
        for y in range(matrix_len):
            if(matrix_str[x][y] == "1"):
                temp.append(1);
            else:
                temp.append(0);
        matrix.append(temp);
    file.close();
    return matrix;
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
    mat_len = len(mat);
    for x in range(mat_len):
        deg = 0;
        for y in range(mat_len):
            if(mat[x][y] == 1):
                deg += 1;
        print("Degree of Node",x,": ",deg,"\n");
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
    mat_len = len(mat);
    idnode = [0] * mat_len;
    idnode[node1] = 1;
    olist = [node1];
    peth = 0;
    sixpaths = [];
    while(peth == 0):
        nodecon = 0;
        curry = [];
        for x in olist:
            for y in range(mat_len):
                if(idnode[y] == 0 and mat[x][y] == 1):
                    nodecon += 1;
                    curry.append(y);
                    idnode[y] = idnode[x] + 1;
        if(node2 in curry):
            peth = 1;
            print("The path is: ")
            count = idnode[node2];
            currynode = node2;
            sixpaths.append(currynode);
            while(count > 1):
                for x in range(mat_len):
                    if(idnode[x] == (count - 1) and mat[x][currynode] == 1):
                        print("(",x,",",currynode,"),");
                        currynode = x;
                        sixpaths.append(currynode);
                        break;
                count -= 1;
            return sixpaths;
        elif(nodecon == 0):
            print("No such path");
            peth = -1;
            return sixpaths;
        else:
            olist = curry;
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
    mat_len = len(mat);
    trEEE = [];
    for x in range(mat_len):
        temp = [];
        for y in range(mat_len):
            if(mat[x][y] == 1):
                temp.append(y);
        trEEE.append([-1,0,temp]);
    olist = [0];
    trEEE[0][1] = 1;
    cicle = 0;
    scicole = [];
    while(cicle == 0):
        curry = [];
        for x in olist:
            for y in trEEE[x][2]:
                if(y != trEEE[x][0] and trEEE[y][1] == 1):
                    cicle = 1;
                    print("Find a cycle consisting of the following edges:\n");
                    rbranch = [];
                    rnode = y;
                    while(rnode != -1):
                        rbranch.append(rnode);
                        rnode = trEEE[rnode][0];
                    lnode = x;
                    while(lnode != - 1):
                        if(lnode in rbranch):
                            break;
                        else:
                            scicole.append(lnode);
                            print("(",trEEE[lnode][0],",",lnode,")\n");
                            lnode = trEEE[lnode][0];
                    scicole.reverse();
                    print("(",x,",",y,")\n");
                    currynode = y;
                    while(currynode != lnode):
                        scicole.append(currynode);
                        print("(",currynode,",",trEEE[currynode][0],")\n");
                        currynode = trEEE[currynode][0];
                    scicole.append(currynode);
                    return scicole;
                elif(trEEE[y][1] == 0):
                    trEEE[y][1] = 1;
                    curry.append(y);
                    trEEE[y][0] = x;
        if(curry == []):
            cicle = -1;
            print("No cycle in the graph");
            return scicole;
        else:
            olist = curry;