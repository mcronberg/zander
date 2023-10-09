a = [1,2,3,4,5,6,7,8,9,10]
print(len(a))
print(a[0])
print(a[3])
a[1] = 100
print(a[len(a)-1])
print(a)

for item in a:
    print(item)

for i in range(len(a)):
    print(str(i) + " " + str(a[i]))



# b = [1, "zander", 4, [5,2,7]]
# print(b)

# nedbør = [[100,200,350], []]

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(matrix[2][1])