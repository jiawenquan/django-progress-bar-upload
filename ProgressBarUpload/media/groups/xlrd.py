import xlrd

b = xlrd.open_workbook("./test.xls")

print b.nsheets # print number of sheets
print b.sheet_names() # and their names

s = b.sheet_by_index(0) # select first sheet

print s.nrows # number of rows
print s.ncols # number of columns

print s.row_values(0) # print first row
print s.col_values(1) # and second column

# get slice of column = 2 for rows = 1..6
a = s.col_values(2,1,6)

print a
print sum(a) # and print their sum

# get value of cell

d = s.cell(2,3).value

print d

# to convert value of date cell to tuple

dt = xlrd.xldate_as_tuple(d,b.datemode)

print dt