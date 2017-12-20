#!python

def get_next_velocity( v, a ):
    return ( v[0]+a[0], v[1]+a[1], v[2]+a[2] )

def any_axis_slowing( next_vel, cur_vel ):
    return abs(next_vel[0]) < abs(cur_vel[0]) or abs(next_vel[1]) < abs(cur_vel[1]) or abs(next_vel[2]) < abs(cur_vel[2])

def manhattan_distance( p ):
    return abs(p[0]) + abs(p[1]) + abs(p[2])

class Particle:
    def parse_xyz(self, some_str):
        parts = tuple( map( lambda x: int(x), some_str.split('=')[1].strip('<>').split(',') ) )
        return parts

    def calculate_closest_to_origin_and_acceleration_away(self):
        closest_distance = manhattan_distance( self.position )
        cur_pos       = self.position
        cur_vel       = self.velocity
        accel         = self.acceleration
        next_vel      = get_next_velocity( cur_vel, accel )
        ticks         = 0
        while any_axis_slowing( next_vel, cur_vel ):
            ticks += 1
            next_pos = get_next_velocity( cur_pos, next_vel )
            if manhattan_distance( next_pos ) < closest_distance:
                closest_distance = manhattan_distance( next_pos )
            cur_vel = next_vel
            next_vel = get_next_velocity( cur_vel, accel )
        return ( self.id, closest_distance, ticks, manhattan_distance( accel ) )

    def __init__(self, id, p, v, a):
        self.id = id
        self.position = self.parse_xyz( p )
        self.velocity = self.parse_xyz( v )
        self.acceleration   = self.parse_xyz( a )
        self.manhattan_distances = []
        self.delta_accel = abs(self.acceleration[0]) + abs(self.acceleration[1]) + abs(self.acceleration[2])
        self.manhattan_distances.append( abs(self.position[0]) + abs(self.position[1]) + abs(self.position[2]) )

    def __repr__(self):
        return "<Particle pos:%s vel:%s accel:%s>" % ( self.position, self.velocity, self.acceleration )
        
particles=[]
with open('input.txt') as f:
    count=0
    for line in f:
        (point, velocity, accel) = line.strip().split(', ')
        particles.append( Particle( count, point, velocity, accel ) )
        count += 1

closest_data=[]
for particle in particles:
    closest_data.append( particle.calculate_closest_to_origin_and_acceleration_away() )

def getKey( data ):
    return data[3]

for data in sorted( closest_data, key=getKey ):
    print( data )
#print( closest_data )