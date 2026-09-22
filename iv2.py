def sum_elements_dn(div, nondiv, count): 
    zoznam=[]
    k=count
    n=1
    while k>0:
        if (n*div) % nondiv != 0:
            zoznam.append(n*div)
            k=k-1
            n=n+1
        else:
            n=n+1    
    return sum(zoznam)
print(sum_elements_dn(3, 6, 3))