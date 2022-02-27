arr=[1,2,3,4,5,6]
n=len(arr)
i,j=0,n-1
while(i<j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
    j-=1
    i+=1
print(arr)


# O(n/2)----> O(n)  



