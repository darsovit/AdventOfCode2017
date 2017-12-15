#!python

modValue = 2147483647

def int_generatorA( input ):
    return ( ( 16807 * input ) % modValue )

def generatorA( input ):
    newVal = int_generatorA( input )
    while ( newVal % 4 ) != 0:
        newVal = int_generatorA( newVal )
    return newVal
    
def int_generatorB( input ):
    return ( ( 48271 * input ) % modValue )

def generatorB( input ):
    newVal = int_generatorB( input )
    while ( newVal % 8 ) != 0:
        newVal = int_generatorB( newVal )
    return newVal
    
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
numPairs=5000000
  
for i in range(numPairs):
    a = generatorA( a )
    b = generatorB( b )
    if judge( a, b ):
        count += 1
    #print( "{0:10} {1:10} {2:10}".format( a, b, count ) )
    
print( count )
        