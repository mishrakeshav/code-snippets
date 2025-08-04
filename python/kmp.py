


def computeLPS(pattern):
    i = j = 0 
    lps = [0 for i in range(len(pattern))]
    i = 1 
    while i < len(pattern):
        while j > 0 and  pattern[i] != pattern[j]:
            j = lps[j - 1]
        
        if pattern[i] == pattern[j]:
            j += 1 

        lps[i] = j 
        i += 1 
    return lps


def search(pattern, text):

    lps = computeLPS(pattern)
    m, n = len(pattern), len(text)
    i = j = 0 
    res = []

    while i < n:

        while j > 0 and pattern[j] != text[i]:
            j = lps[j - 1]
        
        if pattern[j] == text[i]:
            j += 1 

        if j == len(pattern):
            res.append(i - m + 1)
            j = lps[j - 1]
        i += 1 
    
    return res 

if __name__ == '__main__':
    # text = "ababaababcabc"
    # pattern = "aba"

    # print(search(pattern,text))


    print(computeLPS("aacecaaa#aaacecaa"))




