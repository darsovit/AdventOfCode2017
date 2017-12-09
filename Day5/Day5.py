#!python

maze_steps=[]
with open('input.txt') as f:
    for line in f:
        maze_steps.append( int(line) )

location=0
steps=0
print( "maze length: ", len(maze_steps) )
while location >= 0 and location < len(maze_steps):
    curloc = location
    location += maze_steps[curloc]
    if abs(maze_steps[curloc]) >= 3:
       maze_steps[curloc] -= 1
    else:
        maze_steps[curloc] += 1
    steps += 1
    
print( "escaped to: ", location )
print( "steps needed: ", steps )
