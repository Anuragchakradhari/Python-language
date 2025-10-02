import pandas as pd
Data = {'Name': ['Raghav','Rohan','Sameer'], 'Age':[23,56,18], 'Roll_no.':[3,6,5]}
df= pd.DataFrame(Data)
print(df)

# data= df.loc[0]
# print(data)

data= df.iloc[0]
print (data)