# Write a Python code to print the following number pattern using a loop.

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5


n=5
for i in range(1,n+1,1):
    for j in range(1,i+1,1):
        print(j,end=" ")
    print()


# Write a Python program to print the reverse number pattern using a for loop.

# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1

n=5

print("Reverse number pattern")
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()