#!python

#class ShellValues:
#    def __init__(self):
#        values=[1]
#        size=1
#    def min(self):
#        return values[0]
#
#    def max(self):
#        if size > 1:
#            return values[len(values)-1]
#        return 0
#
#    def __init__(self, inner_shell):
#        values=[]
#        size = inner_shell.size+2
#        values.append( inner_shell.min() + inner_shell.max() )
#        if size > 3:
#            values.append( values[0] + inner_shell.min() + inner_shell.max() )
#            for y in range(0, size-4):
#                values.append(
        
def determine_shell(input):
    shell = 1
    while input > (shell * shell):
        shell += 2
    return shell
    
def distance_to_center_edge(input, shell):
    se_corner = shell*shell
    sw_corner = se_corner - (shell-1)
    nw_corner = sw_corner - (shell-1)
    ne_corner = nw_corner - (shell-1)
    min_pos   = ne_corner - (shell-2)
    midpoint  = 0
    if ne_corner > input:
        midpoint = ne_corner - int(shell/2)
    elif nw_corner > input:
        midpoint = nw_corner - int(shell/2)
    elif sw_corner > input:
        midpoint = sw_corner - int(shell/2)
    else:
        midpoint = se_corner - int(shell/2)
    return abs( input - midpoint )

def determine_neighbors( step ):
    neighbors=[]
    neighbors.append( (step[0]+1, step[1]+1 ) )
    neighbors.append( (step[0], step[1]+1 ) )
    neighbors.append( (step[0]-1, step[1]+1 ) )
    neighbors.append( (step[0]-1, step[1] ) )
    neighbors.append( (step[0]-1, step[1]-1 ) )
    neighbors.append( (step[0], step[1]-1 ) )
    neighbors.append( (step[0]+1, step[1]-1 ) )
    neighbors.append( (step[0]+1, step[1] ) )
    return neighbors
    
def calculate_value( step, matrix ):
    neighbors = determine_neighbors( step )
    new_value = 0
    for neighbor in neighbors:
        new_value += matrix.get( neighbor, 0 )
    return new_value

def increment_step( step, matrix ):
    if step == (0,0):
        return (1,0)
    elif abs(step[0]) > abs(step[1]):
        if step[0] > 0:
            return (step[0], step[1]+1)
        else:
            return (step[0], step[1]-1)
    elif abs(step[1]) > abs(step[0]):
        if step[1] > 0:
            return (step[0]-1, step[1])
        else:
            return (step[0]+1, step[1])
    else:
        if step[0] > 0 and step[1] > 0:
            return (step[0]-1, step[1])
        elif step[0] < 0 and step[1] > 0:
            return ( step[0], step[1]-1)
        elif step[0] < 0 and step[1] < 0:
            return ( step[0]+1, step[1] )
        else:  # step[0] > 0 and step[1] < 0
            return ( step[0]+1, step[1] )

matrix={}
step=(0,0)
#matrix[(0,0)] = 1
matrix[step] = 1
#value = 1
#step = 0
input=289326
value=1
while value <= input:
    step = increment_step( step, matrix )
    value = calculate_value( step, matrix )
    matrix[step] = value
    
print( value )