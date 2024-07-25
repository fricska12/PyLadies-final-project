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
        coordinates.append((coordinates[-1][0]-1, coordinates[-1][1]))
    elif direction == "s" :
        coordinates.append((coordinates[-1][0]+1, coordinates[-1][1]))
    elif direction == "e" :
        coordinates.append((coordinates[-1][0], coordinates[-1][1]+1))
    elif direction == "w" :
        coordinates.append((coordinates[-1][0], coordinates[-1][1]-1))
    
    SnekBit = 0
    # snake self-collison avoidance
    #for i in range(len(initial_coordinates)):
     #   if coordinates[-1] == initial_coordinates[i] :
      ##      SnekBit = 1
         #   print("Snek bit itself and its hurting! Choose another direction!")
        #else : 
         #   SnekBit = 0
    # wall collison check
    if coordinates[-1][0] >  ydim-2 :
            SnekBit = 1
            print("Snek bumped in the wall Horizontal! Choose another direction!")
    elif coordinates[-1][1] >  xdim-2  : 
            SnekBit = 1
            print("Snek bumped in the wall Vertical! Choose another direction!")

    
    if SnekBit == 1 :
        output = initial_coordinates
        print("Snekbit")
    else :
        output = coordinates[len(coordinates)-snake_lenght:]
    
    return output

print("Now for real")
xdim = 10
ydim = 10
coordinates = [(0,0),(0,1),(0,2),(0,3)] #starting snake
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

