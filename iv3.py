def largest_on_path(num): 
    cisla=[num]
    while num>1:
        if num % 2==0:
            num=num/2
        else:
            num=3*num+1
        cisla.append(num)
    return max(cisla)
print(largest_on_path(7))