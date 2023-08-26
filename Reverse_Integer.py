num=int(input())
rev=0
flag=0
if num<0:
    num=num*-1
    flag=1
while(num!=0):
        rem=num%10
        rev=rev*10+rem
        num=num//10
if flag==1:
    print(rev*-1)
else:
    print(rev)