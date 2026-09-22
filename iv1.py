def nth_element_lv(p, q, index): 
    if index ==  0:
        return 0
    if index ==1:
        return p
    else:
        return p * nth_element_lv(p, q, index - 1) + q * nth_element_lv(p, q, index - 2)
print(nth_element_lv(2, 3, 5))    