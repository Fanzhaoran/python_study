# !/usr/bin/python3
# @File: flored.py
# --coding:utf-8--
# @Author:fzr
# @Time: 2022年05月27日

from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=10) as executor:
    future = executor.submit(pow, 323, 1235)
    print(future.result())


class People(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def getinfo(cls, info):
        name, age = map(str, info.split(","))
        info = cls(name, age)
        return info


p = People('张三', 2)
print(p.name)
print(p.age)

k = People.getinfo('李四,18')
print(k.name)
print(k.age)

