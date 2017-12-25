#!python

def read_input():
    input=[]
    with open('input.txt') as file:
        for line in file:
            input.append(line.strip())
    return input

def read_sample():
    input=[]
    input.append('0/2')
    input.append('2/2')
    input.append('2/3')
    input.append('3/4')
    input.append('3/5')
    input.append('0/1')
    input.append('10/1')
    input.append('9/10')
    return input

def build_graph( graph, input ):
    for line in input:
        (left, right) = line.split('/')
        if left not in graph['node']:
            graph['node'][left] = {}
        if right not in graph['node']:
            graph['node'][right] = {}
        graph['node'][left][right] = ( line, int(left)+int(right) )
        graph['node'][right][left] = ( line, int(left)+int(right) )

def find_strongest( graph, start_node, used_links, strength, length ):
    #print( "find_strongest, start_node:", start_node, ", used_links:", used_links, ", strength: ", strength )
    strongest_link=strength
    for link_node in graph['node'][start_node]:
        (link,this_strength) = graph['node'][start_node][link_node]
        if link not in used_links:
            my_set=set()
            my_set.add( link )
            this_strength=find_strongest( graph, link_node, used_links.union(my_set), strength+this_strength, length+1)
            if this_strength > strongest_link:
                strongest_link = this_strength
            if length+1 > graph['longest'][0]:
                graph['longest'] = ( length+1, this_strength )
            elif length == graph['longest'][0] and this_strength > graph['longest'][1]:
                graph['longest'] = ( length+1, this_strength )

    return strongest_link

def find_strongest_bridge( graph ):
    start_node='0'
    used_links=set()
    return find_strongest( graph, start_node, used_links, 0, 0 )

def print_graph( graph ):
    for node in sorted(graph['node'].keys()):
        print( node, ":", graph['node'][node] )

lines = read_input()
graph={}
graph['node']={}
graph['edge']={}
graph['longest']=(0,0)

build_graph( graph, lines )

print_graph( graph )
print( "strongest chain: ", find_strongest_bridge( graph ) )
print( "longest strongest: ", graph['longest'] )