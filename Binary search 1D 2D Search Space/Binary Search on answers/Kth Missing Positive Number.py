def findKthPositive(arr, k):
    """This solution is missing some test cases"""
    low = 0
    high = len(arr) - 1
    lastSeenNum = 0
    missingElementsForLastNum = 0

    while low <= high:
        mid = (low + high)// 2

        missingElements = arr[mid] - mid - 1

        if missingElements < k:
            low = mid + 1
            lastSeenNum = arr[mid]
            missingElementsForLastNum = missingElements
        elif missingElements > k:
            high = mid - 1
            lastSeenNum = arr[mid]
            missingElementsForLastNum = missingElements
        else:
            #lastSeenNum = arr[mid]
            if missingElementsForLastNum > k:
                return lastSeenNum - missingElementsForLastNum + 1
            return lastSeenNum + k - missingElementsForLastNum
    
    if missingElementsForLastNum > k:
                return lastSeenNum - missingElementsForLastNum + 1    
    return lastSeenNum + k - missingElementsForLastNum

def findKthPositive(arr, k):
    """
    The better approach would have been to find the two numbers between which the missing number
    will exist and that will be when low crosses high.
    So do a binary search on missing elements where low crosses high and the find the missing number based on
    the missing position.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high)//2
        missing = arr[mid] - mid - 1

        if missing < k:
            low = mid + 1
        else:
            high = mid - 1
    
    #answer will be arr[high] + something extra
    #something extra = k - missing at index high
    # ans = arr[high] + k - (arr[high] - high - 1)
    # ans = k + high + 1
    # ans = low + k 
    # eliminating arr[high] was also important because high might be -1 which means elements are missing from beginning which is not suitable

    return low + k

arr = [1,4,7,9,14,15,16,18,20,23,24,25,26,28,29,30,33,35,38,39,42,44,46,48,49,52,53,55,57,58,60,63,68,69,70]
k = 11

arr =  [2,3,4,7,11]
k = 5
print(findKthPositive(arr, k))