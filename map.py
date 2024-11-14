import random
import os
import msvcrt
import copy

#Map Dimensions
width, height = [20,20]

#Terrain types
terrain = {
    'path': '\033[33m.\033[33m',
    'grass': '\033[32m*\033[32m',
    'player': '\033[31mX\033[31m',
    'gym': '\033[37mG\033[37m',
    'house':'\033[37m0\033[37m'
}   

#Create Map
def create_map(width = width, height= height):
    return [[terrain['path'] for _ in range(width)] for _ in range(height)]

def randomize_map(map,terrain=terrain):
    for y in range(len(map)):
        for x in range(len(map[0])):
            symbol = random.choices(list(terrain.keys())[:-3], weights= [60,40],k=1)[0]
            map[y][x] = terrain[symbol]
    
    rand_x = random.randint(0, len(map[0])-1)
    rand_y = random.randint(0, len(map)-1)
    house_cord = [rand_x,rand_y]

    while True:
        rand_x = random.randint(0, len(map[0])-1)
        rand_y = random.randint(0, len(map)-1)
        gym_cord = [rand_x,rand_y]
        if gym_cord != house_cord:
            break

    map[house_cord[1]][house_cord[0]] = terrain['house']
    map[gym_cord[1]][gym_cord[0]] = terrain['gym']

    return map,house_cord

#Display map
def display_map(map_data):
    for row in map_data:
        print(' '.join(row))

#Place player
def place_player(map, position):
    x, y = position
    prev = map[y][x]
    map[y][x] = terrain['player']
    return prev

def remove_player(map,old_position,prev_symbol):
    x, y = old_position
    map[y][x] = prev_symbol

#Player movement
def move_player(position, direction):
    x,y = position
    if direction == 'W' and y > 0:
        y -= 1
    elif direction == 'S' and y < height - 1:
        y += 1
    elif direction == 'A' and x > 0:
        x -= 1
    elif direction == 'D' and x < width - 1:
        x += 1
    return [x,y]

def get_key():
    return msvcrt.getch().decode('utf-8').upper()

