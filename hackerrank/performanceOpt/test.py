def reverse_numeric(x, y):  
    return y - x  

print  sorted([5, 2, 4, 1, 3], cmp=reverse_numeric)  