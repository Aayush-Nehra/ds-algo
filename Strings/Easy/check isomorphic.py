def createMapping(a, b):
    mapping = {}
    for i in range(len(a)):
        if a[i] not in mapping:
            mapping[a[i]] = b[i]

    return mapping

def createString(a, mapping):
    mappedStr = ""
    for i in range(len(a)):
        mappedStr += mapping[a[i]]

    return mappedStr

def isIsomorphic1(self, s: str, t: str) -> bool:
        #Failing edge case bada baba
        if len(s) != len(t):
            return False
        mapping  = {}
        newText = ""
        #CREATE MAPPING
        for i in range(len(s)):
            if s[i] not in mapping:
                mapping[s[i]] = t[i]

        for i in range(len(s)):
            newText += mapping[s[i]]

        if newText == t:
            return True
        else:
            return False

def isIsomorphic(s, t):
    #Brute force O(n) Space O(n)
    if len(s) != len(t):
        return False
    tempT = ""
    tempS = ""
    #CREATE MAPPING
    mappingS = createMapping(s, t)
    mappingT = createMapping(t, s)

    tempS = createString(s, mappingS)
    tempT = createString(t, mappingT)

    if tempS == t and tempT == s:
        return True
    else:
        return False

def isIsomorphic(self, s: str, t: str) -> bool:
        # Optimal TC = O(n^2) SC = O(n)
        data = {}
        for i, chr in enumerate(s):
            if chr not in data:
                if t[i] in data.values():
                    return False
                data[chr] = t[i]
            elif data[chr] != t[i]:
                return False
        return True
print(isIsomorphic("foo", "bar"))
