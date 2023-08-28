n=int(input())
a=n**2
b=len(str(n))
c=pow(10,b)
if a%c==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")