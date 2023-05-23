
def first():
    (s := input().lower());print("Процентное соотношение G и C:", (s.count('g') + s.count('c')) / len(s) * 100)

def second():
    s = input().lower()
    if not len(s):
        print('')
        return
    
    result = ""
    c = 1
    ls = s[0]
    for i in range(1, len(s)):
        if s[i] != ls:
            result += ls + str(c)
            ls = s[i]
            c = 1
        else:
            c += 1
    result += ls + str(c)
    print(result)

first()
second()