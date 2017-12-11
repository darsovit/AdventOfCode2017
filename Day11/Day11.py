#!python

def get_input():
    directions=[]
    with open('input.txt') as f:
        for line in f:
            directions=line.strip().split(',')
    return directions

def determine_direction( location, movement ):
    if movement == 'n':
        return ( location[0], location[1]+2 )
    elif movement == 's':
        return ( location[0], location[1]-2 )
    elif movement == 'ne':
        return ( location[0]+1, location[1]+1 )
    elif movement == 'se':
        return ( location[0]+1, location[1]-1 )
    elif movement == 'nw':
        return ( location[0]-1, location[1]+1 )
    elif movement == 'sw':
        return ( location[0]-1, location[1]-1 )

def calculate_distance_to( location, origin ):
    x_diff = abs( location[0] - origin[0] )
    y_diff = abs( location[1] - origin[1] )
    vertical_steps=0
    if y_diff > x_diff:
        vertical_steps =  int( ( y_diff - x_diff ) / 2 )
    return x_diff + vertical_steps
        
        
directions = get_input()

location=(0,0)
max_away=0
for movement in directions:
    location = determine_direction(location, movement)
    curr_distance=calculate_distance_to( location, (0,0) )
    if curr_distance > max_away:
        max_away = curr_distance
    
print( location )
print( "steps to get back: ", calculate_distance_to( location, (0,0) ) )
print( "max distance away: ", max_away )

