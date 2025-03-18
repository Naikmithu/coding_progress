# Greedy Algorithm :
# Two pointers iterate , for each l iterate r across and calculate profit,
# when r>l , we know we have iterated to all potential max profits , so move l to rand repeat 

# A Greedy Algorithm is a problem-solving method where you make the best choice at each step without thinking about future consequences.
# The idea is to take the locally optimal choice at every stage, 
# hoping that this leads to a globally optimal solution.

prices = [1,5,3,6,4]

l,r = 0,1

maxprofit=0

while r!=len(prices):
    if prices[l]<prices[r]:
        maxprofit=max(prices[r]-prices[l],maxprofit)
    else:
        l=r
    
    r+=1

print(maxprofit)


# Why is this a Greedy Algorithm?
# It makes the best choice at every step (always checking if selling today gives a better profit).
# It doesn’t go back and change past decisions.
# It keeps track of the lowest price seen so far to ensure optimal profit.
