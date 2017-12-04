#!python

def determine_shell(input):
    shell = 1
    while input > (shell * shell):
        shell += 2
    return shell
    
def distance_to_center_edge(input, shell):
    se_corner = shell*shell
    sw_corner = se_corner - (shell-1)
    nw_corner = sw_corner - (shell-1)
    ne_corner = nw_corner - (shell-1)
    min_pos   = ne_corner - (shell-2)
    midpoint  = 0
    if ne_corner > input:
        midpoint = ne_corner - int(shell/2)
    elif nw_corner > input:
        midpoint = nw_corner - int(shell/2)
    elif sw_corner > input:
        midpoint = sw_corner - int(shell/2)
    else:
        midpoint = se_corner - int(shell/2)
    return abs( input - midpoint )

input = 289326
shell = determine_shell( input )
print("shell", shell)
middle_distance = distance_to_center_edge( input, shell )
print("middle_distance", middle_distance)
distance_to_one = middle_distance + int(shell/2)
print("distance_to_one", distance_to_one)

    