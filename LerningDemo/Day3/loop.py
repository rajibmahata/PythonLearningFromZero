

# for loop

i= 10

# for i in range(1,i):
#     print(i)

for i in range(1,i, i+1):
    print(f"{ i+1}:{i}")


items= [1,2,3,4,5,6,7,8,9,10]
num=5

for i in range(len(items)):
    if(items[i]==num): 
        print(f"Search completed at index:{i}")
        break




for i in range(5,10,2):
    print(i)

#while loop

print("while loop")
n=10 
j=0

while j<n:
    print(f"Value of j is {j}")
    j+=1    

#For example, if the user entered 10, the output should be 55 (1+2+3+4+5+6+7+8+9+10)

n= int(input("Enter a number:"))

sum=0
numofsum="("
for i in range(1,n+1,1):
    sum+=i
    numofsum+=str(i)
    if(i<n):
        numofsum+="+"
numofsum+=")"
print(f"Sum of {n} is {sum}{numofsum}")