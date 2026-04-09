# Take a number from the user and find the number of digits in it?

def fun(number):
    count=0
    while number>0:
        count+=1
        number=number//10
    return count
number=int(input("enter a number:"))
print(f"The number of digits in {number} is {fun(number)}")      
