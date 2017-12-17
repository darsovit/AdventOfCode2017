#!python

def insert_new_value( state, nextval ):
    curpos = ( state['pos'] + state['cStep'] ) % len(state['buffer'])
    #print('curpos:', curpos, ', buffer:', state['buffer'])
    #print('state[buffer][:curpos]', state['buffer'][:curpos])
    state['buffer'] = state['buffer'][:curpos+1] + [nextval] + state['buffer'][curpos+1:]
    #state['buffer'] = newbuf
    state['pos'] = curpos+1

circular_buffer=[]
state={}
state['pos'] = 0
state['buffer']=[0]
state['cStep']=367

for i in range(2017):
    insert_new_value( state, i+1 )

def find_pos( buffer, value ):
    for i in range(len(buffer)):
        if buffer[i] == value:
            return i
    return -1

def get_pos( buffer, pos ):
    return pos % len(buffer)
    
#print( state['buffer'] )
posOf2017 = find_pos( state['buffer'], 2017 )
print( 'next after 2017:', state['buffer'][get_pos(state['buffer'], posOf2017+1)] )

i = 2017
state['buflen'] = len( state['buffer'] )
state['afterzero'] = state['buffer'][1]
while i < 50000000:
    while state['cStep'] > ( state['buflen'] - state['pos'] ):
        state['buflen'] += 1
        state['pos'] += state['cStep'] + 1
        i += 1
    if state['pos'] + state['cStep'] % state['buflen'] == 0:
        state['afterzero'] = i+1
        i += 1
        state['buflen'] += 1
        state['pos'] = 1
        print('added after zero:', state['afterzero'] )
    else:
        state['buflen'] += 1
        state['pos'] = ( state['pos'] + state['cStep'] % state['buflen'] ) + 1
        i += 1
    
print( state['afterzero'] )