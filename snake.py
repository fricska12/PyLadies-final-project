def draw_map(coordinates) :
    xdim = 50
    ydim = 50
    points = []
    point = list()
    dotti = ""
    for x in range(xdim) :
        for y in range(ydim) :
            dotto = "."
            for m, n in coordinates :
                if (m,n) == (x,y) :
                    dotto = "X"
                    #dotti = dotti + "X"
                
            
            dotti = dotti + dotto

            point.append(".")
            #points[x, y] = ["."]
        dotti = dotti + "\n"
    

    return dotti 
    
    
print("gedvàs seggpiton")
print(draw_map([(1,1),(4,5),(0,0)]))
print("NAAGY KIGYOOOO ajajaj!")
print(draw_map([(0,0), (0,1), (0,2), (0,3),(1,3), (2,3),(3,3), (3,4), (3,5)]))
#asf = draw_map(1)
#print(asf[1])
coordinates = [(1,2), (2,3), (3,4)]
a, b = coordinates[1]
print(coordinates[1][0])
print(a)
print(b)
#print("fosporkolt")
#print([".", ".", ".", "\n",".",".","."])
#print(".....................\n................")
#print("."+"."+ "."+ "\n"+"."+"."+".")