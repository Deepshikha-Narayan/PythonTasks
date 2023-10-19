#Fibonacci series(0,1,1,2,3,5,8,13)

n=7
num1=0
num2=1
next_num=num2
count=1

while count<=n:
    print(next_num)
    count+=1
    num1,num2=num2,next_num
    next_num=num1+num2
print()