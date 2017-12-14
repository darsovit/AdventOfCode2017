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
        knot_hash=dense_knot_hash( '%s-%s' % ( key, str( row ) ) )
        row=''
        for part in range(0, len(knot_hash) ):
            row = '{0}{1:0>8s}'.format(row, bin(knot_hash[part])[2:] )
        disk.append( row )
        #print( row )
    return disk
    
#test_disk=build_disk_grid( 'flqrgnkx' )
#for i in range( 0, 8 ):
#    print( print_dense_hash( test_disk[i] ) )

def count_used_bits( disk_grid ):
    bits=0
    for row in range( 0, 128 ):
        bits += disk_grid[row].count('1')
    return bits

def find_neighbor_regions( state, loc ):
    regions=set()
    if loc[0] > 0:
        region_id = state['sectormap'].get((loc[0]-1,loc[1]), -1)
        if ( region_id != -1 ):
            regions.add( region_id )
    if loc[1] > 0:
        region_id = state['sectormap'].get((loc[0],loc[1]-1), -1 )
        if ( region_id != -1 ):
            regions.add( region_id )
    return regions

def add_to_region( state, region_id, loc ):
    #print( "Adding to region: ", region_id, " for loc: ", loc )
    state['regions'][region_id].append( loc )
    state['sectormap'][loc] = region_id

def create_new_region( state, loc ):
    region_id = state['next_region']
    state['next_region'] += 1
    #print( "Create region: ", region_id, " for loc: ", loc )
    state['regions'][region_id]=[ loc ]
    state['sectormap'][loc] = region_id

def combine_regions( state, region_ids, loc ):
    #print( "combining regions: ", region_ids )
    lowest_region = min( region_ids )
    highest_region = max( region_ids )
    assert ( highest_region > lowest_region )
    sectors_from_highest = state['regions'].pop( highest_region, [] )
    assert ( len(sectors_from_highest) > 0 )
    for i in sectors_from_highest:
        state['sectormap'][i] = lowest_region
        state['regions'][lowest_region].append( i )
    state['regions'][lowest_region].append( loc )
    state['sectormap'][loc] = lowest_region

def determine_regions( disk_grid ):
    state={}
    state['regions']={}
    state['sectormap']={}
    state['next_region'] = 1
    
    for row in range( 0, 128 ):
        assert ( len( disk_grid[row] ) == 128 )
        for col in range( 0, 128 ):
            if disk_grid[col][row] == '1':
                region_set=find_neighbor_regions( state, (col, row) )
                if len(region_set) > 1:
                    combine_regions( state, region_set, (col, row) )
                elif len(region_set) == 1:
                    add_to_region( state, min(region_set), (col, row) )
                else: # regions empty
                    create_new_region( state, ( col, row ) )
    return state

puzzle_disk=build_disk_grid( 'ffayrhll' )
print( count_used_bits( puzzle_disk ) )
state=determine_regions( puzzle_disk )
# Answer 1602 is too high, so 1603 is out of the question as well!
print( len(state['regions']) )
