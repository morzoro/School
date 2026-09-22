def next_multiple(number, k): 
    n=2
    l=k
    while l<number:
        l=n*k
        n=n+1
    return l
print(next_multiple(900000000, 899999999))
print(next_multiple(321,541 ))

def next_prime(number):
    while True:
        number+=1
        p=0
        for i in range(2,number):
            if number%i==0:
                p+=1
        if p==0:
            return number   
print(next_prime(8))      
     
        