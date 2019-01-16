c_input = input("请输入一个字符串")
c_str = list(c_input)
#存储个数以及字符
c_str.append(0)   #把数字0作为检索字符串的结束字符
l = []
count = 1
for i in range(0,len(c_str)-1):
    if c_str[i] == c_str[i+1]:
        count += 1
    else:
        l.append(c_str[i])
        l.append(count)
        count=1
for j in l:
    if j == 1:
        l.remove(j)
print(l)
