# !/usr/bin/python3
# @File: getC.py
# --coding:utf-8--
# @Author:fzr
# @Time: 2022年05月31日
import subprocess


cmd = "tcping 59.219.204.43 13001"
p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,close_fds=True)

for i in iter(p.stdout.readline,'b'):
    if not i:
        break
    print(i.decode('gbk'), end='')
    if "Port is open" in i.decode('gbk'):
        print(i.decode('gbk').split("/")[0])


