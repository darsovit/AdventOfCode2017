#!python

def get_value( state, val ):
    if 'a' <= val and val <= 'z':
        return state['reg'].get( val, 0 )
    else:
        return int( val )

def snd( state, tuple ):
    state['last_freq'] = get_value( state, tuple[0] )
    state['pc'] += 1

def set_reg( state, tuple ):
    state['reg'][tuple[0]] = get_value( state, tuple[1] )
    state['pc'] += 1

def add_reg( state, tuple ):
    state['reg'][tuple[0]] = get_value( state, tuple[0] ) + get_value( state, tuple[1] )
    state['pc'] += 1

def mul_reg( state, tuple ):
    state['reg'][tuple[0]] = get_value( state, tuple[0] ) * get_value( state, tuple[1] )
    state['pc'] += 1

def mod_reg( state, tuple ):
    state['reg'][tuple[0]] = get_value( state, tuple[0] ) % get_value( state, tuple[1] )
    state['pc'] += 1

def rcv( state, tuple ):
    if get_value( state, tuple[0] ) != 0:
        print("Recovered:", get_value( state, tuple[0] ) )
        exit()
    state['pc'] += 1

def jgz( state, tuple ):
    if ( get_value( state, tuple[0] ) > 0 ):
        state['pc'] += get_value( state, tuple[1] )
    else:
        state['pc'] += 1

def parse_instruction( state, line ):
    instr = line.split()
    if instr[0] == 'snd':
        assert len(instr)==2
        state['prog'].append( (snd, instr[1] ) )
    elif instr[0] == 'set':
        assert len(instr)==3
        state['prog'].append( (set_reg, (instr[1], instr[2]) ) )
    elif instr[0] == 'add':
        assert len(instr)==3
        state['prog'].append( (add_reg, (instr[1], instr[2]) ) )
    elif instr[0] == 'mul':
        assert len(instr)==3
        state['prog'].append( (mul_reg, (instr[1], instr[2]) ) )
    elif instr[0] == 'mod':
        assert len(instr)==3
        state['prog'].append( (mod_reg, (instr[1], instr[2]) ) )
    elif instr[0] == 'rcv':
        assert len(instr)==2
        state['prog'].append( (rcv, (instr[1]) ) )
    elif instr[0] == 'jgz':
        assert len(instr)==3
        state['prog'].append( (jgz, (instr[1], instr[2]) ) )
    else:
        print( line )
        assert False and instr[0]

def getcmd( state ):
    if state['pc'] >= 0 and state['pc'] < len( state['prog'] ):
        return state['prog'][state['pc']]
    return None

def run_prog( state ):
    cmd = getcmd( state )
    while cmd != None:
        print( cmd )
        cmd[0]( state, cmd[1] )
        print( state['reg'] )
        cmd = getcmd( state )
        
    
state={}
state['reg']={}
state['last_freq']=0
state['pc']=0
state['prog']=[]

with open('input.txt') as f:
    for line in f:
        parse_instruction( state, line.strip() )

run_prog( state )