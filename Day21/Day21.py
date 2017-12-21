#!python

converter={}
converter[2]={}
converter[3]={}

def add_converter( converter, line ):
    (input, output) = line.split(' => ')
    if len(input) == 5:
        converter[2][input]=output
    elif len(input) == 11:
        converter[3][input]=output
    else:
        assert( False and input )

def draw_pattern( pattern ):
    for line in pattern:
        print( line )
    
with open('input.txt') as file:
    for line in file:
        add_converter( converter, line.strip() )

start_pattern='.#./..#/###'.split('/')
draw_pattern( start_pattern )

