stri=input("enter the string")
li=list(stri.split())
l=[]
rev=li[ : : -1]
print(" ".join(rev))
for w in rev:
    w=w[ : : -1]
    l.append(w)
print(" ".join(l))
