def get_generation(cells, generations):
    height = len(cells)
    width = max(list(map(lambda x: len(x), cells)))

    for count in range(generations):

        #Enlarge world to check new life
        cells = [[0 for i in range(width)]]+cells[:]+[[0 for i in range(width)]]
        width+=2
        height+=2
        cells = map(lambda x: [0]+x[:]+[0], cells)

        #debug
        print "Lifetime:",count+1,"on",generations

        newcells = [[0 for i in range(width)] for j in range(height)]
        r = 0
        for row in cells:
            c = 0
            for col in row:
                neighbours = [[x,y] for x in range(r-1, r+2) for y in range(c-1, c+2)]
                neighbours.remove([r,c])
                alive = 0
                for i in neighbours:
                    try:
                        if (0 <= i[0] < height and 0 <= i[1] < width):
                            alive += cells[i[0]][i[1]]
                    except:
                        continue

                # Here decide to do. If i am alive or dead and to do based on alive neighbours
                if cells[r][c] == 1:
                    newcells[r][c] = 1 if 1<alive<4 else 0
                elif cells[r][c] == 0 and alive == 3:
                    newcells[r][c] = 1
                else:
                    newcells[r][c] = 0

                c+=1
            r+=1
        cells = newcells[:]

        # Crop the world around life

        # Crop rows
        topremove = 0
        for t in cells: # Top-Down Crop
            if all(map(lambda x: x==0, t)):
                topremove += 1
                height-=1
            else:
                break

        bottomremove = 0 # Bottom-Up Crop
        for t in reversed(cells): # Top-Down Crop
            if all(map(lambda x: x==0, t)):
                bottomremove -=1
                height-=1
            else:
                break

        cells = cells[topremove:bottomremove] if bottomremove != 0 else cells[topremove:]

        # Crop columns
        leftremove = 0
        for i in range(width):
            if all(map(lambda x: x[i]==0, cells)):
                leftremove += 1
            else:
                break

        rightremove = 0
        for i in reversed(range(width)):
            if all(map(lambda x: x[i]==0, cells)):
                rightremove -= 1
            else:
                break

        #print "Cropping Cols.."
        cells = map(lambda x: x[leftremove:rightremove], cells) if rightremove != 0 else map(lambda x: x[leftremove:], cells)
        width = width - leftremove + rightremove

        #print htmlize(cells)

    return cells
