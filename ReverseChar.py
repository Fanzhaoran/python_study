def func():
    # please define the python3 input here. 
    # For example: a,b = map(int, input().strip().split())
    # please finish the function body here.
    # please define the python3 output here. For example: print().
    print("".join([i.lower() if ord(i)<=90 else i.upper() for i in input().strip()]))
    # input().strip().swapcase()
    
if __name__ == "__main__":
    func()
