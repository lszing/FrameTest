import xlrd
import xlwt
import os


def read_excel_all(file_name):
    data = list()
    book = xlrd.open_workbook(file_name)
    sheet = book.sheet_by_index(0)
    nrows = sheet.nrows  # 获取已存在数据的行数
    ncols = sheet.ncols  # 获取已存在数据的列数
    sheet.cell_value()
    for i in range(nrows):
        tmp = list()
        if sheet.cell(i, 0) is None or sheet.cell(i, 1).value == '':
            break
        for j in range(ncols):
            tmp.append(sheet.cell(i, j).value)
        data.append(tmp)
    return data


if __name__ == '__main__':
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_name = path + '\\data\\test.xls'
    print(file_name)
    print(read_excel_all(file_name))


    def read_excel_all1(file_name):
        data = list()
        book = xlrd.open_workbook(file_name)
        sheet = book.sheet_by_index(0)
        nrows = sheet.nrows
        ncols = sheet.ncols
        for i in range(nrows):
            tmp = list()
            if sheet.cell(i, 0) is None or sheet.cell(i, 1).value == '':
                break
            for j in range(ncols):
                tmp.append(sheet.cell(i, j))
            data.append(tmp)
        return data


    print(read_excel_all1(file_name))


    def read_excel_all2(file_name):
        data = []
        book = xlrd.open_workbook(file_name)
        sheet = book.sheet_by_index(0)
        nrows = sheet.nrows
        ncols = sheet.ncols
        for i in range(nrows):
            temp = []
            if sheet.cell(1, 0) is None or sheet.cell(i, 1).value == '':
                break
            for j in range(ncols):
                temp.append(sheet.cell(i, j).value)
            data.append(temp)
        return data


    print(read_excel_all2(file_name))


    def read_excel_all3(file_name):
        data = []
        book = xlrd.open_workbook(file_name)
        sheet = book.sheet_by_index(0)
        nrows = sheet.nrows
        ncols = sheet.ncols
        for i in range(nrows):
            temp = []
            if sheet.cell(i, 1).value == '' or sheet.cell(i, 0) is None:
                return False
            for j in range(ncols):
                temp.append(sheet.cell(i, j).value)
            data.append(temp)
        return data
