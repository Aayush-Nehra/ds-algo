def check(a):
    isIncreasing = False
    rotateVal = 0

    if len(a) == 1 or len(a) == 2:
        return True

    #Getting rotate val
    for i in range(len(a)-1):
        if(a[i]<=a[i+1]):
            rotateVal += 1
            isIncreasing = True
        else:
            rotateVal += 1
            isIncreasing = False
            break

    if isIncreasing:
        return True
    else:
        last_highest = a[len(a)-1]
        for i in range(rotateVal, len(a)-1):
            if a[i]<=a[i+1]:
                isIncreasing = True
            else: 
                isIncreasing =  False
                break

        if isIncreasing and last_highest <= a[0]:
            return True
        elif last_highest <= a[0] and rotateVal == len(a)-1:
            return True
        else:
            return False

def check2(nums):
    c=0
    for i in range(len(nums)):
        if nums[i]>nums[(i+1)%len(nums)]:
            c+=1
        if c>1:
            return False
    return True
                
print(check2([3,4,5,1,2]))
# print(check([2,1,3,4]))
# print(check([1,2,3]))
# print(check([1]))
# print(check([1,1,1]))
# print(check([3,4,4,5,5,1,2,3]))
# print(check([4,1]))
print(check([6,10,6]))
