#!python

from math import sqrt

b = 81 * 100 + 100000
c = b + 17000
not_prime_count=0
for i in range( b, c+17, 17 ):
    d = 2
    prime=1
    while prime==1 and d < ( int( sqrt( i ) ) + 1):
        if i % d == 0:
            print( d, 'is a factor of', i )
            prime=0
        d += 1
    if prime==0:
         print( i, 'is not prime' )
         not_prime_count += 1
    else:
         print( i, 'is prime' )    
# 908 is too low
print( not_prime_count )