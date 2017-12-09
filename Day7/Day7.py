#!python

def process_line( state, line ):
    #print( line )
    
    line_contents=line.replace(",","").split()
    name=line_contents[0]

    state['progs'][name]={}
    #print( line_contents[1][1:-1] )
    state['progs'][name]['weight']=int(line_contents[1][1:-1])
    
    if len(line_contents) > 2:
        state['progs'][name]['held_up']=[]
        for friend in line_contents[3:]:
            state['progs'][name]['held_up'].append(friend)
            state['targets'].append(friend)

def find_total_weight( state, base ):
    state['progs'][base]['total_weight'] = state['progs'][base]['weight']

    if 'held_up' in state['progs'][base]:
        state['progs'][base]['weights_of_held']={}
        for item in state['progs'][base]['held_up']:
            held_weight=find_total_weight( state, item )
            if held_weight not in state['progs'][base]['weights_of_held']:
                state['progs'][base]['weights_of_held'][held_weight]=[]
            state['progs'][base]['weights_of_held'][held_weight].append(item)
            state['progs'][base]['total_weight'] += find_total_weight( state, item )
        if len( state['progs'][base]['weights_of_held'] ) == 1:
            state['progs'][base]['balanced'] = 1
    return state['progs'][base]['total_weight']
            

def find_out_of_balance( state, base ):
    for item in state['progs'][base]['held_up']:
        if 'balanced' not in state['progs'][item]:
            return find_out_of_balance(state, item)
    return base

def fix_size_of_out_of_balance( state, base, target ):
    for item in state['progs'][base]['held_up']:
        if 'balanced' not in state['progs'][item]:
            if target in state['progs'][item]['held_up']:
                target_weight=0
                print("Total weights: ")
                for weight in state['progs'][item]['weights_of_held']:
                    print( "totals: ", weight, state['progs'][item]['weights_of_held'][weight] )
                    if len(state['progs'][item]['weights_of_held'][weight]) > 1:
                        target_weight = weight
                return target_weight - ( state['progs'][target]['total_weight'] - state['progs'][target]['weight'] )
            else:
                return fix_size_of_out_of_balance( state, item, target )
        
state={}
state['targets']=[]
state['progs']={}

with open('input.txt') as f:
    for line in f:
        process_line( state, line )

base=""
for key in state['progs']:
    if key not in state['targets']:
        base=key
print ("calculating total weight of: ", base )
print ("total weight of", base, ":", find_total_weight( state, base ) )
out_of_balance=find_out_of_balance( state, base )
print ("prog out of balance: ", out_of_balance )
print ("fix size: ", fix_size_of_out_of_balance( state, base, out_of_balance ) )
print ( state['progs'][out_of_balance] )
print ( state['progs']['cwwwj'] )