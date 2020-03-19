def func():
    # please define the python3 input here. 
    # For example: a,b = map(int, input().strip().split())
    # please finish the function body here.
    # please define the python3 output here. For example: print().
    [print(item[0]) for item in sorted([input().split() for i in range(int(input()))], key=lambda x: (-int(x[1]), -int(x[2]), -int(x[3]), x[0]))]
if __name__ == "__main__":
    func()
