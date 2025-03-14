def maxDepth(s):
    curDep = 0
    maxDep = 0

    for char in s:
        if char == "(":
            curDep += 1
            if curDep > maxDep:
                maxDep = curDep
        elif char == ")":
            curDep -= 1
        else:
            continue

    return maxDep

print(maxDepth("(1+(2*3)+((8)/4))+1"))