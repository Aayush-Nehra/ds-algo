def findMinLenStr(strs):
    minStrLen = 201
    for str in strs:
        if len(str) < minStrLen:
            minStrLen = len(str)

    return minStrLen

def longestCommonPrefix(strs):
    if len(strs) == 1:
        return strs[0]
    elif len(strs) == 0:
        return ""

    minStrLen = findMinLenStr(strs)
    commonPrefixLen = -1
    flag = 1
    for i in range(minStrLen):
        for j in range(1,len(strs)):
            if strs[j][i] != strs[j-1][i]:
                flag = 0
                break
        if j == len(strs)-1 and flag == 1:
            commonPrefixLen = i

    return strs[0][:commonPrefixLen+1]

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))