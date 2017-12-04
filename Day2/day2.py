#!python

sum=0

with open('input.txt') as f:
    for line in f:
        int_list = [int(i) for i in line.split()]
        sum += max(int_list)-min(int_list)
print (sum)
