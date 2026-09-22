def is_abundant(number): 
    p=0
    for i in range(1,number):
        if number%i==0:
            p+=i
    if(p < number):
        return "is abundant"
    else:
        return "is not abundant"
print(is_abundant(100))    