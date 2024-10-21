def findMinMaxCowDistance(stalls):
    minDistance = 9999999999
    for i in range(len(stalls)-1):
        distance = stalls[i+1] - stalls[i]
        if distance < minDistance:
            minDistance = distance

    #print([minDistance, stalls[len(stalls)-1] - stalls[0]])
    return [minDistance, stalls[len(stalls)-1] - stalls[0]]

def checkCowPlacementPossibleForDistance(stalls, k, dist):
    i = 1 #placed first cow in stall 0
    k -= 1 # k-1 cows to be arranged in stalls
    prevCowPos = 0
    while i < len(stalls):
        if stalls[i] - stalls[prevCowPos] >= dist:
            #cow can be placed
            prevCowPos = i
            k -= 1
            i += 1

        else:
            i += 1
        
        if k == 0:
            break

    if k == 0:
        # print("possible")
        return True
    else:
        # print("not possible")
        return False

def findMinPossibleCowDist(arr, N, k):
    arr.sort()
    minCowDistance, maxCowDistance = findMinMaxCowDistance(arr)
    maxMinDist = 0
    for dist in range(minCowDistance, maxCowDistance+1):
        isDistancePossible = checkCowPlacementPossibleForDistance(arr, k, dist)
        if isDistancePossible:
            maxMinDist = dist
        else:
            break

    print(maxMinDist)
    return maxMinDist

def findMinPossibleCowDistBinarySearch(arr, N, k):
    arr.sort()
    low, high = findMinMaxCowDistance(arr)

    while low <= high:
        midDistance = (low + high)//2
        isDistancePossible = checkCowPlacementPossibleForDistance(arr, k, midDistance)

        if isDistancePossible:
            low = midDistance + 1
        else:
            high = midDistance - 1
    
    print(high)
    return high

N = 6
K = 4
arr = [0,3,4,7,10,9] 

# N = 5
# K = 2
# arr = [4,2,1,3,6]

#findMinMaxCowDistance(sorted(arr))
#checkCowPlacementPossibleForDistance(sorted(arr), K, 3)

findMinPossibleCowDistBinarySearch(arr, N, K)
        
