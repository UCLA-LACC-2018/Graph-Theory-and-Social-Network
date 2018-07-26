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
    file=open(filename)
    a=file.readlines()
    num=len(a)
    #print (a)
    mat=[]
    for x in range(num):
        tmp=[]
        for y in range (num):
            if a[x][y]=='1':
                tmp.append(1)
            else:
                tmp.append(0)
        mat.append(tmp)
    file.close()
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

def print_degrees(mat,ax,by):
    num=len(mat)
    for x in range(num):
        degree=0
        for y in range(num):
            if mat[x][y]==1:
                degree+=1
        print('\n','Degree of Node ',x,': ',degree, ' (', ax[x],',', by[x], ')')
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
    print (mat)
    num= (len(mat))
    #print ('num',num)
    next = []
    past = []
    path = 0
    nxt = []
    
#node1    
    #while path == 0:
    #print (node1)
    for x in range(num):
        #print (str(mat[node1][x]))
        if (mat[node1][x]) == 1:
            next.append(mat[x])
            nxt.append(x)
            #print (mat[x])
#next   
    #nxtx = len(nxt)
    #print ('past',past)
    print ('next',next)
    print ('nxt', nxt)
    #print ('nxtx',nxtx)
    #past.append(node1)
    next = []
    #nxt=[]
    temp = []
    stop = 0
    mat1= mat
    nope=[]
    #global nope
    
#nextnode 
    #for m in mat:
    #for m in range(num):
        #print(m)
        #print('past',past)
#        
    def loop(NN):
        #global kms
        #nope=[]
        past1 = past
        #print ('\n')
        ##print('NN',NN)
        for N in NN:
            ##print(N)
           # for m in range(len(NN)):
            for n in range(num):
                ##print('n',n)
                if mat[y][n]==1:
                    ##print('dsassa')
                    
                    if n not in past1:
                        past1.append(n)
                        
                        if n != node2:
                            for np in range(num):
                                if (mat[n][np]) == 1 and np not in past1:
                                    nope.append(np)
                            print('               mat:',[n], mat[n], '#N:', nope)
                            loop(nope)
                            ###print('past1',past1)
                            
                            
                        elif n == node2:
                            nope = node2
                            print('                   ', mat[n], '#N:',[node2], '/node2')
                    elif n in past1:
                        print('               mat:',[n], mat[n], '#T',[n], 'pass')
                    #return nope
                    #print (m)
        #return nope    
            
            
#            #print ('               ',mat[N])
 #           for m in range(len(mat[N])):
  #              if (mat[N][m]) == 1:
   #                 if m not in temp:
    #                    temp.append(m)
     #                   if m != node2:
      #                      print('                   ', mat[m], '#N:', m)
       #                 elif m == node2:
        #                    print('                   ', mat[m], '#N: 4', '/node2')
                  
         #           elif m in temp:
          #              print('                   ', mat[m], '#T',[m], 'pass')
    
    
    for x in (nxt):
        
        #nope= []
        rip = []
        kms = []
        past = [0]
        #print (mat[x])
        for no in range(num):
            if (mat[x][no]) == 1:
                rip.append(no)
        print ('\n','x:',x, '  ///   #N', rip, "    past:",past)
        print('xmat:', mat[x])
        #temp.append(x)
        NN = []
        #if x in past:
            #print('pass')
        #loop(mat1)
        for y in range(num):
            #print('\n')
            past = [0]
            nxx = []
            if (mat[x][y]) == 1: 
                if y not in past:
                    past.append(y)
                    
                    if y == node2:
                        print('\n','     ','mat',[y], mat[y], '##N:',[node2],'/node2')
                        
                    else:
                        
                        for nx in range(num):
                            if (mat[y][nx]) == 1:
                                nxx.append(nx)
                                
                        #NN.append(y)
                        #temp.append(y)
                        print('\n','     ','mat',[y], mat[y], '##N:', nxx)
                        ###print('past',past)
                        loop(nxx)
                        
                        #kms = loop(nxx)
                        #print (kms)
                        #print('nope',nope)
                        
                        #while nope != node2:
                            #loop(nope)
                       # print('\n','                   ','mat',[y], mat[y], '#N: 4','/node2')
                        
                            
                        #print (loop(nxx))
                        #xd = loop(nxx)
                        #print ('nope',xd)
                        
                elif y in past:
                    print('\n','     ','mat',[y], mat[y],'##T:',[y],'pass')
        
        
        
#        for N in NN:
 #           #print ('               ',mat[N])
  #          for m in range(len(mat[N])):
   #             if (mat[N][m]) == 1:
    #                if m not in temp:
     #                   temp.append(m)
      #                  if m != node2:
       #                     print('              ', mat[m], '#N:', m)
        #                elif m == node2:
         #                   print('              ', mat[m], '#N:', m, 'node2')
          #        
           #         elif m in temp:
            #            print('              ', mat[m],'pass')
                #print ('                     ', mat[N][m])
                
            
      #      if (mat[x][N]) == 1: 
       #         if N not in temp:    
        #            print('     ', mat[N])
         #           temp.append(y)
          #      elif N in temp:
           #         print('     ', mat[N],'pass')            
            #print(temp)
                        
            
                
            

                        
        #nxtx = len(nxt)    
        nxt = temp
        #print ('next',next)
        #print ('nxt',nxt, '\n')
        #print('nxtx',nxtx, '\n')
        next = []
        temp=[]
    #print ('node1',node1) 

#    for x in range(num):
 #       print (str(mat[x]))
  #      for y in range(num):
   #         if mat[x][y] == 1:
    #            print ('next', str(mat[y]))
     #           break
                
    
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
	pass
