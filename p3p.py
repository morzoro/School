def largest_triple(max_side:int)->int:
    p=[]
    for a in range(1, max_side):
        for b in range(1,max_side): 
            if(((a**2 + b**2)**0.5) == int((a**2 + b**2)**0.5)):
                p.append((a**2+b**2)**0.5+a+b)
    return max(p) if p else 0
def main():
    assert largest_triple(10) == 24
    assert largest_triple(25) == 72
    assert largest_triple(100) == 288
    assert largest_triple(150) == 490
    assert largest_triple(1000) == 3290


if __name__ == "__main__":
    main()
