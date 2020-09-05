marks=[
    [8,3,4],
    [1,5,9],
    [6,7,2],
]
i=0
sum_row=0
sum_column=0
while i<len(marks):
    j=0
    sum_column+=marks[i][j]
    sum_row+=marks[j][i]
    i+=1
print(sum_row)
print(sum_column)
k=0
sum_diagonal=0
while k<len(marks):
    n=0
    while n<len(marks[k]):
        if k==n:
            sum_diagonal+=marks[k][n]
        n+=1
    k+=1
print(sum_diagonal)
if sum_column==sum_row==sum_diagonal:
    print("magic square")
else:
    print("not magic square")