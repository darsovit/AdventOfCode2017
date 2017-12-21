#!python

def get_next_velocity( v, a ):
    return ( v[0]+a[0], v[1]+a[1], v[2]+a[2] )

def any_axis_slowing( next_vel, cur_vel ):
    return abs(next_vel[0]) < abs(cur_vel[0]) or abs(next_vel[1]) < abs(cur_vel[1]) or abs(next_vel[2]) < abs(cur_vel[2])

def manhattan_distance( p ):
    return abs(p[0]) + abs(p[1]) + abs(p[2])

def displacement( vi, accel, t ):
    return vi * t + accel * int( ( t * (t+1) ) / 2 )

class Particle:
    def parse_xyz(self, some_str):
        parts = tuple( map( lambda x: int(x), some_str.split('=')[1].strip('<>').split(',') ) )
        return parts

    
    def __calculate_closest_to_origin_and_acceleration_away(self):
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

    def calculate_closest_to_origin_and_acceleration_away(self):
        return ( self.id, self.closest_to_origin, self.ticks_to_velocity_away, self.delta_accel )

    def __init__(self, id, p, v, a):
        self.id = id
        self.position = self.parse_xyz( p )
        self.velocity = self.parse_xyz( v )
        self.acceleration   = self.parse_xyz( a )
        self.manhattan_distances = []
        self.delta_accel = abs(self.acceleration[0]) + abs(self.acceleration[1]) + abs(self.acceleration[2])
        self.manhattan_distances.append( abs(self.position[0]) + abs(self.position[1]) + abs(self.position[2]) )
        ( some_id, self.closest_to_origin, self.ticks_to_velocity_away, tmp ) = self.__calculate_closest_to_origin_and_acceleration_away()        

    def location_at_tick( self, tick ):
        x = self.position[0]+displacement(self.velocity[0], self.acceleration[0], tick )
        y = self.position[1]+displacement(self.velocity[1], self.acceleration[1], tick )
        z = self.position[2]+displacement(self.velocity[2], self.acceleration[2], tick )
        return ( x, y, z )

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
max_ticks=0
for particle in particles:
    my_tuple = particle.calculate_closest_to_origin_and_acceleration_away()
    if max_ticks < my_tuple[2]:
        max_ticks = my_tuple[2]
    closest_data.append( my_tuple )

def getKey( data ):
    return data[3]

points_sorted_by_accel = sorted( closest_data, key=getKey )

particles_not_collided = set( particles )
for tick in range( max_ticks ):
    point_to_particles={}
    for particle in particles_not_collided:
        location_of_particle = particle.location_at_tick( tick )
        if location_of_particle in point_to_particles:
            point_to_particles[location_of_particle].append( particle )
        else:
            point_to_particles[location_of_particle]=[ particle ]
    for loc in point_to_particles.keys():
        if len( point_to_particles[loc] ) > 1:
            for particle in point_to_particles[loc]:
                particles_not_collided.remove( particle )

print( len( particles_not_collided ) )