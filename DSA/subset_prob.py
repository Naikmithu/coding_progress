#Print All Subsets of a Small Set

def printSubset(arr,k,cnt):
    
    def generate(curr_subset,index):
        nonlocal cnt #non local when used it will modify the outer count
        print(curr_subset)
        
        eve_sub = 0
        for j in curr_subset:
            if j%2 == 0:
                eve_sub +=0
            else :
                eve_sub +=1
        if len(curr_subset) == k:
            cnt+=1
        
        if eve_sub == 0:
            print(f"Even Subset : {curr_subset}")

        if sum(curr_subset) %2 == 0:
            print(f"Even sum subset :  {curr_subset}")
        
        print(f"Total Sum of subset : {sum(curr_subset)}")
        for i in range(index,len(arr)):
            generate(curr_subset+[arr[i]],i+1)
        
    generate([],0)
    return cnt


arr=[1,2,3,4]
k=0
print(printSubset(arr,k,0))
