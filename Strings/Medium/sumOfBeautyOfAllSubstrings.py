def getMinFreq(hash):
    minFreq = 500
    for f in hash.values():
        if f < minFreq:
            minFreq = f

    return minFreq

def beautySum(s):
    total = 0
    maxFreq = 1
    charFreqHash = {}
    for i in range(0, len(s)):
        charFreqHash[s[i]] = 1
        for j in range(i+1, len(s)):
            if s[j] not in charFreqHash:
                charFreqHash[s[j]] = 1
            else:
                charFreqHash[s[j]] += 1
                if charFreqHash[s[j]] > maxFreq:
                    maxFreq = charFreqHash[s[j]]
            minFreq = min(charFreqHash.values())
            total = total + maxFreq - minFreq

        charFreqHash.clear()
        maxFreq = 1

    return total

print(beautySum("pgljlqegfyqhs"))

            
