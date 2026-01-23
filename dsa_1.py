def palindrome(arr):
    if arr == arr[::-1]:
        print("palindrome")
    else:
        print("not palindrome")

arr = [1, 2, 3, 2, 1]
palindrome(arr) 


arr = [1, 2, 3, 4, 5]
i=0
j=len(arr)-1
flag=True
while i<j:
    if arr[i]!=arr[j]:
        flag=False
        break
    i+=1
    j-=1 


    arr = [3,4,7,6]
    sum=0
    for i in range(len(arr)):
        sum*=10
        sum+=arr[i]
    print(sum)