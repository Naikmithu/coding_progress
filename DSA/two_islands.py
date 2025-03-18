def bfs(r,c):
            q = deque()
            vist.add((r,c))
            q.append((r,c))

            while q:
                row,col = q.popleft()
                directions = [(1,0),(-1,0),(0,1),(0,-1)]
                for dr,dc in directions:
                     r,c = row+dr,col+dc
                     if (r in range(rows) and c in range(cols) and grid[r][c]=='1'  and (r,c) not in vist):
                        q.append((r,c))
                        vist.add((r,c))



 count=0
 rows = len(grid)
 cols = len(grid[0])
 vist = set()
 for r in range(rows):
    for c in range(cols):
        if (r,c) not in vist and grid[r][c]=='1':
                    bfs(r,c)
                    count+=1
return count