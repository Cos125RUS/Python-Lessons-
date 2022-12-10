n = 23
i = 0
while n != 0:
    i = i*10 + (n%10)
    n //= 10
else:
    print('Finish')    

print(i)