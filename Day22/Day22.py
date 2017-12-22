#!python


def read_input():
    input_map=[]
    with open('input.txt') as file:
        for line in file:
            input_map.append(line.strip())
    return input_map

def read_sample():
    input_map=[]
    input_map.append('..#')
    input_map.append('#..')
    input_map.append('...')
    return input_map

def calculate_infected_map( input_map ):
    length_of_lines=len(input_map[0])
    num_lines=len(input_map)
    x_offset=int((length_of_lines-1)/2)
    y_offset=int((num_lines-1)/2)
    assert(length_of_lines%2==1)
    assert(num_lines%2==1)
    infected_map=set()
    for y in range(num_lines):
        assert(len(input_map[y])==length_of_lines)
        for x in range(length_of_lines):
            if '#' == input_map[y][x]:
                infected_map.add((x-x_offset, y_offset-y))
    return infected_map

def init_state( input_map ):
    state={}
    state['infectedcount'] = 0
    state['carrierpos'] = ( ( 0, 0 ), 'n' )
    state['infected_map'] = calculate_infected_map( input_map )
    return state

def turn_left( dir ):
    if dir == 'n':
        return 'w'
    elif dir == 's':
        return 'e'
    elif dir == 'w':
        return 's'
    assert( dir == 'e' )
    return 'n'

def turn_right( dir ):
    if dir == 'n':
        return 'e'
    elif dir == 'e':
        return 's'
    elif dir == 's':
        return 'w'
    assert( dir == 'w' )
    return 'n'

def calculate_new_carrierpos( pos, dir ):
    if dir == 'n':
        return ( (pos[0], pos[1]+1), dir )
    elif dir == 'e':
        return ( (pos[0]+1, pos[1]), dir )
    elif dir == 's':
        return ( (pos[0], pos[1]-1), dir )
    assert ( dir == 'w' )
    return     ( (pos[0]-1, pos[1]), dir )

def perform_burst( state ):
    if state['carrierpos'][0] in state['infected_map']:
        state['infected_map'].remove( state['carrierpos'][0] )
        state['carrierpos'] = calculate_new_carrierpos( state['carrierpos'][0], turn_right(state['carrierpos'][1]) )
    else:
        state['infected_map'].add( state['carrierpos'][0] )
        state['infectedcount'] += 1
        state['carrierpos'] = calculate_new_carrierpos( state['carrierpos'][0], turn_left(state['carrierpos'][1]) )

input_map = read_input()
state     = init_state( input_map )
num_bursts= 10000
#print( state )
for i in range( num_bursts ):
    perform_burst( state )
    #print( state )
print( state['infectedcount'] )