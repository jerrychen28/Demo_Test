# coding:utf-8

import xlrd


def get_excel(file_name="D:\\Test\\pythonProject\\new\\data_for_test\\contact_mandatory_field_test_data.xlsx"):
    rows = []
    book = xlrd.open_workbook(file_name)
    sheet = book.sheet_by_index(0)
    for row in range(1, sheet.nrows):
        rows.append(list(sheet.row_values(row, 0, sheet.ncols)))
    return rows
