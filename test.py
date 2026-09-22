def max_triple(max_side):
    p=[]
    max_perimeter = 0
    for a in range(1, max_side):
        for b in range(1,max_side): 
            if(((a**2 + b**2)**0.5) == int((a**2 + b**2)**0.5)):
                p.append((a**2+b**2)**0.5+a+b)
    return max(p) if p else 0
print(max_triple(100))