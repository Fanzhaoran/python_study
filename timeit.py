import timeit

c = """
sum = []
for i in range(1000):
    sum.append(i)
"""

print timeit.timeit(stmt="[i for i in range(1000)]", number=100000)
print timeit.timeit(stmt=c, number=100000)
输出：
3.79257702827
9.0510661602
