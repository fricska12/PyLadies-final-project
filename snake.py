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
    
    
print("Snake example:")
print(draw_map([(0,0), (0,1), (0,2), (0,3),(1,3), (2,3),(3,3), (3,4), (3,5)]))

