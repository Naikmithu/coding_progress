
def containsDupesK(num,k):
    
    dupes_index={}
    
    for i in range(len(num)):
        
        if num[i] in dupes_index:
            return True

        dupes_index[num[i]]=i
        
        if i >= k:
            dupes_index.pop(num[i-k])
    
    return False

        

num=[1,2,3,4,1]
k=4

print(containsDupesK(num,k))

#Linear time complexity
#space : O(K)