def frequencySort(s):
    hashMap = {}
    for ch in s:
        if ch not in hashMap:
            hashMap[ch] = 1
        else:
            hashMap[ch] += 1
    str = ""
    maxValue = 0
    for value in hashMap.values():
        if value > maxValue:
            maxValue = value

    while(maxValue!=0):
        keys = [k for k, v in hashMap.items() if v == maxValue]
        for key in keys:
            str += key * maxValue

        maxValue -= 1

    print(str)

frequencySort("bbbcaddd")