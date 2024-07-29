# Final Pyladies Project: Snake

#The snake is moving in a predefined grid, eats food and grows over the time. Game is over and the player loses when the snake hits the wall or the gamer wants to end the game.

import random


def draw_map(coordinates, xdim, ydim, food_coordinates) :

    dots = ""
    for x in range(xdim) :
        for y in range(ydim) :
            dot = "."
            for m, n in coordinates :
                
                if (m,n) == (x,y) :
                    dot = "X"
                    
            for k, l in food_coordinates :
                if (k,l) == (x,y) :
                    dot = "O"
                                                
            dots = dots + dot

        dots = dots + "\n"
    
    return dots
    
def move(coordinates, snake_lenght, xdim, ydim, SnakeGrows) :
    
    initial_coordinates = coordinates

    direction = input("Which direction to go? (n,s,e,w) \n Type 'end' to exit game. : ").strip().lower()

    if direction == "n" :
        if coordinates[-1][0]-1 > -1 :
            if [coordinates[-1][0]-1, coordinates[-1][1]] not in coordinates : 
                coordinates.append([coordinates[-1][0]-1, coordinates[-1][1]])
            else :
                print("GAME OVER! Snake bit itself (north).")
                #print("Snake bit itself (north). Choose another direction.")
                return 0
        else :
            print("GAME OVER! Snake reached the top end on the map (north).") 
            #print("Snake reached the top end on the map (north). Choose another direction.") 
            return 0
    elif direction == "s" :
        if coordinates[-1][0]+1 < xdim :
            if [coordinates[-1][0]+1, coordinates[-1][1]] not in coordinates :
                coordinates.append([coordinates[-1][0]+1, coordinates[-1][1]])
            else :
                print("GAME OVER! Snake bit itself (south).")
                return 0
        else :
            print("GAME OVER! Snake reached the bottom end on the map (south).")
            return 0
    elif direction == "e" :
        if coordinates[-1][1]+1 < ydim :
            if [coordinates[-1][0], coordinates[-1][1]+1] not in coordinates :
                coordinates.append([coordinates[-1][0], coordinates[-1][1]+1])
            else :
                print("GAME OVER! Snake bit itself (east).")
                return 0
        else :
            print("GAME OVER! Snake reached the right side on the map (east).")
            return 0
    elif direction == "w" :
        if coordinates[-1][1]-1 > -1 :
            if [coordinates[-1][0], coordinates[-1][1]-1] not in coordinates :
                coordinates.append([coordinates[-1][0], coordinates[-1][1]-1])
            else :
                print("GAME OVER! Snake bit itself (west).")
                return 0
        else :
            print("GAME OVER! Snake reached the left side on the map (west).")
            return 0
    elif direction == "end" : 
        return 1
    
    if SnakeGrows > 0 :
        output = coordinates
    else :
        output = coordinates[(len(coordinates)-snake_lenght):]

    return output

def map_range_chk( xdim, ydim, xlim, ylim) :
    if xdim >= xlim :
        if ydim >= ylim :
            NOK = 0
        else :
            NOK = 1
    else : 
        NOK = 1

    return NOK

def add_food(xdim, ydim, coordinates, number_of_food) :
    food_coordinates = []
    food_cannot_be_placed = 1
    k = 0
    while food_cannot_be_placed :
        x = random.randint(0,xdim-1)
        y = random.randint(0,ydim-1)
        if [x, y] not in coordinates and [x, y] not in food_coordinates :
            food_coordinates.append([x,y])
            k = k + 1
            if k == number_of_food :
                food_cannot_be_placed = 0

    return food_coordinates

    


print("Now for real")
xdim = 10
ydim = 10
#coordinates = [(0,0),(0,1),(0,2),(0,3)] #starting snake
coordinates = [[0,0],[0,1],[0,2],[0,3]] #starting snake
SnakeGrows = 0  # 0 : snake stays the same length, 1: sneak grows
SnakeLength = len(coordinates)  # len(coordinates) or a constant, snake length at start or if limited
RangeChk = map_range_chk( xdim, ydim, 4, 1)
# add initial foods
food_coordinates = add_food(xdim, ydim, coordinates,3)

while 1 : 
    # Check map size
    if RangeChk > 0 :
        print("Map size invalid. Map must be greater than (4,1)")
        break
    print(draw_map(coordinates, xdim, ydim, food_coordinates))
    coordinates = move(coordinates, SnakeLength, xdim, ydim, SnakeGrows)
    # Check if GAME OVER
    if coordinates == 0 : 
        print("game over")
        break
    elif coordinates == 1 :
        print("user quit")
        break
    # Update map with moved snake
    print(draw_map(coordinates, xdim, ydim, food_coordinates))
    
    # Check if snake found the food
    for i in range(len(food_coordinates)) :
        if coordinates[-1] == food_coordinates[i] : # snake ate a food
            SnakeGrows = 1
            SnakeLength = SnakeLength + 1
            del food_coordinates[i]
            # Only generate new food if the initial amount is eaten
            if len(food_coordinates)<1 :
                food_coordinates_temp = add_food(xdim, ydim, coordinates,1) # generate 1 new food 
            #if food_coordinates_temp not in food_coordinates : # put it somewhere else
            #    del food_coordinates[i]
                food_coordinates.append(food_coordinates_temp[0])
            break 
        else : 
            SnakeGrows = 0 # snake did not eat the food
    print(draw_map(coordinates, xdim, ydim, food_coordinates))
    print("Snake is at coordinates :   ", coordinates)
    
    #OnOff = input("Snek moved! Type 'end' to stop :  ")

    #if OnOff == "end" :
    #    break
    

