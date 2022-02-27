a=[2]
max_1,min_1=a[0],a[0]
for i in range(1,len(a)):
    if a[i]>max_1:
        max_1=a[i]
    if a[i]<min_1:
        min_1=a[i]
print(max_1,min_1)
        