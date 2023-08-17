a,b,c=map(float,input().split())
if a+b>c and a+c>b and b+c>a:
    print("Valid triangle")
else:
    print("Invalid triangle")