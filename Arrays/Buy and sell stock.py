# O(N) Time and O(1) Space

def maxProfit(prices):
    n=len(prices)
    cost = 0
    maxcost = 0
    min_price = prices[0]
    if n == 0:
        return 0
    for i in range(n):
        min_price = min(min_price,prices[i])
        cost = prices[i] - min_price
        maxcost = max(maxcost,cost)
    return maxcost

if __name__ == '__main__':
    prices=[7,1,4,3,6,5]
    print(maxProfit(prices))

