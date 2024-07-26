def draw_map(coordinates, xdim, ydim) :

    
    dotti = ""
    for x in range(xdim) :
        for y in range(ydim) :
            dotto = "."
            for m, n in coordinates :
                if (m,n) == (x,y) :
                    dotto = "X"
                    #dotti = dotti + "X"
                            
            dotti = dotti + dotto

        dotti = dotti + "\n"
    

    return dotti 
    
def move(coordinates, snake_lenght, xdim, ydim) :
    
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
    
    
    return coordinates[(len(coordinates)-snake_lenght):]

print("Now for real")
xdim = 10
ydim = 10
#coordinates = [(0,0),(0,1),(0,2),(0,3)] #starting snake
coordinates = [[0,0],[0,1],[0,2],[0,3]] #starting snake
SL = 4  # snake length at beginning
while 1 : 
    print(draw_map(coordinates, xdim, ydim))
    print(coordinates)
    coordinates = move(coordinates,SL,xdim,ydim)
    print(coordinates)
    OnOff = input("Snek moved! Type 'end' to stop :  ")
    print(coordinates)
    if OnOff == "end" :
        break

