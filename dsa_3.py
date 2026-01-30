# li = [3,5,7,6,2,0,1]    
# for i in range (len(li)):
#     if(i%2 == 0):
#         print(li[i])
# for i in range (len(li)):
#     if(i%2 != 0):
#         print(li[i])

#  output = [3 7 2 1 5 6 0]

# //find max and min in a list
li = [1,3,2,4]
max = li[0]
min = li[0]

for i in li:
    if i > max:
        max= i
    if i < min:
        min = i

print("Max", max)
print("Min", min)
print("Sum:", min + max)


l = [1, 0, 3, 4]
total = 1
for i in l:
    total *= i
result = []
for i in l:
    result.append(total // i)
print(result)

# l=[2,0,3,4,0,5]
# total = 1
# for i in l:
#     total*= i
# result = [] 
# for i in l:
#     result.append(total // i if i != 0 else 0)
# print(result)