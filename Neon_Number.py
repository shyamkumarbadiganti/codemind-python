n=int(input())
s=0 
sq=n**2
while(sq!=0):
    r=sq%10 
    s+=r    
    sq//=10
if(s==n):
    print("Neon Number")
else:
    print("Not Neon Number")