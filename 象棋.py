from tkinter import *
import tkinter.font as tkFont  #字体大小

root = Tk()
root.title("象棋棋盘")

can = Canvas(root,width=642,height=740)
can.create_line((0,2),(640,2),width=6)


for n in range(1,11):
    can.create_line((0,80*(n-1)+2),(640,80*(n-1)+2),width=3)
#画两个边界
can.create_line((4,2),(4,722),width=3)
can.create_line((640,2),(640,722),width = 3)

#中间竖线
for i_top in range(1,8):
    can.create_line((80*i_top,2),(80*i_top,322),width = 3)

for i_down in range(1,8):
    can.create_line((80*i_down,402),(80*i_down,722),width = 3)

#加字 楚界和汉界

can.create_text(160,362,text = "楚界")
can.create_text(480,362,text = "汉界")

#画田
can.create_line((240,2),(400,162),width = 3)
can.create_line((400,2),(240,162),width =3 )

can.create_line((240,562),(400,722),width =3)
can.create_line((400,562),(240,722),width =3)

##
can.pack()
root.mainloop()