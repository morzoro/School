def amicable(a, b):
    def sum_of_divisors(n):
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors)
    
    if sum_of_divisors(a) == sum_of_divisors(b) and sum_of_divisors(b) == sum_of_divisors(a):
        return "is amicable"
    else:
        return "is not amicable"
print(amicable(12, 11))    