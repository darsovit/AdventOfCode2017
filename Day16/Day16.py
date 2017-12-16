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
        elif ( programs[i] == two_progs[1] ):
           programs[i] = two_progs[0]
           swapped1 = i
    assert( swapped0 != swapped1 )
    assert( swapped0 > -1 )
    assert( swapped1 > -1 )
    return programs

def handle_input( programs, move ):
    if move[0] == 's':
        return shift_programs( programs, int(move[1:]) )
    elif move[0] == 'x':
        return exchange_slots( programs, list(map(lambda x: int(x), move[1:].split('/')) ) )
    elif move[0] == 'p':
        return exchange_programs( programs, list(move[1:].split('/') ) )
    else:
        assert( False & move[0] )

def test1():
    test=[ 'a', 'b', 'c', 'd', 'e' ]
    assert( 'abcde' == ''.join( test ) )
    test=handle_input( test, 's1' )
    print( test )
    assert( 'eabcd' == ''.join( test ) )
    test=handle_input( test, 'x3/4' )
    print( test )
    assert( 'eabdc' == ''.join( test ) )
    test=handle_input( test, 'pe/b' )
    print( test )
    assert( 'baedc' == ''.join( test ) )

def test2():
    test=[ 'a', 'b', 'c', 'd', 'e' ]
    test = handle_input( test, 's3' )
    assert( 'cdeab' == ''.join(test) )
    
def prog():
    programs=list( map(lambda x: chr(ord('a')+x), range(16) ) )
    print( programs )
    new_positions=programs
    moves=[]
    with open('input.txt') as f:
        for line in f:
            moves = list( line.strip().split(',') )
    for i in range( 1000000000 ):
        for move in moves:
            new_positions = handle_input( new_positions, move )
    return new_positions
    
# imkn hbla dcpf jego  is incorrect
test1()
test2()
print( ''.join( prog() ) )        
        