# Final Pyladies Project: Snake
#The snake is moving in a predefined grid, eats food and grows over the time. Game is over and the player loses when the snake hits the wall.

# random is needed for randomly placing the snake food
import random

# The map drawing function makes a long string and will place a dot "." everywhere on an arbitrary size map defined by xdim and ydim (rows and columns)
# Dots are placed everyhere except where there is the snake "X" defined "coordinates" or snake food "O" defined by "food_coordinates"
def draw_map(coordinates, xdim, ydim, food_coordinates) :

    dots = "" # initialize the map (string)
    for x in range(xdim) :
        for y in range(ydim) :
            dot = "."
            for m, n in coordinates :
                
                if (m,n) == (x,y) :
                    dot = "X" # place an "X" where the snake is 
                    
            for k, l in food_coordinates :
                if (k,l) == (x,y) :
                    dot = "O" # place an "O" where the snake food is
                                                
            dots = dots + dot # "append" the characters to map string

        dots = dots + "\n" # end-line at the end of each row
    
    return dots

# The move function takes user input for direction to move the snake's head by 1 step or exit game.
# The snakes body "coordinates" are taken as input and updated withe new position of the snake. 
# The argument and variable "coordinates" is a list of lists: a list of [x,y] pairs, and the snake's head is the last index.
# The function detects self- and wall-collisions via xdim an ydim and will return game over if that happens.
# The functions takes the input argument "SnakeGrows" to determine if the snake should remain the same length or grow 1 bit
def move(coordinates, xdim, ydim, SnakeGrows) :
    
    snake_lenght = len(coordinates) # The snake's length before the move, this lenght stay the same if the "SnakeGrows" = 0 (no food)
    # get user input, can be small or capital, its converted
    direction = input("Which direction to go? (n,s,e,w) \n Type 'end' to exit game. : ").strip().lower()
    # Snake goes north (up)
    if direction == "n" :
        if coordinates[-1][0]-1 > -1 : #check if snake reached the north (upper) border of the map, if not, then go further, else game over
            if [coordinates[-1][0]-1, coordinates[-1][1]] not in coordinates : # check if the snak is crossing itself, that is: the new coordinate given by the user is already in the "coordinates", if not, then append the new coordinate, else game over
                coordinates.append([coordinates[-1][0]-1, coordinates[-1][1]])
            else :
                print("GAME OVER! Snake bit itself (north).")
                return 0
        else :
            print("GAME OVER! Snake reached the top end on the map (north).") 
            return 0 # zero return value is evaluated outside the function and interpreted as game over
    # Snake goes south (down)    
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
    # Snake goes east (left)
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
    # Snake goes west (right)
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
    
    # The snake grows when it has eaten a food. One of the function's argument carries this information.
    # If the "SnakeGrows" argument is 0, then the snake's head "coordinates[-1]" did not meet the "food_coordinates" thus the length of the snake remains the same
    if SnakeGrows > 0 :
        output = coordinates # coordinates has an extra element due to the newly appended (x,y)
    else :
        output = coordinates[(len(coordinates)-snake_lenght):] # Loose the first coordinate if the snake did not grow.

    return output

# This function is checking whether the user-defined map size if greater than the minimum defined map size. If the defined map is NOK, this will be interpreted as an error. The map size is defined in code, not by terminal input.
def map_range_chk( xdim, ydim, xlim, ylim) :
    if xdim >= xlim :
        if ydim >= ylim :
            NOK = 0
        else :
            NOK = 1
    else : 
        NOK = 1

    return NOK

# This function adds an arbitrary number of randomly placed food on the map.
# Food is placed anywhere except where the snake is.
# The function returns a list of lists [[x,y], [..],..] with the coordinate of food "food_coordinates"
def add_food(xdim, ydim, coordinates, number_of_food) :
    food_coordinates = []
    food_cannot_be_placed = 1
    k = 0
    while food_cannot_be_placed :
        x = random.randint(0,xdim-1)
        y = random.randint(0,ydim-1)
        if [x, y] not in coordinates and [x, y] not in food_coordinates : # if the position is not already occupied by a previouly placed food, then place food
            food_coordinates.append([x,y])
            k = k + 1
            if k == number_of_food :
                food_cannot_be_placed = 0

    return food_coordinates

    


print("SNAKE 0.1")
# define map size
xdim = 10
ydim = 10
coordinates = [[0,0],[0,1],[0,2],[0,3]] #starting snake
SnakeGrows = 0  # 0 : snake stays the same length, 1: sneak grows
SnakeLength = len(coordinates)  # len(coordinates) or a constant, snake length at start or if limited
# Check the map dimensions
RangeChk = map_range_chk( xdim, ydim, 4, 1)
# Add initial foods
food_coordinates = add_food(xdim, ydim, coordinates,3) #e.g. add 3 pieces of sneak food

while 1 : 
    # See if map size was okay
    if RangeChk > 0 :
        print("Map size invalid. Map must be greater than (4,1). Please choose a different map size.")
        break
    # Show the map
    print(draw_map(coordinates, xdim, ydim, food_coordinates))
    # Make sneak move
    coordinates = move(coordinates, xdim, ydim, SnakeGrows)
    # Check if GAME OVER or exit criteria met
    if coordinates == 0 : 
        print("Game terminated (game over)!")
        break
    elif coordinates == 1 :
        print("Game terminaed (user quit game)!")
        break
    # Show updated map with moved snake
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
            #if food_coordinates_temp not in food_coordinates : put it somewhere else
            #    del food_coordinates[i]
                food_coordinates.append(food_coordinates_temp[0])
            break 
        else : 
            SnakeGrows = 0 # snake did not eat the food
    

# end of code