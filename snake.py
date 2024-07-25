def draw_map(coordinates) :
    xdim = 10
    ydim = 10
    
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
    
def move(coordinates) :
    
    direction = input("Wich direction to go? (n,s,e,w) : ")

    if direction == "n" :
        coordinates.append((coordinates[-1][0]-1, coordinates[-1][1]))
    elif direction == "s" :
        coordinates.append((coordinates[-1][0]+1, coordinates[-1][1]))
    elif direction == "e" :
        coordinates.append((coordinates[-1][0], coordinates[-1][1]+1))
    elif direction == "w" :
        coordinates.append((coordinates[-1][0], coordinates[-1][1]-1))
    
    return coordinates

print("Snake example:")
print(draw_map([(0,0), (0,1), (0,2), (0,3),(1,3), (2,3),(3,3), (3,4), (3,5)]))
print("mooove")
coordinates = [(2,2)]
coords = move(coordinates)
print(coords)

