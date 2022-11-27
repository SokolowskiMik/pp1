ma = [
        [1,2,3],
        [4,5,6],
        [7,8,9]]

mb = [
        [1,2,3,4,5],
        [6,7,8,9,0]]

mc = [5,6,7,8]

def transpose_matrix(m):
    try:
        rows = len(m)
        col = len(m[0])

        matrix_T = []

        for j in range(col):
            row = []
            for i in range(rows):
                row.append(m[i][j])
            matrix_T.append(row)

    except:
        col = len(m)

        matrix_T = []

        for i in range(col):
            matrix_T.append(m[i])
        
    return matrix_T

def disp(ar):
        for row in ar:
            print(row)

disp(ma)
print()
disp(transpose_matrix(ma))
print('--------')
disp(mb)
print()
disp(transpose_matrix(mb))
print('--------')
print(mc)
print()
disp(transpose_matrix(mc))

