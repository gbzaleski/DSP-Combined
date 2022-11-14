 

def osob_brute(mat, n): # O(n^2)

    for p in range(n):
        is_known = 0
        knows = 0
        for i in range(n):
            is_known += mat[i][p]
            knows += mat[p][i]
        
        if is_known == n and knows == 1:
            return p + 1 # 0-indexing
    
    return None

def osob_lin(mat, n): # O(n)
    p = 0
    i = 0

    while i < n and p < n:
        if mat[p][i] == 1:
            p = i
        i = i + 1


    is_known = 0
    knows = 0;
    for i in range(n):
        is_known += mat[i][p]
        knows += mat[p][i]
    
    if is_known == n and knows == 1:
        return p + 1 # 0-indexing

    return None


if __name__ == "__main__":

    n = 4

    mat = [ # 3
        [1, 0, 1, 1],
        [1, 1, 1, 1],
        [0, 0, 1, 0],
        [1, 1, 1, 1]
    ]

    mat2 = [ # Null
        [1, 0, 1, 1],
        [1, 1, 1, 1],
        [0, 0, 1, 1],
        [1, 1, 1, 1]
    ]

    mat3 = [ # 4
        [1, 1, 1, 1],
        [0, 1, 1, 1],
        [1, 0, 1, 1],
        [0, 0, 0, 1]
    ]

    mat4 = [ # 1
        [1, 0, 0, 0],
        [1, 1, 1, 1],
        [1, 0, 1, 1],
        [1, 0, 0, 1]
    ]

    matx = mat2
    print((osob_brute(matx, n), osob_lin(matx, n)))