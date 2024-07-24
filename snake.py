def draw_map(coordinates) :
    xdim = 10
    ydim = 10
    points = []
    point = list()
    for x in range(xdim) :
        for y in range(ydim) :
            point.append(".")
            #points[x, y] = ["."]
    return point 
    
    
print(draw_map(1))
print("fosporkolt")
print([".", ".", ".", "\n",".",".","."])
print(".....................\n................")
print("."+"."+ "."+ "\n"+"."+"."+".")