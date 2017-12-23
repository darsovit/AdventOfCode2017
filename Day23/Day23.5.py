#!python

def get_value( state, val ):
    if 'a' <= val and val <= 'z':
        return state['reg'].get( val, 0 )
    else:
        return int( val )

def snd( state, tuple ):
    state['reg']['snd'] = get_value( state, tuple[0] )
    state['reg']['pc'] += 1

def set_reg( state, tuple ):
    state['reg'][tuple[0]] = get_value( state, tuple[1] )
    state['reg']['pc'] += 1

def add_reg( state, tuple ):
    state['reg'][tuple[0]] = get_value( state, tuple[0] ) + get_value( state, tuple[1] )
    state['reg']['pc'] += 1

def sub_reg( state, tuple ):
    state['reg'][tuple[0]] = get_value( state, tuple[0] ) - get_value( state, tuple[1] )
    state['reg']['pc'] += 1

def mul_reg( state, tuple ):
    state['reg'][tuple[0]] = get_value( state, tuple[0] ) * get_value( state, tuple[1] )
    state['reg']['pc'] += 1
    state['count']['mul'] += 1

def mod_reg( state, tuple ):
    state['reg'][tuple[0]] = get_value( state, tuple[0] ) % get_value( state, tuple[1] )
    state['reg']['pc'] += 1

def rcv( state, tuple ):
    if get_value( state, tuple[0] ) != 0:
        print("Recovered:", state['reg']['snd'] )
        exit()
    state['reg']['pc'] += 1

def jgz( state, tuple ):
    if ( get_value( state, tuple[0] ) > 0 ):
        state['reg']['pc'] += get_value( state, tuple[1] )
    else:
        state['reg']['pc'] += 1

def jnz( state, tuple ):
    if get_value( state, tuple[0] ) != 0 :
        state['reg']['pc'] += get_value( state, tuple[1] )
    else:
        state['reg']['pc'] += 1

def parse_instruction( state, line ):
    instr = line.split()
    if instr[0] == 'set':
        assert len(instr)==3
        state['prog'].append( (set_reg, (instr[1], instr[2]) ) )
    elif instr[0] == 'mul':
        assert len(instr)==3
        state['prog'].append( (mul_reg, (instr[1], instr[2]) ) )
    elif instr[0] == 'sub':
        assert len(instr)==3
        state['prog'].append( (sub_reg, (instr[1], instr[2]) ) )
    elif instr[0] == 'jnz':
        assert len(instr)==3
        state['prog'].append( (jnz, (instr[1], instr[2]) ) )
    elif instr[0] == 'jgz':
        assert len(instr)==3
        state['prog'].append( (jgz, (instr[1], instr[2]) ) )
    else:
        assert( False and instr )

#    if instr[0] == 'snd':
#        assert len(instr)==2
#        state['prog'].append( (snd, instr[1] ) )
#    elif instr[0] == 'mod':
#        assert len(instr)==3
#        state['prog'].append( (mod_reg, (instr[1], instr[2]) ) )
#    elif instr[0] == 'rcv':
#        assert len(instr)==2
#        state['prog'].append( (rcv, (instr[1]) ) )
#    else:
#        print( line )
#        assert False and instr[0]

def getcmd( state ):
    if state['reg']['pc'] >= 0 and state['reg']['pc'] < len( state['prog'] ):
        return state['prog'][state['reg']['pc']]
    return None

def run_prog( state ):
    cmd = getcmd( state )
    while cmd != None:
        #print( cmd )
        cmd[0]( state, cmd[1] )
        #print( state['reg'] )
        cmd = getcmd( state )
        
    
state={}
state['reg']={}
state['reg']['pc']=0
state['prog']=[]
state['count']={}
state['count']['mul']=0
state['reg']['a']=1

with open('input2.txt') as f:
    for line in f:
        parse_instruction( state, line.strip() )

run_prog( state )
print( state['count']['mul'] )
print( state['reg'] )