
#Reverse a integer number

num=int(input("Enter a number: "))
reverse=0

while num>0:
    remaninder=num%10
    reverse= reverse*10+remaninder
    num=num//10

print(f"Reverse of the number is: {reverse}")