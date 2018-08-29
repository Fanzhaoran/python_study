#globals()返回全局变量的字典
class P:
    
    def __init__(self):
        pass
    def __call__(self,n):  #函数重构。再加一个功能
        g = globals()   #返回函数全局变量的字典
        
        #print(g)       #如果有兴趣可以加上看看
        for key in g:
            if g[key] == self:
                x = key[1:]    #x为截取变量名第一个字符之后的字符
                no = int(x)    #转化为整数
                print(n/no)
                break  
p2 = P()
p2(8)
p3 = P()
p3(9)
