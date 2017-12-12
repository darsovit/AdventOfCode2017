#!python

def parse_line( line, state ):
	first=line.split(' <-> ')
	state['connections'][int(first[0])]=list(map(lambda x: int(x), first[1].split(', ')))
	print(state['connections'][int(first[0])])

    
def build_group( state, base ):
    state['indirect'][base]=set( [ base ] )
    startlen=0
    endlen=1
    new_entries=state['indirect'][base]
    while startlen < endlen:
        origset=state['indirect'][base]
        newset=origset
        startlen=len(newset)
        for x in new_entries:
            newset = newset | set( state['connections'][x] )
        state['indirect'][base] = newset
        endlen=len(newset)
        new_entries = newset - origset
    for x in state['indirect'][base]:
        state['ingroup'][x] = base

state={}
state['connections']={}
state['indirect']={}
state['ingroup']={}

with open('input.txt') as f:
	for line in f:
		parse_line( line.strip(), state )


#state['indirect']={}
#state['indirect'][0]=set( state['connections'][0] )
#print( state['indirect'][0] )
#endlen=len(state['indirect'][0])
#startlen=0
#while startlen < endlen:
#	newset=state['indirect'][0]
#	startlen=len(newset)
#	for x in state['indirect'][0]:
#		newset = newset | set( state['connections'][x])
#	state['indirect'][0] = newset
#	endlen=len(newset)
for base in sorted(state['connections'].keys()):
    if base not in state['ingroup']:
        build_group( state, base )

print( len(state['indirect'][0]) )
print( len(state['indirect']) )