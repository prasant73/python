import cProfile

def parenthesis_match(s):
    last_opening = [] # list declaration
    for i in range(len(s)):
        if s[i] == "(":
            last_opening.append(i)
            print(last_opening)
        if s[i] == ")":
            print("the corresponding opening bracket to the closing bracket at index {} is at {} position".format(i, last_opening.pop()))
            print(last_opening)


s = """Somebody (I suppose Raj(or Shyam)) has stolen (or robbed(I don't know)) the Empire's crown (or Kohinoor(or the biggest diamond ever))"""

cProfile.run("parenthesis_match(s)")