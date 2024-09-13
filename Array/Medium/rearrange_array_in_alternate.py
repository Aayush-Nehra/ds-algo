def rearrangeArray(nums):
    """Loops"""
    arrangedList = []
    positiveScanPos = 0
    negativeScanPos = 0
    size = len(nums)
    while len(arrangedList) != size:
        if len(arrangedList) % 2 == 0:
            """Positive element loop"""
            for i in range(positiveScanPos, size):
                if nums[i] > 0:
                    positiveScanPos = i+1
                    arrangedList.append(nums[i])
                    break
        else:
            """Negative element loop"""
            for j in range(negativeScanPos, size):
                if nums[j] < 0:
                    negativeScanPos = j+1
                    arrangedList.append(nums[j])
                    break
    return arrangedList


def rearrangedArray2(nums):
    positiveList = []
    negativeList = []
    arrangedList = []
    for i in range(len(nums)):
        if nums[i]>0:
            positiveList.append(nums[i])
        else:
            negativeList.append(nums[i])

    for i in range(len(positiveList)):
        arrangedList.append(positiveList[i])
        arrangedList.append(negativeList[i])
    
    return arrangedList

def rearrangedArray3(nums):
    ans = []
    positiveElementPos = 0
    negativeElementPos = 1

    for i in range(len(nums)):
        if nums[i] < 0:
            ans[negativeElementPos] = nums[i]
            negativeElementPos += 2
        else:
            ans[positiveElementPos] = nums[i]
            positiveElementPos += 2

    return ans