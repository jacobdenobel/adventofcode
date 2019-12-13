from math import gcd
from functools import reduce
from re import findall
from dataclasses import dataclass
from itertools import combinations

def lcm(a,b):
    return (a*b) // gcd(a,b)

@dataclass
class XYZBase:
    x: int
    y: int
    z: int

    def __iter__(self):
        for element in (self.x, self.y, self.z,):
            yield element 

    def __getitem__(self, *a, **kw):
        return self.__getattribute__(*a, **kw)
    
    def __setitem__(self, key, value):
        self.__dict__[key] = value

@dataclass
class Position(XYZBase):
    pass

@dataclass
class Velocity(XYZBase):
    pass

class Moon:
    def __init__(self, x, y, z):
        self.pos = Position(x, y, z)
        self.vel = Velocity(0, 0, 0)
        self.initial_state = self.state

    def apply_gravity(self, other):
        for dim, own_pos, other_pos, own_vel, other_vel in zip(
                ["x", "y", "z"], self.pos, other.pos,
                self.vel, other.vel):
            if own_pos > other_pos:
                self.vel[dim] -= 1
                other.vel[dim] += 1
            elif own_pos < other_pos:
                self.vel[dim] += 1
                other.vel[dim] -= 1
                
    def apply_velocity(self):    
        for dim, pos, vel in zip(["x", "y", "z"], self.pos, self.vel):
            self.pos[dim] += vel
        return self

    @property
    def state(self):
        return {i:(self.pos[i], self.vel[i],) for i in ["x", "y", "z"]}
    
    def in_previous_state(self, axis=None):
        if axis:
            return self.state[axis] == self.initial_state[axis]
        return self.state == self.initial_state
    
    @property
    def potential_energy(self):
        return sum((abs(i) for i in self.pos))

    @property
    def kinetic_energy(self):
        return sum((abs(i) for i in self.vel))
        
    @property
    def total_energy(self):
        return self.potential_energy * self.kinetic_energy

    def __repr__(self):
        return f"{self.pos}, {self.vel}"
        

class System:
    def __init__(self, moons):
        self.moons = [Moon(*moon) for moon in moons]
        self.pairs = list(combinations(self.moons, 2))

    @property
    def total_energy(self):
        return sum((moon.total_energy for moon in self.moons))

    def simulate(self, t, verbose=False):
        periods = dict()
        for t in range(1, t+1):
            for m1, m2 in self.pairs:
                m1.apply_gravity(m2)
            
            for m in self.moons:
                m.apply_velocity()
            
            for axis in ("x", "y", "z"):
                if not axis in periods:
                    if all([m.in_previous_state(axis) 
                            for m in self.moons]):
                        periods[axis] = t
                
            if len(periods) == 3:
                initial_state = reduce(lcm, periods.values())
                return initial_state
                               
            if verbose:
                self.print_moons()

    def print_moons(self):
        for moon in self.moons:
            print(moon)

    


if __name__ == "__main__":
    system = System([
        (-1, 0, 2), 
        (2, -10, -7), 
        (4, -8, 8), 
        (3, 5, -1)
    ])
    system.simulate(t=10)
    assert system.total_energy == 179
    

    system = System([
        [-8, -10, 0],
        [5, 5, 10],
        [2, -7, 3],
        [9, -8, -3]
    ])
    system.simulate(100)
    assert system.total_energy == 1940

    with open("inputs/inputdaytwelve.txt") as f:
        data = [
            list(map(int, findall(r'[-+]?\d+',x))) for x in f.readlines()
        ]
    
    system = System(data)
    system.simulate(t=1000)
    assert system.total_energy == 8538

    system = System(data)
    assert system.simulate(t=int(1e10)) == 506359021038056

