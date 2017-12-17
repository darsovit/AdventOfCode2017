#!python


def shift_programs( programs, shift_value ):
    assert( shift_value > 0 )
    return programs[-shift_value:] + programs[:-shift_value]
    
def exchange_slots( programs, slots ):
    assert( len( slots ) == 2 )
    tmp = programs[slots[1]]
    programs[slots[1]] = programs[slots[0]]
    programs[slots[0]] = tmp
    return programs
    
def exchange_programs( programs, two_progs ):
    assert( len(two_progs) == 2)
    swapped0 = -1
    swapped1 = -1
    for i in range(len(programs)):
        if ( programs[i] == two_progs[0] ):
           programs[i] = two_progs[1]
           swapped0 = i
           if swapped1 > -1:
               break
        elif ( programs[i] == two_progs[1] ):
           programs[i] = two_progs[0]
           swapped1 = i
           if swapped0 > -1:
               break
    assert( swapped0 != swapped1 )
    assert( swapped0 > -1 )
    assert( swapped1 > -1 )
    return programs

def build_moves( move ):
    if move[0] == 's':
        return ( shift_programs, int(move[1:]) )
    elif move[0] == 'x':
        return ( exchange_slots, list(map(lambda x: int(x), move[1:].split('/') ) ) )
    elif move[0] == 'p':
        return ( exchange_programs, list(move[1:].split('/') ) )
    else:
        assert( False & move[0] )

def handle_input( programs, move ):
#    if move[0] == 's':
#        return shift_programs( programs, int(move[1:]) )
#    elif move[0] == 'x':
#        return exchange_slots( programs, list(map(lambda x: int(x), move[1:].split('/')) ) )
#    elif move[0] == 'p':
#        return exchange_programs( programs, list(move[1:].split('/') ) )
#    else:
#        assert( False & move[0] )
    my_moves = build_moves( move )
    return my_moves[0]( programs, my_moves[1] )

def test1():
    test=[ 'a', 'b', 'c', 'd', 'e' ]
    assert( 'abcde' == ''.join( test ) )
    test=handle_input( test, 's1' )
    #print( test )
    assert( 'eabcd' == ''.join( test ) )
    test=handle_input( test, 'x3/4' )
    #print( test )
    assert( 'eabdc' == ''.join( test ) )
    test=handle_input( test, 'pe/b' )
    print( test )
    assert( 'baedc' == ''.join( test ) )
    
    test=list('abcde')
    print(test)
    test=handle_input( test, 'pe/b' )
    test=handle_input( test, 's1' )
    test=handle_input( test, 'x3/4' )
    print( test )

def test2():
    test=[ 'a', 'b', 'c', 'd', 'e' ]
    test = handle_input( test, 's3' )
    assert( 'cdeab' == ''.join(test) )

def build_moves_map( shift_moves ):
    start_positions = list( range(16) )
    positions=start_positions
    for move in shift_moves:
        positions = move[0]( positions, move[1])
    assert( 16 == len( positions ) )
    moves_map={}
    for i in range( 16 ):
        moves_map[ i ] = positions[ i ]
    return moves_map
    
def apply_moves_map( start_positions, shift_mapping ):
    new_positions=list()
    for i in range( 16 ):
        new_positions.append( start_positions[ shift_mapping[i] ] )
    return new_positions

def build_swap_map( swap_moves ):
    new_positions = list( map( lambda x: chr(ord('a')+x), range(16) ) )
    for move in swap_moves:
        new_positions = move[0]( new_positions, move[1] )
    start_positions = list( map( lambda x: chr(ord('a')+x), range(16) ) )
    #print ( 'build_swap_map (start pos):', ''.join( start_positions ) )
    #print ( 'build_swap_map (final pos):', ''.join( new_positions ) )
    
    swap_map={}
    for i in range(16):
        swap_map[start_positions[i]] = new_positions[i]
    #print( 'build_swap_map: ', swap_map )
    return swap_map
    
def apply_swap_map( start_positions, swap_mapping ):
    #print( 'apply_swap_map: ', ''.join( start_positions ) )
    new_positions=list()
    for i in range( 16 ):
        new_positions.append( swap_mapping[start_positions[i]] )
    #print( 'apply_swap_map: ', ''.join( new_positions ) )
    return new_positions

def prog():
    iterations=1000000000
    programs=list( map(lambda x: chr(ord('a')+x), range(16) ) )
    #print( programs )
    new_positions=programs
    moves=[]
    with open('input.txt') as f:
        for line in f:
            moves = list( map( lambda x: build_moves(x), line.strip().split(',') ) )
    shift_moves=[ move for move in moves if move[0] != exchange_programs ]
    shift_mapping = build_moves_map( shift_moves )
    thousand_shift_mapping = build_moves_map( [(apply_moves_map, shift_mapping)]*1000 )

    swap_moves=[ move for move in moves if move[0] == exchange_programs ]
    swap_mapping = build_swap_map( swap_moves )
    thousand_swap_mapping = build_swap_map( [(apply_swap_map, swap_mapping)]*1000 )
    
    for i in range( int( iterations / 1000 ) ):
        new_positions = apply_moves_map( new_positions, thousand_shift_mapping )
        if iterations > 10 and i % int(iterations/10) == 0:
            print( i )
        #for move in shift_moves:
        #    new_positions = move[0]( new_positions, move[1] )
    #print( new_positions )
    #swap_moves = reduce_swaps( swap_moves )
    for i in range( int( iterations / 1000 ) ):
        new_positions = apply_swap_map( new_positions, thousand_swap_mapping )
        if iterations > 10 and i % int(iterations/10) == 0:
            print( i )
        #for move in swap_moves:
        #    new_positions = move[0]( new_positions, move[1] )
    #print( shift_moves )
    return new_positions
    
# imkn hbla dcpf jego  is incorrect
#test1()
#test2()
print( ''.join( prog() ) )        
        