

def zoznam(n)->list:
    inka=1
    p: list[int] = []
    while len(p) < n+1:
         for i in range(1,inka+1):
             p.append(i)
         inka+=1
    return p

def nested(n:int)->int:
    m=zoznam(n)
    return  m[n]



def nested_sum(n:int)->int:
    m=zoznam(n)
    return sum(m[0:n])
def main():
    assert nested(0) == 1
    assert nested(1) == 1
    assert nested(2) == 2
    assert nested(8) == 3
    assert nested(9) == 4
    assert nested(25) == 5
    assert nested(130) == 11

    assert nested_sum(2) == 2
    assert nested_sum(5) == 7
    assert nested_sum(13) == 26
    assert nested_sum(30) == 87
    assert nested_sum(100) == 500


if __name__ == "__main__":
    main()
