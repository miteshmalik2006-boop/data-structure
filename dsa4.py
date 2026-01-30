l1 = [3,4,5,6]
l2 = [3,2,3,2,3]
print(12)
#find the second largest element in a list.

l1 = [3,12,9,16,7,8]

largest = l1[0]
second_largest = l1[0]
for i in l1:
    if i>largest:
        second_largest = largest
        largest = i
    elif i>second_largest and i !=largest:
        second_largest = i
print("second largest:", second_largest)






num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)