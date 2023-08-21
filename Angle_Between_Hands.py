n=(input())
l=n.split(":")
m=6*int(l[1])
h=(30*int(l[0]))+(.5*int(l[1]))
a=max(m,h)-min(m,h)
b=360-a
print(min(a,b))