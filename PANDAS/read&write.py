import pandas as pd
student_df= pd.read_csv('student.csv')
print(student_df)

# write the data into a file named student_export.csv
student_df.to_csv('student_export.csv', index= False)