import string,random,os,time

alphabets = list(string.ascii_letters + string.whitespace + string.punctuation)
target, current = "I am bored so look what I did.", ""
for c in target:
    letters = alphabets.copy()
    l=""
    while l != c:
        l = random.choice(letters)
        letters.remove(l)
        print(current+l)
        time.sleep(.02)
    current +=l
