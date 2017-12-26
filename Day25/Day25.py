#!python

def read_input():
    state={}
    state['tape']=set()
    state['steps']=0
    state['diag']=12172063
    state['current']='A'
    state['loc']=0
    state['A']=( (1, 1,'B'), (0,-1,'C') )
    state['B']=( (1,-1,'A'), (1,-1,'D') )
    state['C']=( (1, 1,'D'), (0, 1,'C') )
    state['D']=( (0,-1,'B'), (0, 1,'E') )
    state['E']=( (1, 1,'C'), (1,-1,'F') )
    state['F']=( (1,-1,'E'), (1, 1,'A') )
    return state
    
def read_sample():
    state={}
    state['tape']=set()
    state['steps']=0
    state['diag']=6
    state['current']='A'
    state['loc']=0
    state['A']=( (1, 1,'B'), (0,-1,'B') )
    state['B']=( (1,-1,'A'), (1, 1,'A') )
    return state

def run_step( state, current_state ):
    if current_state[1] in state['tape']:
        cur_val = 1
    else:
        cur_val = 0
    (new_val,step,new_state) = state[current_state[0]][cur_val]
    if new_val != cur_val:
        if new_val == 1:
            state['tape'].add( current_state[1] )
        else:
            state['tape'].remove( current_state[1] )
    return ( new_state, current_state[1]+step )

def run_to_diagnostic( state ):
    current_state=( 'A', 0 )
    for i in range( state['diag'] ):
        current_state=run_step( state, current_state )

state=read_input()
print( state )
run_to_diagnostic( state )
print( len( state['tape'] ) )