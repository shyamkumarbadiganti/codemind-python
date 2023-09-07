n=int(input())
l=[]
for i in str(n):
    l.append(i)
    s=set(l)
    li=list(s)
    st='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'
    for i in li:
        st+=i
if len(str(n))==len(st):
    print("Unique Number")
else:
    print("Not Unique Number")