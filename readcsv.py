# using pandas
import pandas as pd

#case1:  reading csv file
#   type of df:    <class 'pandas.core.frame.DataFrame'>
df = pd.read_csv("C:/Users/felix/Desktop/Python Ex/pycsv.csv")
df


#   head() show the first 5 row data & header
df.head()


#case2:  reading xlsx file
df2 = pd.read_excel("C:/Users/felix/Desktop/新增 Microsoft Excel 工作表 (3).xlsx")

#   creating subdataframe usingf [['header1','header2',...]]
df2[['Job ID', 'Posting Title']]

#casting a dictionary to a dataframe
dict = {"header1": ['r1h1', 'r2h1', 'r3h1', 'r4h1'], "header2":['r1h2', 'r2h2', 'r3h2', 'r4h2']} 
df3 = pd.DataFrame(dict)