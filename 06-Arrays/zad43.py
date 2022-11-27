def identity_matrix(n):
    L = []
    for i in range(n):
        L.append([0]*n)
    
    
    j = 0
    for row in L:
        L[j][j] = 1
        j += 1
        
    # while j < n:
    #     L[j][j] = 1
    #     j += 1
    
    return L

def disp(ar):
    for r in ar:
        print(r)

disp(identity_matrix(3))
print()
disp(identity_matrix(5))
print()
disp(identity_matrix(8))
