#!python

def parse_line( line, state ):
	first=line.split(' <-> ')
	state['connections'][int(first[0])]=list(map(lambda x: int(x), first[1].split(', ')))
	print(state['connections'][int(first[0])])

state={}
state['connections']={}

with open('input.txt') as f:
	for line in f:
		parse_line( line.strip(), state )

state['indirect']={}
state['indirect'][0]=set( state['connections'][0] )
print( state['indirect'][0] )
endlen=len(state['indirect'][0])
startlen=0
while startlen < endlen:
	newset=state['indirect'][0]
	startlen=len(newset)
	for x in state['indirect'][0]:
		newset = newset | set( state['connections'][x])
	state['indirect'][0] = newset
	endlen=len(newset)
print( endlen )