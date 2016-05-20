def longest_slide_down(pyramid):
    h = len(pyramid)
    n,l,tree=0,0,[]
    for row in pyramid:
        for col in row:
            tree.append({"n":n,"l":l,"v":col,"pow":0})
            n+=1
        l+=1
        
    for i in reversed(range(0,h)):
        for k in range(i*(i+1)/2, (i+1)*(i+2)/2):
            tree[k]["pow"] = tree[k]["v"] if i==h-1 else tree[k]["v"] + max(tree[tree[k]["n"]+tree[k]["l"]+1]["pow"], tree[tree[k]["n"]+tree[k]["l"]+2]["pow"])

    return tree[0]["pow"]

#test
print longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]])
