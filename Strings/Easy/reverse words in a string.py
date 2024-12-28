def reverseWords(s):
    words = s.split()
    ans = ""
    for i in range(len(words)-1, -1, -1):
        if len(words[i])!= 0:
            ans += words[i] + " "

    return ans.strip()

def reverseWords(s):
    words = s.split()
    reverseWords = words[::-1]
    return ' '.join(reverseWords)


print(reverseWords("a good   example"))