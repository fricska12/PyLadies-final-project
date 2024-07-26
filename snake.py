import random

def draw_map(coordinates, xdim, ydim, food_coordinates) :

    
    dotti = ""
    for x in range(xdim) :
        for y in range(ydim) :
            dotto = "."
            for m, n in coordinates :
                
                if (m,n) == (x,y) :
                    dotto = "X"
                    
            for k, l in food_coordinates :
                if (k,l) == (x,y) :
                    dotto = "O"
                                                
            dotti = dotti + dotto

        dotti = dotti + "\n"
    

    return dotti 
    
def move(coordinates, snake_lenght, xdim, ydim, SnakeGrows) :
    
    initial_coordinates = coordinates

    direction = input("Which direction to go? (n,s,e,w) : ")

    if direction == "n" :
        if coordinates[-1][0]-1 > -1 :
            if [coordinates[-1][0]-1, coordinates[-1][1]] not in coordinates : 
                coordinates.append([coordinates[-1][0]-1, coordinates[-1][1]])
            else :
                print("Snake bit itself (north). Choose another direction.")
        else :
            print("Snake reached the top end on the map (north). Choose another direction.")
    elif direction == "s" :
        if coordinates[-1][0]+1 < xdim :
            if [coordinates[-1][0]+1, coordinates[-1][1]] not in coordinates :
                coordinates.append([coordinates[-1][0]+1, coordinates[-1][1]])
            else :
                print("Snake bit itself (south). Choose another direction.")
        else :
            print("Snake reached the bottom end on the map (south). Choose another direction.")
    elif direction == "e" :
        if coordinates[-1][1]+1 < ydim :
            if [coordinates[-1][0], coordinates[-1][1]+1] not in coordinates :
                coordinates.append([coordinates[-1][0], coordinates[-1][1]+1])
            else :
                print("Snake bit itself (east). Choose another direction.")
        else :
            print("Snake reached the right side on the map (east). Choose another direction.")
    elif direction == "w" :
        if coordinates[-1][1]-1 > -1 :
            if [coordinates[-1][0], coordinates[-1][1]-1] not in coordinates :
                coordinates.append([coordinates[-1][0], coordinates[-1][1]-1])
            else :
                print("Snake bit itself (west). Choose another direction.")
        else :
            print("Snake reached the left side on the map (west). Choose another direction.")
    
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
food_coordinates = add_food(xdim, ydim, coordinates,1)

while 1 : 
   
    print("Food coord.:  ", food_coordinates)
    print(draw_map(coordinates, xdim, ydim, food_coordinates))
    coordinates = move(coordinates, SnakeLength, xdim, ydim, SnakeGrows)
    for i in range(len(food_coordinates)) :
        if coordinates[-1] == food_coordinates[i] : # snake ate a food
            SnakeGrows = 1
            SnakeLength = SnakeLength + 1
            food_coordinates_temp = add_food(xdim, ydim, coordinates,1) # generate new food 
            if food_coordinates_temp not in food_coordinates : # put it somewhere else
                print("Food coords:   ", food_coordinates[i] )
                print("Food coords temp:   ", food_coordinates_temp[0] )
                food_coordinates[i] = food_coordinates_temp[0]
        else : 
            SnakeGrows = 0 # snake did not eat the food

    print("Food coord.:  ", food_coordinates)
    OnOff = input("Snek moved! Type 'end' to stop :  ")

    if OnOff == "end" :
        break
    if RangeChk > 0 :
        print("Map size invalid. Map must be greater than (4,1)")
        break

