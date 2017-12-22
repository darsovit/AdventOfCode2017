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
    infected_map={}
    for y in range(num_lines):
        assert(len(input_map[y])==length_of_lines)
        for x in range(length_of_lines):
            if '#' == input_map[y][x]:
                infected_map[(x-x_offset, y_offset-y)] = '#'
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

def turn_around( dir ):
    if dir == 'n':
        return 's'
    elif dir == 'e':
        return 'w'
    elif dir == 's':
        return 'n'
    assert( dir == 'w' )
    return 'e'

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
    infection_state = state['infected_map'].get( state['carrierpos'][0], '.' )
    if infection_state == 'W':
        state['infected_map'][state['carrierpos'][0]] = '#'
        state['infectedcount'] += 1
        state['carrierpos'] = calculate_new_carrierpos( state['carrierpos'][0], state['carrierpos'][1] )
    elif infection_state == '#':
        state['infected_map'][state['carrierpos'][0]] = 'F'
        state['carrierpos'] = calculate_new_carrierpos( state['carrierpos'][0], turn_right(state['carrierpos'][1]) )
    elif infection_state == 'F':
        state['infected_map'].pop( state['carrierpos'][0] )
        state['carrierpos'] = calculate_new_carrierpos( state['carrierpos'][0], turn_around(state['carrierpos'][1] ) )
    else:
        assert( infection_state == '.' )
        state['infected_map'][state['carrierpos'][0]] = 'W'
        state['carrierpos'] = calculate_new_carrierpos( state['carrierpos'][0], turn_left(state['carrierpos'][1]) )

input_map = read_input()
state     = init_state( input_map )
num_bursts= 10000000
#print( state )
for i in range( num_bursts ):
    perform_burst( state )
    #print( state )
print( state['infectedcount'] )