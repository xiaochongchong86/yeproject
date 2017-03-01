#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlrd


def read_excel():
    data = xlrd.open_workbook(r'user_data.xls')
    print data.sheet_names()

    table1 = data.sheets()[0]
    print table1

    nrows = table1.nrows
    ncols = table1.nocls
    print nrows, ncols

    for i in range(nrows):
        print "row %s: %s " % (i, table1.row_values(i))

    cell_A1 = table1.cell(0, 0).value
    cell_C3 = table1.cell(1, 1).value
    print cell_A1, cell_C3

    cell_A1 = table1.row(0)[0].value
    cell_A2 = table1.row(1)[0].value
    print cell_A1, cell_A2

if __name__ == '__main__':
    read_excel()