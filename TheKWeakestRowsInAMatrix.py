def kWeakestRows(mat, k):

    idx = 0
    result = []
    rank = []
    for i in range(len(mat)):
        s_counter = 0
        c_counter = 0
        for j in range(len(mat[0])):
            if mat[i][j]==1:
                s_counter+=1
            else:
                c_counter+=1
            
        
        result.append([s_counter,i])
            
    result.sort()
    for i in range(len(mat)):
        if i<k:
            rank.append(result[i][1])    
        
    return rank



mat =[[1,0],
      [1,0],
      [1,0],
      [1,1]]
k=4
print(kWeakestRows(mat,k))
