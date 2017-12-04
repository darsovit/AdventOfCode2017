#!python

sum=0

def find_line_value(line_ints):
    for i in range(0, len(line_ints)-1):
        for j in range(i, len(line_ints)):
            if ( i == j ):
                continue;
            if (line_ints[i] > line_ints[j]):
                if ( line_ints[i] % line_ints[j] == 0 ):
                    return int( line_ints[i] / line_ints[j] );
            elif ( line_ints[j] > line_ints[i] ):
                if ( line_ints[j] % line_ints[i] == 0 ):
                    return int( line_ints[j] / line_ints[i] );
            else:
                return 1            

with open('input.txt') as f:
    for line in f:
        int_list = [int(i) for i in line.split()]
        sum += find_line_value( int_list )
print (sum)
