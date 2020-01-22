#>>>>>>>>>>>> Task1: Find the unique item in the column 'header1'  <<<<<
#>>>>>>>>>>>> Task2: Select rows base on criteria   <<<<<<
#>>>>>>>>>>>> Task3: Export the csv file            <<<<<<

import pandas as pd

dict = {"header1": [1, 2, 2, 4], "header2":[5, 6, 6, 8]} 
df1 = pd.DataFrame(dict)

df1

#   header1  header2
#0        1        5
#1        2        6
#2        2        8
#3        4        8

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~Task1: Find the unique item in the column 'header1' ~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Attribute only apply on 'Series', not 'DataFrame'
df1['header1'].unique()
#output:  array([1, 2, 4], dtype=int64)

type(df1['header1'].unique())
#<class 'numpy.ndarray'>



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~Task2: Select rows base on criteria ~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

df1['header1']>=2
#0    False
#1     True
#2     True
#3     True

type(df1['header1']>=2)
#<class 'pandas.core.series.Series'>

###### Note that: df1[[    ]] double bracket will give you a DataFrame instead, not Series]

#df1[Series] <---the select those row that has TRUE boolean value
df2 = df1[df1['header1']>=2]
df2
#   header1  header2
#1        2        6
#2        2        8
#3        4        8

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~ Task3: Export the csv file  ~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
df2.to_csv('pythoncsv.csv')
