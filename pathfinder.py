#pathfinding code from Data Structures and Algorithmic Thinking with Python, 
#by N. Karumanchi
#comments added by dr.mo

def pathFinder( Matrix, position, N):
    
    if position == (N - 1, N - 1): #check if we're in the bottom left corner (the goal)
        return [(N - 1, N - 1)] #if so, add this to the end of our list of points
    
    x, y = position
    
    if x + 1 < N and Matrix[x+1][y] == 1: #check that we're not off the side of the matrix (going right) AND that we're still on a path (not a wall)
        a = pathFinder( Matrix, (x + 1, y), N) #recursive function call
        if a != None: #if something was returned from the last call, add it to the list of travel points
            return [(x, y)] + a 
    
    #repeat the above clump of code but going DOWN
    if y + 1 < N and Matrix[x][y+1] == 1:
        b = pathFinder( Matrix, (x, y + 1), N)
        if b != None:
            return [(x, y)] + b

#END FUNCTION DEFINITION--------------------------------------------

#driver code (like main)
Matrix = [[1, 1, 1, 1, 0],
          [0, 1, 0, 1, 0],
          [0, 1, 0, 1, 0],
          [0, 1, 0, 0, 0],
          [1, 1, 1, 1, 1]]

print(pathFinder(Matrix,(0,0), 5)) #the original function call
