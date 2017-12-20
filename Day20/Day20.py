#!python


with open('input.txt') as f:
    count=0
    for line in f:
        (point, velocity, accel) = line.strip().split(', ')
        print('point:', point, ', velocity:', velocity, ', acceleration:', accel )
