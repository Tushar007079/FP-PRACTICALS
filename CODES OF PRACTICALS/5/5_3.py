def is_ident_mat(rows, cols, mat):
    if rows != cols:
        return False
    for i in range(rows):
        for j in range(cols):
            if i == j and mat[i][j] != 1:
                return False
            elif i != j and mat[i][j] != 0:
                return False
            return True


def is_bin_mat(rows, cols, mat):
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] not in [0, 1]:
                return False
            return True
rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))
mat = [[] for i in range(rows)]
for i in range(rows):
    inp = input(f"Enter the elements of row {i + 1}: ").split()
    for j in range(cols):
        mat[i].append(int(inp[j]))
for i in range(rows):
    print(mat[i])

ident_mat = 'YES' if is_ident_mat(rows, cols, mat) else 'NO'
bin_mat = 'YES' if is_bin_mat(rows, cols, mat) else 'NO'
print('Indentity Matrix: ', ident_mat)
print('Binary Matrix: ', bin_mat)
