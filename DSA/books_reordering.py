from collections import defaultdict

class Solution:
    def rearrange(self, pages, shelf):
        # code here
        
        index_map = defaultdict(list)
        
        for i,v in enumerate(shelf):
            index_map[v].append(i)
        
        tot_cost=0
        
        
        for indexes in index_map.values():
            if len(indexes)>1:
                indexes.sort(key=lambda x:pages[x])
                
                for i in range(len(indexes)-1):
                    tot_cost+=pages[indexes[i]]
        
        return tot_cost
    