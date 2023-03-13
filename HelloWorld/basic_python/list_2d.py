matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][1])
print(matrix[1][1])
matrix[1][1] = 20
print(matrix[0][1])
print(matrix)

for row in matrix: # row contains 1 list fx first list is 1,2,3
    for item in row:
        print(item)