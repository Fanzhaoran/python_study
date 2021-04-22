import xlrd
import os


class ReadExcel:

    def __init__(self, excel_path, sheetName="Sheet1"):
        self.data = xlrd.open_workbook(excel_path)
        # 获取页脚 默认sheet1
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行作为key
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowSum = self.table.nrows
        # 获取总列数
        self.colSum = self.table.ncols

    def dict_data(self):
        if self.rowSum <= 1:
            print("总行数小于1")
            return
        else:
            res = []
            index = 1
            for i in range(1, self.rowSum):
                s = {}
                values = self.table.row_values(index)
                for x in range(self.colSum):
                    s[self.keys[x]] = values[x]
                res.append(s)
                index += 1
            return res


if __name__ == '__main__':
    filepath = os.path.join("opt.xlsx")
    data = ReadExcel(filepath)
    print(data.dict_data())
    # 获取索引
    print(data.keys)
