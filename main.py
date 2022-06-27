# pip install tabula-py
import tabula

#tables=tabula.read_pdf('weather.pdf', pages=1)

#print(tables) # 
#print(type(tables))     # tables is a list
#print(tables[0])        # 
#print(type(tables[0]))  # tables[0] is a dataframe containing the table, so table is a list of dataframes, each containing a table

#Extract a table to a CSV file
#tables[0].to_csv('weather.csv', index=None)

# Now for a PDF containing a table and free text
tables=tabula.read_pdf('Table+and+Text.pdf', pages=1)
tables[0].to_csv('output.csv', index=None)

# To write to an Excel file (instead of  CSV), first install openpyxl
# pip install openpyxl
tables[0].to_excel('output.xlsx', index=None)
