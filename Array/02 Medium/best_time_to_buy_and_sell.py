from cmath import inf

def maxProfit(prices):
    """Brute force"""
    maxProfit = 0
    currentProfit = 0
    size = len(prices)
    for i in range(size):
        for j in range(i, size):
            currentProfit = prices[j] - prices[i]
            maxProfit = max(maxProfit, currentProfit)
    return maxProfit

print(maxProfit([1,1,1,2]))

def maxProfit2(prices):
    """Optimised learning from Kadane's algorithm"""
    maxProfit = 0
    minBuyPrice = 99999

    for i in range(len(prices)):
        minBuyPrice = min(minBuyPrice, prices[i])
        maxProfit = max(maxProfit, prices[i]-minBuyPrice)

    if maxProfit < 0:
        return 0
    
    return maxProfit

def maxProfit3(prices):
    """Optimised learning from Kadane's algorithm"""
    maxProfit = 0
    minBuyPrice = 99999

    for i in range(len(prices)):
        if prices[i] < minBuyPrice:
            minBuyPrice = prices[i]
        else: 
            maxProfit = max(maxProfit, prices[i]-minBuyPrice)

    if maxProfit < 0:
        return 0
    
    return maxProfit

print(maxProfit2([[7,6,4,3,1]]))