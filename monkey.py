from functools import lru_cache

@lru_cache()
def f(n):
    if n<3:
        return 1
    elif n==3:
        return 2
    else:
        return f(n-1)+f(n-3)
def func():
    # please define the python3 input here. 
    # For example: a,b = map(int, input().strip().split())
    # please finish the function body here.
    # please define the python3 output here. For example: print().
    while True:
        try:
            n=int(input())
            print(f(n))
        except EOFError:
            break
    
if __name__ == "__main__":
    func()
