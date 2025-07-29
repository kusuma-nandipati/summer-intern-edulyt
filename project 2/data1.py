import pandas as pd

# Load the Excel file
xls = pd.ExcelFile('Credit Banking - 3.xls')

# Save each sheet as CSV
xls.parse('cb2').to_csv('cb2.csv', index=False)
xls.parse('ci').to_csv('ci.csv', index=False)

