n=int(input())
a=False
for i in range(0,n//2):
    if i*(i+1)==n:
        a=True
if a:
    print("YES")
else:
    print("NO")