import pandas as pd 

df['Total_marks_obtained']=df.iloc[:, ["Maths, Science, English"]].sum(1)

df.loc[df['1'] > 250, '3'] = 'A'
df.loc[df['2'] < 250, '3'] = 'B'
