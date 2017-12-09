#!python
import re

def strip_garbage( line ):
    found_start=-1
    ignore_next=0
    garbage_to_remove=[]
    garbage_count = 0
    for step in range(0, len(line) ):
        if found_start < 0:
            if line[step] == '<':
                found_start = step
        else:
            if ignore_next == 0:
                if line[step] == '!':
                    ignore_next=1
                elif line[step] == '>':
                    garbage_to_remove.append( (found_start, step) )
                    found_start=-1
                else:
                    garbage_count += 1
            else:
                ignore_next=0
    #print( 'line:', line, " garbage: ", garbage_to_remove )
    for step in range( len(garbage_to_remove), 0, -1 ):
        #print( "garbage step: ", step, ", tuple: ", garbage_to_remove[step-1] )
        new_line=line[0:garbage_to_remove[step-1][0]] + line[garbage_to_remove[step-1][1]+1:]
        line=new_line
    return ( line, garbage_count )

def count_and_score_groups( line ):
    depth=0
    total_score=0
    for step in range(0, len(line) ):
        if line[step] == '{':
            depth += 1
        elif line[step] == '}':
            total_score += depth
            depth -= 1
            assert( depth >= 0 )
    return total_score

def process_input( name, line ):
    #print (name, ", input: ", line )
    garbage_free=strip_garbage( line )
    #print (name, ", after strip:", line )
    total_score=count_and_score_groups( garbage_free[0] )
    print( name, 'score:', total_score )
    print( name, 'garbage score:', garbage_free[1] )

input_line=""
with open('input.txt') as f:
    for line in f:
        input_line=line

process_input( '{}', '{}' )
process_input( '{{{}}}', '{{{}}}' )
process_input( '{{},{}}', '{{},{}}' )
process_input( '{{{},{},{{}}}}', '{{{},{},{{}}}}' )
process_input( '{<{},{},{{}}>}', '{<{},{},{{}}>}' )
process_input( '{<a>,<a>,<a>,<a>}', '{<a>,<a>,<a>,<a>}' )
process_input( '{{<a>},{<a>},{<a>},{<a>}}', '{{<a>},{<a>},{<a>},{<a>}}' )
process_input( '{{<!>},{<!>},{<!>},{<a>}}', '{{<!>},{<!>},{<!>},{<a>}}' )
process_input( '{{<!!>},{<!!>},{<!!>},{<!!>}}', '{{<!!>},{<!!>},{<!!>},{<!!>}}' )
process_input( '{{<!!>},{<!!>},{<>},{<!!>}}', '{{<!!>},{<!!>},{<>},{<!!>}}' )

process_input( 'input.txt', input_line )
