def even(n): 
    vysledok=0
    for j in range(1,n+1):
            vysledok+=4*j**2
    return vysledok
print(even(10))