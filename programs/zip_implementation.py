


# zip function implementation
matrix = [[1, 2, 3], [4, 5, 6]] 
# print(zip(*matrix))
# for i in zip(*matrix):
# 	print(i, type(i))

i , j = matrix
print(i, j)
for d in range(len(i)):
	print(tuple((i[d], j[d])))