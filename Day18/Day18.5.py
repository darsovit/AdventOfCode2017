#!python

def get_value( state, val ):
    if 'a' <= val and val <= 'z':
        return state['reg'].get( val, 0 )
    else:
        return int( val )

def snd( state, tuple ):
    val_to_send = get_value( state, tuple[0] )
    state['reg']['sendq'].append( val_to_send )
    state['reg']['msg_count'] += 1
    state['reg']['pc'] += 1

def set_reg( state, tuple ):
    state['reg'][tuple[0]] = get_value( state, tuple[1] )
    state['reg']['pc'] += 1

def add_reg( state, tuple ):
    state['reg'][tuple[0]] = get_value( state, tuple[0] ) + get_value( state, tuple[1] )
    state['reg']['pc'] += 1

def mul_reg( state, tuple ):
    state['reg'][tuple[0]] = get_value( state, tuple[0] ) * get_value( state, tuple[1] )
    state['reg']['pc'] += 1

def mod_reg( state, tuple ):
    state['reg'][tuple[0]] = get_value( state, tuple[0] ) % get_value( state, tuple[1] )
    state['reg']['pc'] += 1

def rcv( state, tuple ):
    if len( state['reg']['mq'] ) > 0:
        state['reg'][tuple[0]] = state['reg']['mq'].pop(0)
        state['reg']['blocked'] = 0
        state['reg']['pc'] += 1
    else:
        state['reg']['blocked'] = 1    
    
def jgz( state, tuple ):
    if ( get_value( state, tuple[0] ) > 0 ):
        state['reg']['pc'] += get_value( state, tuple[1] )
    else:
        state['reg']['pc'] += 1

def parse_instruction( prog, line ):
    instr = line.split()
    if instr[0] == 'snd':
        assert len(instr)==2
        prog.append( (snd, instr[1] ) )
    elif instr[0] == 'set':
        assert len(instr)==3
        prog.append( (set_reg, (instr[1], instr[2]) ) )
    elif instr[0] == 'add':
        assert len(instr)==3
        prog.append( (add_reg, (instr[1], instr[2]) ) )
    elif instr[0] == 'mul':
        assert len(instr)==3
        prog.append( (mul_reg, (instr[1], instr[2]) ) )
    elif instr[0] == 'mod':
        assert len(instr)==3
        prog.append( (mod_reg, (instr[1], instr[2]) ) )
    elif instr[0] == 'rcv':
        assert len(instr)==2
        prog.append( (rcv, (instr[1]) ) )
    elif instr[0] == 'jgz':
        assert len(instr)==3
        prog.append( (jgz, (instr[1], instr[2]) ) )
    else:
        print( line )
        assert False and instr[0]

def isblocked( prog, state ):
    if state['reg']['pc'] < 0 or state['reg']['pc'] >= len( prog ):
        # program is done; pc is off
        return true
    return state['reg']['blocked'] > 0 and len(state['reg']['mq']) == 0

def inctick( state ):
    state['reg']['tick'] += 1

def getcmd( prog, state0, state1 ):
    blocked0 = isblocked( prog, state0 )
    blocked1 = isblocked( prog, state1 )
    if blocked0 and blocked1:
        print( "state0:", state0 )
        print( "state1:", state1 )
        return( None, None )
    curstate=state0
    if blocked0:
        curstate=state1
    elif blocked1:
        curstate=state0
    elif state0['reg']['tick'] > state1['reg']['tick']:
        curstate=state1
    else:
        curstate=state0
    inctick( curstate )
    return( prog[curstate['reg']['pc']], curstate )    

def run_prog( prog, state0, state1 ):
    ( cmd, curstate ) = getcmd( prog, state0, state1 )
    while cmd != None:
        #print( cmd )
        cmd[0]( curstate, cmd[1] )
        #print( curstate )
        ( cmd, curstate ) = getcmd( prog, state0, state1 )
        
    
state0={}
state0['MyId']=0
state0['reg']={}
state0['reg']['p']=0
state0['reg']['pc']=0
state0['reg']['mq']=list()
state0['reg']['blocked']=0
state0['reg']['msg_count']=0
state0['reg']['tick']=0

state1={}
state1['MyId']=1
state1['reg']={}
state1['reg']['p']=1
state1['reg']['pc']=0
state1['reg']['mq']=list()
state1['reg']['blocked']=0
state1['reg']['msg_count']=0
state1['reg']['tick']=0

state1['reg']['sendq']=state0['reg']['mq']
state0['reg']['sendq']=state1['reg']['mq']

prog=[]

with open('input.txt') as f:
    for line in f:
        parse_instruction( prog, line.strip() )

run_prog( prog, state0, state1 )