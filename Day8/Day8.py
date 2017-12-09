#!python

def get_reg_value( reg, state ):
    return state['reg'].get( reg, 0 )

def inc_reg_value( reg, value, state ):
    calculated_value = get_reg_value( reg, state ) + value
    if state['highest_value'] < calculated_value:
        state['highest_value'] = calculated_value
    state['reg'][reg] = calculated_value

def dec_reg_value( reg, value, state ):
    inc_reg_value( reg, -value, state )

def evaluate_condition( test_reg, condition, test_value, state ):
    if condition == '>':
        return get_reg_value( test_reg, state ) > test_value
    elif condition == '>=':
        return get_reg_value( test_reg, state ) >= test_value
    elif condition == '<':
        return get_reg_value( test_reg, state ) < test_value
    elif condition == '<=':
        return get_reg_value( test_reg, state ) <= test_value
    elif condition == '==':
        return get_reg_value( test_reg, state ) == test_value
    elif condition == '!=':
        return get_reg_value( test_reg, state ) != test_value


def parse_instruction( line, state ):
    instruction=line.split()
    target_reg=instruction[0]
    test_reg=instruction[4]
    value = int( instruction[2] )
    test_value = int( instruction[6] )
    condition = instruction[5]
    assert instruction[3] == 'if'
    if evaluate_condition( test_reg, condition, test_value, state ):
        if instruction[1] == 'inc':
            inc_reg_value( target_reg, value, state )
        else:
            dec_reg_value( target_reg, value, state )

instructions=[]
state={}
state['reg']={}
state['highest_value'] = 0
with open('input.txt') as f:
    for line in f:
        parse_instruction( line, state )

largest_value=0
for reg in state['reg']:
    if state['reg'][reg] > largest_value:
        largest_value = state['reg'][reg]
print( 'largest end value:', largest_value )
print( 'largest calculated_value:', state['highest_value'])
        
        
        
