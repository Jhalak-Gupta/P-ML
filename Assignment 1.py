#Question1
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
print("Sum=",a+b)

#Question2
x=int(input("Enter the number:"))
if x%2==0:
    print("Even")
elif x%2!=0:
    print("odd")

#Question3
y=int(input("Enter the number:"))
fact=1
for i in range(1,y+1) :
    fact=fact*i
print("Factorial=",fact)

#Question4
name=input("Enter your name:")
print("Welcome",name)

#Question5

#Question6

#Question7
str=input("Enter the string:")
print("Length of the string=",len(str))

#Question8
str1=input("Enter 1st string:")
str2=input("Enter 2nd string:")
print(str1+str2)

#Question9
s=input("Enter the string:")
ss=input("Enter the sub string:")
sx=s.split()
c=0
for i in sx:
    if i==ss:
        c+=1
if c>0:
    print("The substring is present in the string")
else:
    print("The substring is not present in the string")

#Question10
strx=input("Enter the string:")
print(strx.upper())

#Question11
n=int(input("Enter the number of terms:"))
fib_series=[0, 1]
for i in range(2, n):
    nt=fib_series[-1]+fib_series[-2]
    fib_series.append(nt)
print(fib_series)

#Question12
num=eval(input("Enter the number:"))
sum=0
while num>0:
    d=num%10
    sum=sum+d
    num//=10
print("Sum of digits=",sum)

#Question13
py=int(input("Enter the present year:"))
by=int(input("Enter your birth year:"))
print("Age=",py-by)

#Question14

#Question15

#Question16
string=input("Enter the string:")
dict={}
for ch in string:
    if ch in dict:
        dict[ch]+=1
    else:
        dict[ch]=1
for key in dict:
    print(key,":",dict[key])

#Question17
st=input("Enter the string:")
print(st.title())

#Question18

#Question19

#Question20
l=eval(input("Enter the list of numbers:"))
sum=0
for i in l:
    sum=sum+i
print("sum=",sum)

#Question21
list=eval(input("Enter the list of numbers:"))
el=eval(input("Enter the element:"))
cnt=0
for i in range(0,len(list)):
    if el==list[i]:
        cnt+=1
if cnt==0:
    print("Not found")
else:
    print("Frequency=",cnt)

#Question22
lst=eval(input("Enter the list of numbers"))
print("Maximum Value=",max(lst))
print("Minimum Value=",min(lst))

#Question23

#Question24
Oper=input("Enter the operator (+,-,*,/): ")
num1=eval(input("Enter first number: "))
num2=eval(input("Enter second number: "))
if Oper == "+":
    print("Sum of the two numbers is ",num1+num2)
elif Oper == "*":
    print("Product of the two numbers is ",num1*num2)
elif Oper == "-":
    print("Difference of the two numbers is ",num1-num2)
elif Oper == "/":
    print("Quotient of the two numbers is ",num1/num2)
else:
    print("Invalid")

#Question25

#Question26
s1=input("Enter the string:")
sp=input("Enter the prefix:")
sf=input("Enter the suffix:")
if s1[0]==sp:
    print("String starts with the prefix")
else:
    print("String does not start with the prefix")
if s1[-1]==sf:
    print("String ends with the suffix")
else:
    print("String does not end with the suffix")

#Question27
stx=input("Enter the string:")
ls=[]
for ch in stx:
    ls.append(ch)
print(ls)
