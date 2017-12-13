#!python

def calculate_collision( step, range, delay ):
    print( "calculate_collision(", step, ",", range, ",", delay, "), detects position of scanner at:", (step+delay) % ( (range-1)*2) )
    return ( (step+delay) % ( (range-1) * 2 ) ) == 0

def calculate_cost( step, state, delay ):
    if step in state['layer']:
        if calculate_collision( step, state['layer'][step], delay ):
            return step * state['layer'][step]
    return 0

def parse_line( line, state ):
    (layer, range) = line.split(': ')
    state['layer'][int(layer)] = int(range)


state={}
state['layer']={}

with open('input.txt') as f:
    for line in f:
        parse_line( line.strip(), state )

#state['layer'][0] = 3
#state['layer'][1] = 2
#state['layer'][4] = 4
#state['layer'][6] = 4

cost=0
delay=0
for step in range( 0, max( state['layer'].keys() )+1 ):
    cost += calculate_cost( step, state, delay )

print( "cost to leave with no delay: ", cost )

while ( cost > 0 ):
    delay += 1
    cost = 0
    for step in range( 0, max(state['layer'].keys() )+1 ):
        cost = calculate_cost( step, state, delay )
        if cost > 0:
            print( "delay: ", delay, " leads to failure in step: ", step )
            break

# 156052 is not correct
print( "delay to leave out without any cost: ", delay )