vysledok=0
b=[[0,0],[1,1]]
def fibonaci(m):
    global b
    if len(b)>m and m!=0:
     if m==b[m][0]:
        return b[m][1]
    if m == 0:

        return 0
    if m == 1:
        return 1
    b.append([m,fibonaci(m-1) + fibonaci(m-2)])
    return fibonaci(m-1) + fibonaci(m-2)
def fibonacii(n):
     global vysledok,helper,pocet
     pocet=0
     helper=0
     while pocet<n:
         helper=3+helper
         k=fibonaci(helper)
         if k%2==0:
             pocet+=1
             vysledok+=k
     return vysledok        
print(fibonacii(3000))