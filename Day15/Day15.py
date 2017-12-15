#!python

modValue = 2147483647

def generatorA( input ):
    return ( ( 16807 * input ) % modValue )
    
def generatorB( input ):
    return ( ( 48271 * input ) % modValue )
    
def judge( a, b ):
    VALUE_MASK = 0b001111111111111111
    if ( a & VALUE_MASK ) == ( b & VALUE_MASK ):
        return True
    else:
        return False
     
#a=65
#b=8921
a=679
b=771   
count=0  
for i in range(40000000):
    a = generatorA( a )
    b = generatorB( b )
    if judge( a, b ):
        count += 1
    #print( "{0:10} {1:10} {2:10}".format( a, b, count ) )
    
print( count )
        