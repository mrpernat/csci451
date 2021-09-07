def zAlg(string):
    s = list(string)
    n = len(s)
    z = [-1] * n
    l, r = 0, 0
    for k in range(1, n):
        if k > r:
            i = 0
            while k + i < n and s[k + i] == s[i]:
                i += 1
            z[k] = i
            if i > 0:
                r = k + i - 1
                l = k
        else:
            k_prime = k - l
            beta = r - k + 1
            if z[k_prime] < beta:
                z[k] = z[k_prime]
            else:
                i = r + 1
                while i < n and s[i - k] == s[i]:
                    i += 1
                z[k] = i - k
                l = k
                r = i -1
    return(z)

def patternMatch(text, pattern):
    m = len(list(pattern))
    string = pattern + "$" + text
    zArr = zAlg(string)
    
    matches = 0
    for i in zArr:
        if i == m:
            matches += 1
    print("There are " + str(matches) + " matches.")
    

text = "cgattagacccattgact"
pattern = "att"
patternMatch(text, pattern)