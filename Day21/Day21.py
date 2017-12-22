#!python

converter={}

def add_converter( converter, line ):
    (input, output) = line.split(' => ')
    if len(input) == 5:
        converter[input]=output
    elif len(input) == 11:
        converter[input]=output
    else:
        assert( False and input )

def draw_pattern( pattern ):
    for line in pattern:
        print( line )

def get_two_piece( image, x, y ):
    start_x = x*2
    start_y = y*2
    piece="{0}/{1}".format( image[start_y][start_x:start_x+2], image[start_y+1][start_x:start_x+2] )
    return piece

def break_into_twos( image ):
    solution={}
    solution['divisions']=int(len(image)/2)
    solution['sections']={}
    sections={}
    for i in range( int(len(image)/2) ):
        for j in range( int(len(image)/2) ):
            solution['sections'][(i,j)] = get_two_piece( image, i, j )
    #print( 'image:', image, 'solution:', solution )
    return solution
    
def get_three_piece( image, x, y ):
    start_x = x*3
    start_y = y*3
    piece="{0}/{1}/{2}".format( image[start_y][start_x:start_x+3], image[start_y+1][start_x:start_x+3], image[start_y+2][start_x:start_x+3] )
    return piece
    
def break_into_threes( image ):
    solution={}
    solution['divisions']=int(len(image)/3)
    solution['sections']={}
    for i in range( int(len(image)/3) ):
        for j in range( int(len(image)/3) ):
            solution['sections'][(i,j)] = get_three_piece( image, i, j )
    return solution

def break_into_convertables( image ):
    if len(image) % 2 == 0:
        return break_into_twos( image )
    elif len( image ) % 3 == 0:
        return break_into_threes( image )


def rotate_pattern_2( pattern ):
    return "{3}{0}{2}{4}{1}".format( *list( pattern ) )

def rotate_pattern_3( pattern ):
    return "{8}{4}{0}{3}{9}{5}{1}{7}{10}{6}{2}".format( *list(pattern) )

def rotate_pattern( pattern ):
    if len(pattern) == 5:
        return rotate_pattern_2( pattern )
    else:
        assert( len(pattern) == 11 )
        return rotate_pattern_3( pattern )

def find_rotated_pattern( pattern, converter ):
    rotated_pattern = rotate_pattern( pattern )
    #print( rotated_pattern )
    if rotated_pattern in converter:
        return converter[rotated_pattern]
    rotated_pattern = rotate_pattern( rotated_pattern )
    #print( rotated_pattern )
    if rotated_pattern in converter:
        return converter[rotated_pattern]
    rotated_pattern = rotate_pattern( rotated_pattern )
    #print( rotated_pattern )
    return converter.get( rotated_pattern, None )

def flip_pattern( pattern ):
    lines=pattern.split('/')
    new_lines=[]
    for line in lines:
        new_lines.append( line[::-1] )
    return '/'.join( new_lines )

def find_conversion( pattern, converter ):
    #print( pattern )
    if pattern in converter:
        return converter[pattern]
    solution = find_rotated_pattern( pattern, converter )
    if solution is not None:
        return solution
    flipped_pattern = flip_pattern( pattern )
    #print( flipped_pattern )
    if flipped_pattern in converter:
        return converter[flipped_pattern]
    solution = find_rotated_pattern( flipped_pattern, converter )
    assert ( solution != None )
    return solution            

def add_piece_to_new_image( new_piece, new_image, num_sides, y, x ):
    #print( 'num_sides:', num_sides, 'y:', y, 'len(new_image):', len(new_image) )
    size_of_pieces=len(new_piece.split('/'))
    if ( len(new_image) <= y*size_of_pieces ):
        for parts in new_piece.split('/'):
            new_image.append( parts )
    else:
        count=0
        for part in new_piece.split('/'):
            new_image[ y*size_of_pieces + count ] = '{0}{1}'.format( new_image[y*size_of_pieces + count], part )
            count += 1

def build_new_image( pieces, converter ):
    new_image_pieces={}
    for key in pieces['sections'].keys():
        new_image_pieces[key]=find_conversion( pieces['sections'][key], converter )
    new_image=[]
    #print( pieces['divisions'] )
    for i in range( pieces['divisions'] ):
        for j in range( pieces['divisions'] ):
            add_piece_to_new_image( new_image_pieces[(j,i)], new_image, pieces['divisions'], i, j )
    return new_image

def count_lit_squares( image ):
    count=0
    for line in image:
        for char in line:
            if char == '#':
                count += 1
    return count

with open('input.txt') as file:
    for line in file:
        add_converter( converter, line.strip() )

image='.#./..#/###'.split('/')
#image='../.#'.split('/')
for i in range( 5 ):
    pieces = break_into_convertables( image )
    image=build_new_image( pieces, converter )
    print( i )
    draw_pattern(image)
print( count_lit_squares(image) )


