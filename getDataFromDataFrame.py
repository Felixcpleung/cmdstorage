import pandas as pd

dict = {"header1": ['r1h1', 'r2h1', 'r3h1', 'r4h1'], "header2":['r1h2', 'r2h2', 'r3h2', 'r4h2']} 
df3 = pd.DataFrame(dict)

df3

#  header1 header2  h
#0    r1h1    r1h2  1
#1    r2h1    r2h2  1
#2    r3h1    r3h2  1
#3    r4h1    r4h2  1

#>>>>>>>> Getting i,j entry <<<<<<<<<<<<<<<<<<

#  method1: .loc[x-index, 'y-header']   , 0-indexed
df3.loc[0,'header1']
#'r1h1'

#  method2: .iloc[x-index, y-index]
df3.iloc[0,0]
#'r1h1'  

#Remark:   .ix[x,y] do the .loc first, if it can't find suitable label, it use .iloc[x,y] but .ix is deprecated


#>>>>>>>>> Slicing          <<<<<<<<<<<<<<<

#index-based, so only 2-by-2 dataframe
df3.loc[0:2,'header1':'header2']
#  header1 header2
#0    r1h1    r1h2
#1    r2h1    r2h2
#2    r3h1    r3h2

#index-based, so only 2-by-2 dataframe
df3.iloc[0:2,0:2]
#  header1 header2
#0    r1h1    r1h2
#1    r2h1    r2h2