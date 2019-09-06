frqdic={}
stri="brontosaurus"
for j in stri:
    if j in frqdic:
        frqdic[j]+=1
    else:
        frqdic[j]=1

print(frqdic)
