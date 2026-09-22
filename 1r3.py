def coins(value): 
    sum_of_coins=0
    coins1=5
    coins2=2
    coins3=1
    while value>=coins1:
        value=value-coins1
        sum_of_coins+=1
    while value>=coins2:
        value=value-coins2
        sum_of_coins+=1
    while value>=coins3:
        value=value-coins3
        sum_of_coins+=1
    return sum_of_coins
print(coins(-1))