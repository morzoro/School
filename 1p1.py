
def sequence(n:int,k:int,initial:int)->int:
    final=initial
    for member in range(0,n):
        res=0
        for i in range(0,k):
         res+=((-1*final) if (i+1) % 2 == 1 else 1*final)*(i+1)
        final=res 
    return final
def main():
    assert sequence(2, 3, 2) == 8
    assert sequence(0, 1, 7) == 7
    assert sequence(1, 1, 7) == -7
    assert sequence(1, 2, 7) == 7
    assert sequence(1, 3, 7) == -14
    assert sequence(3, 1, 1) == -1
    assert sequence(2, 2, 2) == 2
    assert sequence(5, 5, 2) == -486
    assert sequence(3, 10, 1) == 125
    assert sequence(4, 10, 1) == 625
    assert sequence(4, 4, 4) == 64 
if __name__ == "__main__":
    main()
        