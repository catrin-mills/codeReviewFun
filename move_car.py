directions = ['N','E','S','W'] 
movement = {'N': (0,1), 'E': (1,0), 'S': (0,-1), 'W':(-1,0)}
commands = {'L': 'turn_left', 'R': 'turn_right', 'M': 'move', 'T': 'travel_like_tardis'}

# General comments:
## 1) State what version of python you're using here.
## Note: I made some changes so that it woudl work in python3 (print(), xrange --> range, raw_input --> input)

## 2) There are no comments in general


## There is no handling if user tries
## to put the car outside of their created grid

## Tell the user what to input
GRID_MAX_X, GRID_MAX_Y = map(int, input("Create your vehicle x-y grid separated by a space. example: 10 10 ").split())

#Could your multiple vehicles just be in one array?
#eg, vehicle_x = [None]*num_vehicles
# but I guess your getting each vehicles position from the user.
# nevermind for now.

# It would be cool if instead of ignoring commands that move you off the grid,
# you just wrap them around (like old video games :0))

#variable names are intuitive and descriptive...nice job!
first_vehicle_x = None
first_vehicle_y = None

class Vehicle():
    def __init__(self, x, y, face):
        self.x = x
        self.y = y
        self.dir = face  ## be careful with dir as class

    def turn_left(self):
        self.dir = directions[(directions.index(self.dir)-1)%len(directions)]

    def turn_right(self):
        self.dir = directions[(directions.index(self.dir)+1)%len(directions)]

    def move(self):
        new_x = self.x + movement[self.dir][0]
        new_y = self.y + movement[self.dir][1]

        if new_x != first_vehicle_x or new_y != first_vehicle_y:
            if new_x in range(GRID_MAX_X+1):    
                self.x = new_x
            if new_y in range(GRID_MAX_Y+1):
                self.y = new_y
                
    def travel_like_tardis(self):
        import random
        new_x = int(random.uniform(0, GRID_MAX_X))
        #print (new_x)
        new_y = int(random.uniform(0, GRID_MAX_X))
        
        if new_x != first_vehicle_x or new_y != first_vehicle_y:
            if new_x in range(GRID_MAX_X+1):    
                self.x = new_x
            if new_y in range(GRID_MAX_Y+1):
                self.y = new_y

vehicle_one_pos = input().split()
vehicle_one_commands = input("'L': 'turn_left', 'R': 'turn_right', 'M': 'move', 'T': 'travel_like_tardis'")

vehicle_one = Vehicle(int(vehicle_one_pos[0]), int(vehicle_one_pos[1]), vehicle_one_pos[2])
for command in vehicle_one_commands:
    eval("vehicle_one.{0}()".format(commands[command]))

first_vehicle_x = vehicle_one.x
first_vehicle_y = vehicle_one.y

# Inputing format is not consistent
vehicle_two_pos = input().split()
vehicle_two_commands = input()

## typo:  ps --> pos
vehicle_two = Vehicle(int(vehicle_two_pos[0]), int(vehicle_two_pos[1]), vehicle_two_pos[2])
for command in vehicle_two_commands:
    eval("vehicle_two.{0}()".format(commands[command]))

print (vehicle_one.x, vehicle_one.y, vehicle_one.dir)
print (vehicle_two.x, vehicle_two.y, vehicle_two.dir)
