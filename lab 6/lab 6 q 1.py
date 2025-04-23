people=['selvi','anoksha',('sam',),('saadhya',)]

boy_count=0
girl_count=0

for i in people:
    if isinstance(i,tuple):
        boy_count+=1

    elif isinstance(i,str):
        girl_count+=1

print('number of boys= ',boy_count)
print('number of girls= ',girl_count)
