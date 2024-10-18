def checkCapacitySatisfies(capacityForADay, weights, days):
    i = 0
    for _ in range(days):
        dayCapacityConsumed = 0
        while True:
            if i == len(weights):
                break
            dayCapacityConsumed += weights[i]
            i += 1
            if dayCapacityConsumed > capacityForADay:
                i -= 1
                break
            elif dayCapacityConsumed == capacityForADay:
                break
    
    if i == len(weights):
        # print("Satisfies")
        return True
    
    # print("Does not satisfy")
    return False

def shipWithinDays(weights, days):
    high = sum(weights)
    low = sum(weights)//days

    ans = 0
    while low <= high:
        mid = (low + high)//2
        isMidSatisfy = checkCapacitySatisfies(mid, weights, days)

        if isMidSatisfy:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    print(ans)
    return ans

weights = [1,2,3,4,5,6,7,8,9,10]
days = 5

# weights = [3,2,2,4,1,4] 
# days = 3

#checkCapacitySatisfies(6, weights, days)
shipWithinDays(weights, days)