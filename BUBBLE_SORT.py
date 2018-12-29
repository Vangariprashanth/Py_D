arr=[5,3,4,2,1]
n=len(arr)
for i in range(len(arr)):
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
print(arr)