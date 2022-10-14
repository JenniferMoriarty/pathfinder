#pathfinding code from Data Structures and Algorithmic Thinking with Python, 
#by N. Karumanchi

def pathFinder( Matrix, position, N):
    #returns a list of the paths taken
    if position == (N - 1, N - 1):
        return [(N - 1, N - 1)]
    x, y = position
    if x + 1 < N and Matrix[x+1][y] == 1:
        a = pathFinder( Matrix, (x + 1, y), N)
        if a != None:
            return [(x, y)] + a
    if y + 1 < N and Matrix[x][y+1] == 1:
        b = pathFinder( Matrix, (x, y + 1), N)
        if b != None:
            return [(x, y)] + b
        
Matrix = [[1, 1, 1, 1, 0],
          [0, 1, 0, 1, 0],
          [0, 1, 0, 1, 0],
          [0, 1, 0, 0, 0],
          [1, 1, 1, 1, 1]]
print(pathFinder(Matrix,(0,0), 5))
