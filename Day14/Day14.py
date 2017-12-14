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

def knot_hash( input ):
    lengths = input + [ 17, 31, 73, 47, 23 ]
    chain = [ x for x in range(0,256) ]
    skip=0
    curpos=0
    for round in range( 0, 64 ):
        for x in range( 0, len(lengths) ):
            reverse_chain( curpos, lengths[x], chain )
            curpos = getpos(curpos, lengths[x] + skip, chain )
            skip += 1
    return chain

def reduce_hash( sparse_hash ):
    dense_hash=[]
    for x in range(0,16):
        startpos=x*16
        value = sparse_hash[startpos]
        for y in range(1,16):
            value = value ^ sparse_hash[startpos + y]
        dense_hash.append(value)
    return dense_hash


def convert_to_input( line ):
    return list( map( lambda x: ord(x), list(line) ) )

def dense_knot_hash( line ):
    sparse_hash = knot_hash( convert_to_input(line) )
    assert( 256 == len(sparse_hash) )
    dense_hash  = reduce_hash( sparse_hash )
    assert( 16 == len(dense_hash) )
    return dense_hash

def print_dense_hash( dense_hash ):
    hx=''
    for x in range( 0, len(dense_hash) ):
        hx = '%s%02x' % ( hx, dense_hash[x] )
    return( hx )

def build_disk_grid( key ):
    disk=[]
    for row in range( 0, 128 ):
        disk.append( dense_knot_hash( '%s-%s' % ( key, str(row) ) ) )
    return disk
    
#test_disk=build_disk_grid( 'flqrgnkx' )
#for i in range( 0, 8 ):
#    print( print_dense_hash( test_disk[i] ) )

def count_used_bits( disk_grid ):
    bits=0
    for row in range( 0, 128 ):
        for hash in range( 0, 16 ):
            bits += bin(disk_grid[row][hash]).count('1')
    return bits

puzzle_disk=build_disk_grid( 'ffayrhll' )
print( count_used_bits( puzzle_disk ) )