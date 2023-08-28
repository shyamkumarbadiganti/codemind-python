a=int(input())
b=int(input())
s=0
d=0
for p in range(1,a):
    if a%p==0:
        s=s+p
for h in range(1,b):
    if b%h==0:
        d=d+h
if s==b and d==a:
    print("Amicable")
else:
    print("Not Amicable")