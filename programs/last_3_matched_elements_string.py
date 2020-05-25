def last_3_matched_elements(s, ch):
    l = []
    l2 = []
    # for i in range(len(s)):
    #     if s[i] == ch:
    #         l.append(i)
    # for i in range(len(l)- 3, len(l)):
    #     l2.append(l[i])
    # return l2
    count = 0
    for i in range(-1, -len(s)-1, -1):
        if (s[i] == ch) & (count < 3):
            l.append(len(s) + i)
            count += 1
    
    a = [l2.append(len(s) + i) for i in range(-1, -len(s)-1, -1) if (s[i] == ch)]
    print(a, "in a")
    return l


s = "abcaabcbahjkadkhadkaha"
ch = input("enter the character to be matched  : ")
print(last_3_matched_elements(s, ch))