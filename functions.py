def sumR(num):
    if num > 1:
        return num + sumR(num - 1)
    else:
        return 1
    
def sumI(num):
    sum = 0
    
    for i in range(0,num - 1):
        sum += num
        
    return sum
    
def fibR(num):
    if num <= 2:
        return 1
    else:
        return fibR(num - 1) + fibR(num - 2)
    
print(sumR(999))
print("test")
print(sumI(999))