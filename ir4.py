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
def fibfibsum(count): 
    zoznam=[]
    sum_of_fibonaci=0
    for i in range(1,count+1):
        zoznam.append(fibonaci(i))
    for i in zoznam:
        sum_of_fibonaci+=fibonaci(i)
    return sum_of_fibonaci    
print(fibfibsum(18))