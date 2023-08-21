a,b=map(int,input().split())
if b-a==1 or a-b==1:
    print("Yes")
elif b==10 and a==1:
    print("Yes")
elif b==1 and a==10:
    print("Yes")
else:
        print("No")