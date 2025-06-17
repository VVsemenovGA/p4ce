from matplotlib import pyplot
from openpyxl import load_workbook

wb = load_workbook('C:\\Py\\data_analysis_lab.xlsx')


def getvalue(x):
    return x.value

sheet = wb['Data']
list_x = list(map(getvalue, sheet['A'][1:]))
list_y1 = list(map(getvalue, sheet['C'][1:]))
list_y2 = list(map(getvalue, sheet['D'][1:]))

pyplot.plot(list_x, list_y1)
pyplot.plot(list_x, list_y2)
pyplot.show()

