#!python

maze_lines=[]

with open('input.txt') as f:
    for line in f:
        maze_lines.append(list(line.strip('\n')))


def find_start( maze_lines ):
    for i in range( len(maze_lines[0]) ):
        if maze_lines[0][i] == '|':
            return ( 0, i, 's' )
    assert False and 'no start found'

def can_walk_direction( maze_lines, pos ):
    direction = pos[2]
    if direction == 's':
        return pos[0] < len(maze_lines)-1 and maze_lines[pos[0]+1][pos[1]] != ' '
    elif direction == 'e':
        return pos[1] < len(maze_lines[pos[0]])-1 and maze_lines[pos[0]][pos[1]+1] != ' '
    elif direction == 'n':
        return pos[0] > 0 and maze_lines[pos[0]-1][pos[1]] != ' '
    elif direction == 'w':
        return pos[1] > 0 and maze_lines[pos[0]][pos[1]-1] != ' '
    return false

def get_maze_path( maze_lines, pos ):
    return maze_lines[pos[0]][pos[1]]

def walk_direction( maze_lines, pos, letters ):
    new_pos = None
    direction = pos[2]
    if direction == 's':
        new_pos = ( pos[0]+1, pos[1], 's' )
    elif direction == 'n':
        new_pos = ( pos[0]-1, pos[1], 'n' )
    elif direction == 'e':
        new_pos = ( pos[0], pos[1]+1, 'e' )
    elif direction == 'w':
        new_pos = ( pos[0], pos[1]-1, 'w' )
    underfoot = get_maze_path( maze_lines, new_pos )
    if underfoot != '|' and underfoot != '-' and underfoot != '+':
        letters.append( underfoot )
    return new_pos

#def can_turn_left( maze_lines, pos ):
#def can_turn_right( maze_lines, pos ):
#def turn_left( maze_lines, pos, letters ):
#def turn_right( maze_lines, pos, letters ):

def walk_path( maze_lines, pos, letters ):
    if can_walk_direction( maze_lines, pos ):
        return walk_direction( maze_lines, pos, letters )
    elif can_turn_left( maze_lines, pos ):
        return turn_left( maze_lines, pos, letters )
    elif can_turn_right( maze_lines, pos ):
        return turn_right( maze_lines, pos, letters )
    else:
        return None
        
pos=find_start( maze_lines )
letters=[]

while pos != None:
    pos = walk_path( maze_lines, pos, letters )


