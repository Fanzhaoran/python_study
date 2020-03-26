# If you need to import additional packages or classes, please import here.

def func():
    # please define the python3 input here.
    # For example: a,b = map(int, input().strip().split())
    # please finish the function body here.
    # please define the python3 output here. For example: print().
    s1= input().strip()
    s2= input().strip()
    keys_public = []
    global MA
    MA = 0
    for i in range(len(s1)):
        for j in range(i+1, len(s1)):
            k = s1[i:j]
            m = len(k)
            if k in s2:
                if m > MA:
                    MA = m
                    keys_public.append(k)
    if len(keys_public)>0:
        change = keys_public[-1]
        print(change)
        if len(change)==len(s1) and len(s1)==len(s2):
            print("-1")
            return
        print(s1.replace(change,"")+s2.replace(change,""))
    else:
        print("-1")


if __name__ == "__main__":
    func()
