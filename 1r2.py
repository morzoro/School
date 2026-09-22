def is_prime(number): 
    p=0
    for i in range(2,number):
                if number%i==0:
                    p+=1
    if p==0:
                return "je prvočíslo" 
    else:
                return "nie je prvočíslo"
print(is_prime(51111))  
print(is_prime(109999))           