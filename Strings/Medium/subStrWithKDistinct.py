def countSubStr(s,k):
    distinctElements = set()
    count = 0
    for i in range(0, len(s)):
        for j in range(i, len(s)):
            distinctElements.add(s[j])
            if len(distinctElements) == k:
                count += 1
            if len(distinctElements) > k:
                break
        distinctElements.clear()
    return count

print(countSubStr("aba",2))