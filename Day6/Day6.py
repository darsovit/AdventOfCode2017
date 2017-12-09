#!python

def redistribute_memory_banks(memory_banks):
    max_mem_bank=0
    max_size=memory_banks[0]
    for i in range(1, len(memory_banks) ):
        if memory_banks[i] > max_size:
            max_size = memory_banks[i]
            max_mem_bank = i
    memory_banks[max_mem_bank] = 0
    target = max_mem_bank
    while max_size > 0:
        target = ( target + 1 ) % 16
        memory_banks[target] += 1
        max_size -= 1
    return memory_banks
    

memory_banks=[]

with open('input.txt') as f:
    for line in f:
        memory_banks=list(map(lambda x: int(x), line.split('\t') ))

key='.'.join(list(map(lambda x: str(x), memory_banks)))

steps=0
states={}
while key not in states:
    states[key] = steps
    steps += 1
    memory_banks = redistribute_memory_banks( memory_banks )
    key='.'.join(list(map(lambda x: str(x), memory_banks ) ) )

    
print( "states: ", states )
print( "steps: ", steps )
print( "steps for loop: ", steps - states[key] )