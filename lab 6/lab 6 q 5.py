lst=[(12,23,55,0),(),(23,66),(43,91),()]

for i in lst:
    if i==():  
        lst.remove(i)

print('new list is: ',lst)
