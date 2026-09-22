
def is_right(a,b,c):
    return True if a**2 + b**2 == c**2 else False
def is_perfect(a,b,c):
    return True if a==b and b==c else False
def spec(a,b,c):
    return True if (a==b and a!=c  or b==c and b!=a or a==c and a!=b) and a+b>c and b+c>a and a+c>b else False
print(is_right(1,2,3))
print(is_right(3,4,5))  
print(is_perfect(1,1,1))
print(is_perfect(1,2,1))
print(spec(100,7,7))
print(spec(2,2,3))
print(spec(1,1,1))