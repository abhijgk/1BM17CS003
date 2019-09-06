def fun(li,key):
        return key in li
li=[x for x in input("Enter the list").split()]
print(li)
key=input("enter the key")
print(fun(li,key))
