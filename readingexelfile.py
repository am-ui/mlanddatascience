import xlrd
loc = ("C:\\Users\\AMIT\\Desktop\\diamond.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
for i in range(0, 5):
    print(sheet.cell_value(0, i))
#import panda as pd
#df=pd.read_excel(r'C:\Users\AMIT\Desktop\diamond.xlsx')
#print(df)