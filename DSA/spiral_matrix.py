



def spiral_matrix(matrix):
    
    row_st = 0
    row_ed = len(matrix)
    col_st = 0
    col_ed = len(matrix[0])
    
    while(row_st<row_ed and col_st<col_ed):
        for col in range(col_st,col_ed):
            print(matrix[row_st][col])
        
       
        row_st+=1
        
        for row in range(row_st,row_ed):
            print(matrix[row][col_ed-1])
        
        
        col_ed-=1 #By my logic we have to decrement by 2 but if i do that its will effect on further loops so handle it in for loop (by decreenting extra 1)
        
        if row_st < row_ed:
            for col in range(col_ed-1,col_st-1,-1): # like here col_ed-1
                print(matrix[row_ed-1][col])
            
            row_ed-=1
        
        if col_st < col_ed:
            for row in range(row_ed-1,row_st-1,-1):
                print(matrix[row][col_st])
            col_st+=1
       
def spiral_alternative(matrix):
    
    ret = []
    while matrix:
        ret+=matrix.pop(0) #first row 
        
        # append last element of each list 
        if matrix and matrix[0]:
            for row in matrix:
                ret.append(row.pop())
        # append last list in reverse
        if matrix :
            ret+=(matrix.pop()[::-1]) #matrix.pop() removes last list in matrix
            
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                ret.append(row.pop(0))
    
    print(ret)

matrix = [[0,1,2,],
          [3,4,5,],
          [6,7,8,]]

spiral_matrix(matrix)
spiral_alternative(matrix)


# Alternative approach :

