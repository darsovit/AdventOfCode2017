#!python

def getpos( curpos, length, chain ):
    return ( curpos + length ) % len( chain )
    

def reverse_chain( curpos, length, chain ):
    for x in range( 0, int(length/2) ):
        swapfront = getpos( curpos, x,        chain )
        swapback  = getpos( curpos, length-x-1, chain ) 
        tmp = chain[swapfront]
        chain[swapfront] = chain[swapback]
        chain[swapback]=tmp

lengths=[]
with open('input.txt') as f:
    for line in f:
        lengths = [int(i) for i in line.split(',')]

chain = [ x for x in range(0,256) ]

skip=0
curpos=0
for x in range( 0, len(lengths) ):
    reverse_chain( curpos, lengths[x], chain )
    curpos = getpos(curpos, lengths[x] + skip, chain )
    skip += 1

print( chain )
print( "test value", chain[0] * chain[1] )

#minichain=[ x for x in range(0, 5) ]
#skip=0
#curpos=0
#lengths=[3, 4, 1, 5]
#for x in range( 0, len(lengths) ):
#    reverse_chain( curpos, lengths[x], minichain )
#    print( minichain )
#    curpos = getpos(curpos, lengths[x] + skip, minichain )
#    skip += 1
    
#print( minichain )

# 48180 is too high
