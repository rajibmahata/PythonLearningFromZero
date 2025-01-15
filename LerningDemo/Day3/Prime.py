# prime number 

start = 25
end = 50

print("Prime numbers between", start, "and", end, "are:")

while start<end:
    flag = 0
    for i in range(2, start//2):
        #print(f"i:{i}, start:{start}, start//2:{start//2}")
        if start % i == 0:
            flag = 1
            break
    if flag == 0:
        print(start)
    start += 1